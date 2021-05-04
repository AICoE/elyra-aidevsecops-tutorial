#!/usr/bin/env python3
#
# Copyright(C) 2021 Francesco Murdaca
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

"""Basic integration test for AI Project."""

import requests
import json
import os
import sys
import logging

from tensorflow.keras.datasets import mnist as tf_dataset

import numpy as np

from behave import given, when, then

@given("dataset is available")
def dataset_availability(context):
    """Check availability of dataset and retrieves it."""
    # Prepare MNIST data.
    _, (x_test, y_test) = tf_dataset.load_data()

    context.dataset = {
        "x_test": x_test,
        "y_test": y_test,
    }

    assert context.dataset


@given("deployment is accessible")
def deployment_accessible(context):
    """Check the deployment is accessible."""
    context.result = {}

    context.model_api_url = os.environ["DEPLOYED_MODEL_URL"]

    response = requests.get(f"{context.model_api_url}")

    assert (
        response.status_code == 200
    ), f"Invalid response when accessing {context.model_api_url}: {response.status_code!r}: {response.text}"

    assert response.text, f"Empty response from server for {context.model_api_url}"


@when("I run test to gather metrics on predict endpoint")
def gather_metrics(context):
    """Gather metrics from the deployed ML model."""
    x_test = context.dataset["x_test"]

    y_test = context.dataset["y_test"]

    # Convert to float32.
    x_test = np.array(x_test, np.float32)

    # Normalize images value from [0, 255] to [0, 1].
    x_test = x_test / 255.0

    addr = f"{context.model_api_url}"
    test_url = addr + "/predict"

    # prepare headers for http request
    headers = {"content-type": "application/json"}

    results = []

    total_tests = len(x_test)
    n = 1

    for img, number in zip(x_test[:2], y_test[:2]):
        data = json.dumps({"inputs": img.tolist()})

        try:
            # send http request with image and receive response
            response = requests.post(test_url, data=data, headers=headers)
        except Exception as model_test_error:
            print(f"Error during gathering of metrics: {model_test_error}")
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

    context.results = results

    assert context.results


@then("I should get model and application metrics")
def get_model_metrics_report(context):
    """Get report from metrics collected."""
    report = {
        "average_latency": np.mean([r["latency"] for r in context.results]),
        "average_error": np.mean([r["error"] for r in context.results]),
    }

    context.report = report

    # TODO: embed in behave report once feature is available > 1.2.6
    with open('metrics.json', 'w') as metrics:
        json.dump(report, metrics, indent=2)

    return context.report
