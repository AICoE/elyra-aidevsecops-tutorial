# Start working on your notebooks

For the purpose of this tutorial, the notebooks have been created already.

## Manage dependencies for your new notebook

Click on the `Manage Dependencies` button to interact with the JupyterLab extension for dependency management. For more documentation how to use this tool, [click here][1].

<div style="text-align:center">
<img alt="Jupyter Hub UI" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/JupyterLabRequirementsExtension.jpg">
</div>

You can use this extension for each notebook to guarantee all notebooks have the correct dependencies and kernel.

The notebooks that will be used in an AI Pipeline are:

1. [download_dataset.ipynb](../../notebooks/download_dataset.ipynb) for downloading the MNIST dataset from Tensorflow. _NOTE: in [Elyra][2] this step can also be performed with the provided [Python script](../../data/download_dataset_from_tf.py)_

2. [training.ipynb](../../notebooks/training.ipynb) for training the model for MNIST Classification and storing it locally or in cloud object storage

## Next Step

[Push changes to GitHub](./push-changes.md)

## References

* [JupyterLab extension for dependency management][1]
* [Elyra][2]

[1]: https://github.com/thoth-station/jupyterlab-requirements
[2]: https://github.com/elyra-ai/elyra
