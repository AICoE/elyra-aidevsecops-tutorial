#!/usr/bin/env python3
#
# Copyright(C) 2020, 2021 Red Hat, Thoth Team
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""Test model and gather metrics."""

import logging
import requests
import json
import os
import sys

from tensorflow.keras.datasets import mnist as tf_dataset

import numpy as np

_LOGGER = logging.getLogger(__name__)


def download_test_dataset():
    """Download test dataset to run script."""
    # Prepare MNIST data.
    _, (x_test, y_test) = tf_dataset.load_data()

    dataset = {
        "x_test": x_test,
        "y_test": y_test,
    }

    return dataset


def main_test():
    """Run main test to gather metrics for data scientists and AI DevOps Engineers."""
    dataset = download_test_dataset()

    x_test = dataset["x_test"]

    y_test = dataset["y_test"]

    # Convert to float32.
    x_test = np.array(x_test, np.float32)

    # Normalize images value from [0, 255] to [0, 1].
    x_test = x_test / 255.0

    addr = os.getenv("DEPLOYED_MODEL_URL", "http://localhost:8080")
    test_url = addr + "/predict"

    # prepare headers for http request
    headers = {"content-type": "application/json"}

    results = []

    total_tests = len(x_test)
    n = 1

    for img, number in zip(x_test, y_test):
        _LOGGER.info(f"test number {n}/{total_tests}")
        data = json.dumps({"inputs": img.tolist()})

        try:
            # send http request with image and receive response
            response = requests.post(test_url, data=data, headers=headers)
        except Exception as model_test_error:
            _LOGGER.error(f"Error during gathering of metrics: {model_test_error}")
            break

        # decode response
        json_response = response.json()

        prediction = json_response["prediction"]
        latency = json_response["latency"]
        probability = json_response["probability"]

        if int(number) == int(prediction):
            error = 1
        else:
            error = 0

        results.append({"error": error, "latency": latency, "probability": probability})

        n += 1

    report = {
        "average_latency": np.mean([r["latency"] for r in results]),
        "average_error": np.mean([r["error"] for r in results]),
    }

    json.dump(report, sys.stdout, indent=2)


if __name__ == "__main__":
    main_test()
