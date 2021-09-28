#!/usr/bin/env python3
#
# Copyright(C) 2020, 2021 Francesco Murdaca
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
import boto3

from pathlib import Path
import numpy as np

from deepsparse import compile_model


class Model:
    """Model to handle prediction for MNIST classification."""

    def __init__(self):
        """Load model once when app starts."""
        # Path to data
        use_ceph = bool(int(os.getenv("TUTORIAL_USE_CEPH", 0)))

        directory_path = Path.cwd()
        trained_model_path = directory_path.joinpath(
            str(os.environ.get("THOTH_AIDEVSECOPS_TRAINED_MODEL_PATH", "models"))
        )

        model_version = str(
            os.environ.get(
                "THOTH_AIDEVSECOPS_MODEL_VERSION",
                "torch-210921164335-c352fe9b17e2f837_mnist_classification_pruned"
            )
        )

        if use_ceph:
            project_name = os.environ.get("PROJECT_NAME", "elyra-aidevsecops-tutorial")

            s3_endpoint_url = os.getenv(
                "ENDPOINT_URL",
                "https://s3-openshift-storage.apps.zero.massopen.cloud/",
            )
            s3_access_key = os.environ["AWS_ACCESS_KEY_ID"]
            s3_secret_key = os.environ["AWS_SECRET_ACCESS_KEY"]
            s3_bucket = os.getenv(
                "BUCKET_NAME",
                "elyra-aidevsecops-tutorial",
            )

            # Create an S3 client
            s3 = boto3.client(
                service_name="s3",
                aws_access_key_id=s3_access_key,
                aws_secret_access_key=s3_secret_key,
                endpoint_url=s3_endpoint_url,
            )

            key = f"{project_name}/models/{model_version}"
            file_downloaded_path = f"{trained_model_path}/{model_version}"

            s3.upload_file(
                Bucket=s3_bucket, Key=key, Filename=str(file_downloaded_path)
            )

        onnx_filepath = f"{trained_model_path}/{model_version}.onnx"
        batch_size = 1

        # Compile
        loaded_model = compile_model(onnx_filepath, batch_size)

        self.model = loaded_model
        self.model_version = model_version

    def predict(self, image):
        """Make prediction using MNIST classifcation model."""
        # reshape
        image_ = np.array(image).reshape(1, 1, 28, 28).astype(np.float32)
        # https://github.com/neuralmagic/deepsparse/blob/60a905c4b08c3f27220df8537663c50267f27ddc/src/deepsparse/engine.py#L296
        prediction = self.model.run([image_])
        pred_y = prediction[0].argmax()
        return pred_y, prediction[0].tolist()[0][pred_y]
