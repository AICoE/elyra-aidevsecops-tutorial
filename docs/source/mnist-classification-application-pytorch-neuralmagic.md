# Explore the notebooks

For the purpose of this tutorial, the notebooks have been created already.

In particular, the notebooks that will be used are:

1. [download_dataset.ipynb](../../notebooks/neural-magic-torch-mnist/download_dataset.ipynb) for downloading the MNIST dataset from Pytorch.

2. [training.ipynb](../../notebooks/neural-magic-torch-mnist/training.ipynb) for training the model for MNIST Classification and storing it locally or in cloud object storage.

3. [convert_model_to_onnx.ipynb](../../notebooks/neural-magic-torch-mnist/training.ipynb) for converting the trained Pytorch model to [ONNX][6] model.

4. [sparsify.ipynb](../../notebooks/neural-magic-torch-mnist/training.ipynb) for sparsifying the model using [Neural Magic][1] Optimizer and recipe.


## Manage dependencies

Reproducibility and shareability of notebooks is very important if you want to allow others to repeat your experiments and avoid issues due to dependencies management.
When using `pip install <package_name>` is not possible to verify which software stack was used to run the notebook and therefore another user cannot repeat the same experiment.
Check the video [here](https://www.youtube.com/watch?v=ifyQ2oSxjnU) if you want to know more.

In order to avoid this issues, dependencies for jupyter notebooks in this tutorial are managed using the JupyterLab extension [jupyterlab-requirements][2].

You can use this extension for each of your notebook to guarantee they have the correct dependencies and kernel.
This extension is able to add/remove dependencies, lock them and store them in the notebook metadata.
In this way all the dependencies information required to repeat the environment are shipped with the notebook.

In particular, in the notebook metadata you can find:

- requirements (Pipfile)

- requirements locked with all hashes (Pipfile.lock)

- dependency resolution engine used (thoth or pipenv)

- configuration file for runtiment environment (.thoth.yaml if you are using thoth resolution engine)

All this information can allow reproducibility of the notebook.

There are 3 ways to interact with this extension:

- using `%horus` magic commands directly in your notebook's cells (preferred approach). To learn more about how to use the `%horus` magic commands check out the guide [here](https://github.com/thoth-station/jupyterlab-requirements#horus-magic-command) or the video [here](https://www.youtube.com/watch?v=FjVxNTXO70I)

<div style="text-align:center">
<img alt="JupyterLab Requirements Horus magic commands" src="https://raw.githubusercontent.com/AICoE/elyra-aidevsecops-tutorial/master/docs/images/JupyterLabRequirementsExtensionMC.png">
</div>

- using the `horus` CLI directly from terminal or integrated in pipelines ([check video](https://www.youtube.com/watch?v=fW0YKugL26g&t)).

<div style="text-align:center">
<img alt="JupyterLab Requirements Horus CLI" src="https://raw.githubusercontent.com/AICoE/elyra-aidevsecops-tutorial/master/docs/images/JupyterLabRequirementsExtensionCLI.png">
</div>

- using the `Manage Dependencies` button that appears in the notebook when it is opened:

<div style="text-align:center">
<img alt="JupyterLab Requirements UI" src="https://raw.githubusercontent.com/AICoE/elyra-aidevsecops-tutorial/master/docs/images/JupyterLabRequirementsExtension.jpg">
</div>

# Run the notebooks

For the notebooks in this tutorial, the dependencies have already been set.
You can check the status of your notebook by running `%horus check`:

<div style="text-align:center">
<img alt="Horus check command" src="https://raw.githubusercontent.com/AICoE/elyra-aidevsecops-tutorial/master/docs/images/JupyterLabHorusCheck.png">
</div>

You can check the dependencies content of your notebook by running `%horus show`:

<div style="text-align:center">
<img alt="Horus show command" src="https://raw.githubusercontent.com/AICoE/elyra-aidevsecops-tutorial/master/docs/images/JupyterLabHorusShow.png">
</div>

If you want to create the kernels to successfully run the notebooks, the only thing you have to do is run `%horus set-kernel` in one cell of the notebook.
This command will create a kernel with the requirements stated in your notebook, install the dependencies saved in the notebook and set the kernel for your notebook.

Once the command ends, you can save the notebook and delete that cell.

Now you are ready to run your notebook with the same environment that was used when the notebook was created in the first place!


## Next Step

[Push changes to GitHub](./push-changes.md)

## References

* [Neural Magic][1]
* [ONNX][2]
* [JupyterLab extension for dependency management][3]

[1]: https://neuralmagic.com/
[2]: https://onnx.ai/
[3]: https://github.com/thoth-station/jupyterlab-requirements
