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
import typing
from pathlib import Path
import numpy as np

import torch
import torch.nn as nn


class CNN(nn.Module):
    """CNN for MNIST using Pytorch."""

    def __init__(self):
        """init."""
        super(CNN, self).__init__()
        self.conv1 = nn.Sequential(
            nn.Conv2d(
                in_channels=1,
                out_channels=32,
                kernel_size=5,
                stride=1,
                padding=2,
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
        )
        self.conv2 = nn.Sequential(
            nn.Conv2d(
                in_channels=32,
                out_channels=64,
                kernel_size=5,
                stride=1,
                padding=2,
            ),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
        )
        num_classes = 10  # total classes (0-9 digits).
        # fully connected layer, output 10 classes
        self.out = nn.Linear(64 * 7 * 7, num_classes)

    def forward(self, x):
        """Forward step."""
        x = self.conv1(x)
        x = self.conv2(x)
        # flatten the output of conv2 to (batch_size, 32 * 7 * 7)
        x = x.view(x.size(0), -1)
        output = self.out(x)
        return output, x  # return x for visualization


class Model:
    """Model to handle prediction for MNIST classification."""

    def __init__(self) -> None:
        """Load model once when app starts."""
        # Path to data
        use_ceph = bool(int(os.getenv("TUTORIAL_USE_CEPH", 0)))

        directory_path = Path.cwd()
        trained_model_path = directory_path.joinpath(
            str(os.environ.get("THOTH_AIDEVSECOPS_TRAINED_MODEL_PATH", "models"))
        )

        model_version = str(
            os.environ.get(
                "THOTH_AIDEVSECOPS_MODEL_VERSION", "torch-210921163030-5341ad0f6f389a55"
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

        # The NN needs to be redefined
        # MNIST dataset parameters.
        loaded_model = CNN()
        loaded_model.load_state_dict(
            torch.load(f"{trained_model_path}/{model_version}/pytorch_model.pt")
        )
        # loaded_model = torch.load(f"{trained_model_path}/{model_version}/pytorch_model.pt")

        self.model = loaded_model
        self.model_version = model_version

    def predict(self, image: typing.Any) -> typing.Tuple[float, float]:
        """Make prediction using MNIST classifcation model."""
        image_ = torch.Tensor(np.array(image))
        self.model.eval()
        with torch.no_grad():
            output, last_layer = self.model(image_)
            pred_y = torch.max(output, 1)[1].data.squeeze()
            sm = torch.nn.Softmax()
            probabilities = sm(output)
            return pred_y, probabilities.tolist()[0][pred_y]
