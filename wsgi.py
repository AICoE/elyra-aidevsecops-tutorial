#!/usr/bin/env python3
#
# Copyright(C) 2020 Red Hat, Thoth Team
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


"""Thoth AIDevSecOps Tutorial App."""

import os
import logging
import time
import json

from version import __version__

from flask_cors import CORS
from flask import Flask
from flask import request
from flask import redirect, jsonify


from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import generate_latest

import numpy as np

from src.model import Model

_LOGGER = logging.getLogger("aidevsecops-tutorial")
_LOGGER.info("Thoth AIDevSecOps Tutorial v%s", __version__)

_REDIRECT_URL = os.getenv(
    "THOTH_AIDEVSECOPS_REDIRECT_URL",
    "https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/README.md",
)

application = Flask("aidevsecops-tutorial")

# Add Cross Origin Request Policy to all
CORS(application)

prometheus_metrics = PrometheusMetrics(application, group_by="endpoint")

# static information as metric
prometheus_metrics.info(
    "aidevsecops_tutorial_app_info", "App version deployed", version=__version__
)

model = Model()

# custom metric to expose model version
model_version_metric = prometheus_metrics.info(
    "aidevsecops_tutorial_model_info",
    "Model version deployed",
    version=model.model_version,  # label
)


@application.before_first_request
def before_first_request_callback():
    """Register callback, runs before first request to this service."""
    model_version_metric.set(1)
    _LOGGER.info("Running once before first request to expose metric.")


@application.after_request
def extend_response_headers(response):
    """Just add my signature."""
    response.headers["X-Thoth-AIDevSecOps-Tutorial-Version"] = f"v{__version__}"
    return response


@application.route("/")
def main():
    """Show this to humans."""
    return redirect(_REDIRECT_URL, code=308)


@application.route("/predict", methods=["POST"])
def predict():
    """Evaluate prediction."""
    image_list = request.get_json()["inputs"]

    # reshape
    image_array = np.array(image_list)

    start = time.monotonic()
    prediction, probability = model.predict(image_array=image_array)
    latency = time.monotonic() - start

    return json.dumps(
        {
            "prediction": int(prediction),
            "latency": latency,
            "probability": float(probability),
        }
    )

def _healthiness():
    return jsonify({"status": "ready", "version": model.model_version}), 200, {"ContentType": "application/json"}


@application.route("/readiness")
def api_readiness():
    """Report readiness for OpenShift readiness probe."""
    return _healthiness()


@application.route("/liveness")
def api_liveness():
    """Report liveness for OpenShift readiness probe."""
    return _healthiness()


@application.route("/metrics")
def metrics():
    """Return the Prometheus Metrics."""
    return generate_latest().decode("utf-8")


if __name__ == "__main__":
    _LOGGER.debug("Debug mode is on")
    application.run(host="0.0.0.0", port=8080)
