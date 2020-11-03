#!/usr/bin/env python3
# elyra-aidevsecops-tutorial
# Copyright(C) 2020 Francesco Murdaca
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

"""Download dataset from TensorFlow."""

import os
import logging
import pickle

from pathlib import Path

# set up logging
DEBUG_LEVEL = bool(int(os.getenv("DEBUG_LEVEL", 0)))

if DEBUG_LEVEL:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

_LOGGER = logging.getLogger(__name__)

IMPORT_DATASET = str(os.environ.get("TUTORIAL_TF_IMPORT_DATASET", "mnist"))

if IMPORT_DATASET == "mnist":
    _LOGGER.info("Selected MNIST Dataset: MNIST handwritten digits dataset.")
    from tensorflow.keras.datasets import mnist as tf_dataset

elif IMPORT_DATASET == "cifar10":
    _LOGGER.info(
        "Selected cifar10 Dataset: CIFAR10 small images classification dataset."
    )
    from tensorflow.keras.datasets import cifar10 as tf_dataset

elif IMPORT_DATASET == "cifar100":
    _LOGGER.info(
        "Selected cifar100 Dataset: CIFAR100 small images classification dataset."
    )
    from tensorflow.keras.datasets import cifar100 as tf_dataset

elif IMPORT_DATASET == "fashion_mnist":
    _LOGGER.info("Selected fashion_mnist Dataset: Fashion-MNIST dataset.")
    from tensorflow.keras.datasets import fashion_mnist as tf_dataset


def _is_file_downloaded(file_downloaded_path: Path) -> bool:
    """Check if file is already downloaded."""
    if os.path.exists(file_downloaded_path):
        _LOGGER.info("{} already exists, skipping ...".format(file_downloaded_path))
        return True

    return False


def download_dataset_from_tf() -> None:
    """Download Datasets from tf and store them locally."""
    # Set path where to store
    directory_path = Path.cwd().parents[1]
    destination_path = directory_path.joinpath(
        str(os.environ.get("DESTINATION_DATASET", "data/raw"))
    )

    if not os.path.exists(destination_path):
        destination_path.mkdir(parents=True, exist_ok=True)

    # Prepare MNIST data.
    (x_train, y_train), (x_test, y_test) = tf_dataset.load_data()

    dataset = {
        "xdata.pkl": x_train,
        "ydata.pkl": y_train,
        "xtestdata.pkl": x_test,
        "ytestdata.pkl": y_test,
    }

    # Store MNIST data for next step.
    for data_name, data_file in dataset.items():

        file_downloaded_path = destination_path.joinpath(data_name)

        if not _is_file_downloaded(file_downloaded_path):
            output = open(file_downloaded_path, "wb")
            pickle.dump(data_file, output)
            output.close()
            _LOGGER.info("Stored {}".format(file_downloaded_path))


if __name__ == "__main__":
    download_dataset_from_tf()
