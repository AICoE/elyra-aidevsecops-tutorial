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
import logging

import numpy as np

from behave import given, when, then

_DEBUG_LEVEL = bool(int(os.getenv("DEBUG_LEVEL", 0)))

if _DEBUG_LEVEL:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

_LOGGER = logging.getLogger(__name__)


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
    addr = f"{context.model_api_url}"
    test_url = addr + "/predict"

    # prepare headers for http request
    headers = {"content-type": "application/json"}

    results = []

    total_tests = int(os.getenv("TUTORIAL_MAX_REQUESTS_TEST", 10000))

    n = 1

    for img, number in context.dataset:
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
            answer = 0
        else:
            answer = 1

        results.append(
            {"error": answer, "latency": latency, "probability": probability}
        )

        if n == total_tests:
            break

        n += 1

    context.custom_inputs = {"number_requests": n}

    context.results = results

    assert context.results


@then("I should get model and application metrics")
def get_model_metrics_report(context):
    """Get report from metrics collected."""
    report = {
        "average_latency": np.mean([r["latency"] for r in context.results]),
        "average_error": np.mean([r["error"] for r in context.results]),
        "average_probability": np.mean([r["probability"] for r in context.results]),
        "number_requests": context.custom_inputs["number_requests"],
    }

    context.store_metrics_path = os.getenv("STORE_METRICS_PATH", "metrics.json")

    context.report = report

    # TODO: embed in behave report once feature is available > 1.2.6
    with open(context.store_metrics_path, "w") as metrics:
        json.dump(report, metrics, indent=2)

    return context.report
