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

import pickle
import logging
import requests
import json
import os
from pathlib import Path

import numpy as np

_LOGGER = logging.getLogger(__name__)


def main_test():
    """Run main test to gather metrics for data scientists and AI DevOps Engineers."""
    dataset = ["xtestdata.pkl", "ytestdata.pkl"]

    directory_path = Path.cwd().parents[1]

    dataset_path = directory_path.joinpath(
        str(os.environ.get("DATASET_PATH", "data/raw/mnist_datasets_tf"))
    )

    # Retrieve test dataset.
    with open(dataset_path.joinpath(dataset[0]), "rb") as pklxtest_file:
        x_test = pickle.load(pklxtest_file)

    with open(dataset_path.joinpath(dataset[1]), "rb") as pklytest_file:
        y_test = pickle.load(pklytest_file)

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

    _LOGGER.info(f"Result from script is: \n {report}")

    output = json.dumps(report, sort_keys=True, indent=2)

    output_fp = os.environ.get("SCRIPT_OUTPUT_PATH")

    if output_fp:
        dir_name = os.path.dirname(output_fp)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        with open(output_fp, "w") as output_file:
            output_file.write(output)


if __name__ == "__main__":
    main_test()
