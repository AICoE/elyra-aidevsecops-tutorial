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


"""Define Model class."""

import os

from pathlib import Path

import tensorflow as tf


class Model:
    """Model to handle prediction for MNIST classification."""

    def __init__(self):
        """Load model once when app starts."""
        # Path to data
        directory_path = Path.cwd()
        trained_model_path = directory_path.joinpath(
            str(os.environ.get("THOTH_AIDEVSECOPS_TRAINED_MODEL_PATH", "models"))
        )
        model_version = str(
            os.environ.get(
                "THOTH_AIDEVSECOPS_MODEL_VERSION", "210124112759-d97fd1f46b13ee40"
            )
        )

        loaded_model = tf.keras.models.load_model(
            f"{trained_model_path}/{model_version}", compile=False
        )
        self.model = loaded_model
        self.model_version = model_version

    def predict(self, image_array):
        """Make prediction using MNIST classifcation model."""
        # reshape
        image = image_array.reshape(1, 28, 28, 1)

        prediction = self.model.predict(image)
        return prediction.argmax(), prediction[0][prediction.argmax()]
