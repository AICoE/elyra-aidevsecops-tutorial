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

import json
import os
import logging

import torch
from torchvision import datasets
from torchvision.transforms import ToTensor

from behave import given, when, then

_DEBUG_LEVEL = bool(int(os.getenv("DEBUG_LEVEL", 0)))

if _DEBUG_LEVEL:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

_LOGGER = logging.getLogger(__name__)


@given("dataset is available from Pytorch")
def dataset_availability(context):
    """Check availability of dataset and retrieves it."""
    # Prepare MNIST data.
    test_data = datasets.MNIST(
        root="./data/raw/pytorch-mnist-dataset",
        train=False,
        transform=ToTensor(),
    )

    loaders = {
        "test": torch.utils.data.DataLoader(
            test_data, batch_size=1, shuffle=True, num_workers=1
        ),
    }

    test_data = loaders["test"]

    context.dataset = test_data

    assert context.dataset