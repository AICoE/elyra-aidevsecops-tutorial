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

import os
import logging

import numpy as np
from tensorflow.keras.datasets import mnist as tf_dataset
from behave import given

_DEBUG_LEVEL = bool(int(os.getenv("DEBUG_LEVEL", 0)))

if _DEBUG_LEVEL:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

_LOGGER = logging.getLogger(__name__)


@given("dataset is available from Tensorflow")
def dataset_availability(context):
    """Check availability of dataset and retrieves it."""
    # Prepare MNIST data.
    _, (x_test, y_test) = tf_dataset.load_data()

    # Convert to float32.
    x_test = np.array(x_test, np.float32)

    # Normalize images value from [0, 255] to [0, 1].
    x_test = x_test / 255.0

    test_data = zip(x_test, y_test)

    context.dataset = test_data

    assert context.dataset
