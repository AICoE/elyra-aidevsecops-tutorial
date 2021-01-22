"""Common method."""

from pathlib import Path
import tensorflow as tf
# Path to data
directory_path = Path.cwd().parents[0]
trained_model_path = directory_path.joinpath(
    str(os.environ.get("TRAINED_MODEL_PATH", "models"))
)
model_version = str(os.environ.get("MODEL_VERSION", "210122170201-e49249594c43e14a") 

loaded_model = tf.keras.models.load_model(
    f"{trained_model_path}/{model_version}/", custom_objects=None, compile=True, options=None
)

