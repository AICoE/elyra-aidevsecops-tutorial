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

USE_NEURAL_MAGIC = bool(int(os.getenv("TUTORIAL_USE_NEURAL_MAGIC", 0)))
USE_PYTORCH = bool(int(os.getenv("TUTORIAL_USE_PYTORCH", 0)))
USE_PYTORCH_ONNX_IN_TF = bool(int(os.getenv("TUTORIAL_USE_PYTORCH_ONNX_IN_TF", 0)))

if USE_NEURAL_MAGIC:
    from deepsparse import compile_model

elif USE_PYTORCH:
    import torch
    import torch.nn as nn
    from torch.autograd import Variable
    from torchvision import transforms as transforms

elif USE_PYTORCH_ONNX_IN_TF:
    import onnx
    from onnx_tf.backend import prepare

else:
    import tensorflow as tf



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
                "THOTH_AIDEVSECOPS_MODEL_VERSION", "tf-210915165333-7b04047d1220f5cd"
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

        if USE_NEURAL_MAGIC:
            onnx_filepath = f"{trained_model_path}/{model_version}.onnx"
            batch_size = 1

            # Compile
            loaded_model = compile_model(onnx_filepath, batch_size)

        elif USE_PYTORCH:
            # The NN needs to be redefined
            # MNIST dataset parameters.
            num_classes = 10  # total classes (0-9 digits).

            class CNN(nn.Module):
                def __init__(self):
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
                            padding=2
                        ),     
                        nn.ReLU(),                      
                        nn.MaxPool2d(kernel_size=2),                
                    )

                    # fully connected layer, output 10 classes
                    self.out = nn.Linear(64 * 7 * 7, num_classes)

                def forward(self, x):
                    x = self.conv1(x)
                    x = self.conv2(x)
                    # flatten the output of conv2 to (batch_size, 32 * 7 * 7)
                    x = x.view(x.size(0), -1)
                    output = self.out(x)
                    return output, x    # return x for visualization

            loaded_model = CNN()
            loaded_model.load_state_dict(torch.load(f"{trained_model_path}/{model_version}/pytorch_model.pt"))
            # loaded_model = torch.load(f"{trained_model_path}/{model_version}/pytorch_model.pt")

        elif USE_PYTORCH_ONNX_IN_TF:
            loaded_model = onnx.load(f"{trained_model_path}/{model_version}")  # load onnx model

        else:
            loaded_model = tf.keras.models.load_model(
                f"{trained_model_path}/{model_version}", compile=False
            )

        self.model = loaded_model
        self.model_version = model_version

    def predict(self, image):
        """Make prediction using MNIST classifcation model."""
        if USE_NEURAL_MAGIC:
            # reshape
            image_ = np.array(image).reshape(1, 1, 28, 28).astype(np.float32)
            # https://github.com/neuralmagic/deepsparse/blob/60a905c4b08c3f27220df8537663c50267f27ddc/src/deepsparse/engine.py#L296
            prediction = self.model.run([image_])
            pred_y = prediction[0].argmax()
            return pred_y, prediction[0].tolist()[0][pred_y]

        elif USE_PYTORCH:
            image_ = torch.Tensor(np.array(image))
            self.model.eval()
            with torch.no_grad():
                output, last_layer = self.model(image_)
                pred_y = torch.max(output, 1)[1].data.squeeze()
                return pred_y, output.tolist()[0][pred_y]

        elif USE_PYTORCH_ONNX_IN_TF:
            # reshape
            image_ = image.reshape(1, 1, 28, 28).astype(np.float32)

            prediction = prepare(self.model).run(image_)
            return prediction._0.argmax(), prediction._0.tolist()[0][prediction._0.argmax()]

        else:
            # Default is TensorFlow model
            # reshape
            image_ = np.array(image).reshape(1, 28, 28, 1)
            prediction = self.model.predict(image_)
            return prediction.argmax(), prediction[0][prediction.argmax()]
