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


"""Test model."""

import requests
import json
import os

from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np


(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Convert to float32.
x_test = np.array(x_test, np.float32)

# Normalize images value from [0, 255] to [0, 1].
x_test = x_test / 255.0

addr = os.getenv("THOTH_AIDEVSECOPS_TUTORIAL_MODEL_URL", "http://localhost:8080")
test_url = addr + "/predict"

# prepare headers for http request
headers = {"content-type": "application/json"}

# select one test image
img = x_test[5890]
data = json.dumps({"inputs": img.tolist()})

# Check which image is sent
plt.imshow(img, cmap="gray")
plt.show(block=False)
plt.pause(1)
plt.close()

# send http request with image and receive response
response = requests.post(test_url, data=data, headers=headers)

# decode response
print(response.text)
