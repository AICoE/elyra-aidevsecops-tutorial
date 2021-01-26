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

from version import __version__

from flask_cors import CORS
from flask import Flask
from flask import request
from flask import redirect

from prometheus_client import generate_latest, Gauge

import numpy as np

from src.model import Model

_LOGGER = logging.getLogger("aidevsecops-tutorial")
_LOGGER.info("Thoth AIDevSecOps Tutorial v%s", __version__)

_GRAFANA_REDIRECT_URL = os.getenv(
    "THOTH_AIDEVSECOPS_GRAFANA_REDIRECT_URL",
    "https://grafana.datahub.redhat.com/"
)

application = Flask("aidevsecops-tutorial")

# Add Cross Origin Request Policy to all
CORS(application)

app_version = Gauge(
    "aidevsecops_tutorial_app_version",
    "App version deployed",
    ["app_version"]
)

model_version = Gauge(
    "aidevsecops_tutorial_model_version",
    "Model version deployed",
    ["model_version"]
)

model = Model()


@application.after_request
def extend_response_headers(response):
    """Just add my signature."""
    response.headers["X-Thoth-AIDevSecOps-Tutorial-Version"] = f"v{__version__}"
    return response


@application.route("/")
def main():
    """Show this to humans."""
    return redirect(_GRAFANA_REDIRECT_URL, code=308)


@application.route("/predict", methods=["POST"])
def predict():
    """Evaluate prediction."""
    image_list = request.get_json()['inputs']

    # reshape
    image_array = np.array(image_list)

    prediction, probability = model.predict(image_array=image_array)
    return {
        'response': f"The number in the image is {str(prediction)}"
                    f" with probability {str(probability)}"
    }


@application.route("/metrics")
def metrics():
    """Return the Prometheus Metrics."""
    app_version.labels(__version__).set(1)
    model_version.labels(model.model_version).set(1)

    return generate_latest().decode("utf-8")


if __name__ == "__main__":
    _LOGGER.debug("Debug mode is on")
    application.run(host="0.0.0.0", port=8080)
