# Start working on your notebooks

For the purpose of this tutorial, the notebooks have been created already.

## Manage dependencies for your new notebook

Use [jupyterlab extension for dependency management][1].
For each notebook you can follow similar pattern, in this way you can guarantee all notebooks are in sync with their dependencies and you are using the correct kernel.

The notebooks that will be used in an AI Pipeline are:

1. [download_dataset.ipynb](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/notebooks/download_dataset.ipynb) -> Download MNIST dataset from Tensorflow (NOTE in [Elyra][5] a step in a pipeline can also be performed with a [Python script](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/src/data/download_dataset_from_tf.py);

2. [test_deployed_model.ipynb](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/notebooks/training.ipynb) Train the model for MNIST Classification and store it locally or in the Cloud Object Storage;

## References

* [jupyterlab extension for dependency management][1]
* [Elyra][2]

[1]: https://github.com/thoth-station/jupyterlab-requirements
[2]: https://github.com/elyra-ai/elyra
