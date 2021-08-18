# Create AI Pipeline (using Elyra UI)

Creating an AI Pipeline consists of 3 steps:

* [Adding runtime images](#add-runtime-images-using-ui)
* [Creating runtime to be used in Kubeflow pipeline](#create-runtime-to-be-used-in-kubeflow-pipeline-using-ui)
* [Creating Elyra AI Pipeline](#create-elyra-ai-pipeline-using-the-ui)

## Add runtime images (using UI)

Now that your images are available on the registry, we need to add them to [Elyra][1] metadata. For that, we need to create a runtime image configuration which identifies the container image that Elyra can pull from our registry and utilize to run the Jupyter notebooks.

1. Open command palette (Cntrl + Shift + C) and select `"Manage Runtime Images"`.

<div style="text-align:center">
<img alt="Manage Image Runtime Elyra" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/ManageRuntimeImageSettingsCM.png">
</div>

2. Once the new panel has been opened on the left of the UI, click add button to create new image.

<div style="text-align:center">
<img alt="Manage Image Runtime Elyra" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/AddRuntimeImage.png">
</div>

3. Fill all required fields to create image for download dataset step:

- Name: `Tutorial Download Dataset Step`

- Image Name: `quay.io/thoth-station/elyra-aidevsecops-dataset:v0.11.0`

<div style="text-align:center">
<img alt="Fill inputs Image Runtime Elyra" src="https://raw.githubusercontent.com/AICoE/elyra-aidevsecops-tutorial/master/docs/images/FillInputsRuntimeImage.png">
</div>

The image is now available and can be used into your AI pipeline

<div style="text-align:center">
<img alt="Updated Runtime Images List" src="https://raw.githubusercontent.com/AICoE/elyra-aidevsecops-tutorial/master/docs/images/UpdatedRuntimeImageList.png">
</div>

4. Repeat steps 2, 3 to add `training` image using the following inputs:

- Name: `Tutorial Training Step`

- Image Name: `quay.io/thoth-station/elyra-aidevsecops-training:v0.11.0`

### Add runtime images (using CLI)

If you are more familiar with using CLI from the terminal you can use the following steps to create a runtime to run an AI Pipeline.

1. Open Terminal in JupyterLab

2. Run the following command with your specific inputs:

```bash
elyra-metadata install runtime-images --display_name="Tutorial Training Step" --description="Training Step Tutorial" --image_name="quay.io/thoth-station/elyra-aidevsecops-training:v0.10.0"
```

To learn more about adding runtime images, check the following [link](https://elyra.readthedocs.io/en/v2.0.1/user_guide/runtime-image-conf.html).

## Create runtime to be used in Kubeflow pipeline (using UI)

We also need to create a Kubeflow Pipeline Runtime configuration. This is configuration adds any additional information to the pipeline metadata that it will need to run on the external Kubeflow Pipeline instance and access any other data that may be required. This includes the KubeFlow endpoint and cloud object storage secrets.

1. Select the Kubeflow Pipeline Runtime Tab on the left panel of Jupyterlab UI or use the command palette (Cntrl + Shift + C) and select `"Manage Kubeflow Pipelines Runtimes"`.

NOTE: There is a button to view Runtimes in the menu tab and in the pipeline editor as well.

<div style="text-align:center">
<img alt="Elyra Runtime Tab" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/ElyraRuntimeTab.png">
</div>

2. Once the new panel has been opened on the left of the UI, click add button to create new Kubeflow Pipeline Runtime

<div style="text-align:center">
<img alt="Create new Runtime" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/CreateNewElyraRuntime.png">
</div>

3. Insert all inputs for the Runtime:

- Name: `Elyra AIDevSecOps Tutorial`

- Kubeflow Pipeline API Endpoint: `http://istio-ingressgateway-istio-system.apps.zero.massopen.cloud/pipeline`

- Kubeflow Pipeline Engine: `Tekton`

- Cloud Object Storage Endpoint: `OBJECT_STORAGE_ENDPOINT_URL`

- Cloud Object Storage Username: `AWS_ACCESS_KEY_ID`

- Cloud Object Storage Password: `AWS_SECRET_ACCESS_KEY`

- Cloud Object Storage Bucket Name: `OBJECT_STORAGE_BUCKET_NAME`

where `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `OBJECT_STORAGE_ENDPOINT_URL`, `OBJECT_STORAGE_BUCKET_NAME` are specific to the user cloud object storage selected.

<div style="text-align:center">
<img alt="Insert inputs in Elyra Runtime" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/InsertInputsElyraRuntime.png">
</div>

⚠️ Please note, if you're using a secure bucket, to avoid exposing your Cloud Object Storage credentials, you can use the `Cloud Object Storage Credentials Secret` which is a Kubernetes secret that’s defined in the Kubeflow namespace, containing the Cloud Object Storage username and password. This secret must exist on the Kubernetes cluster hosting your pipeline runtime in order to successfully execute pipelines.

Refer to this [template](https://elyra.readthedocs.io/en/stable/user_guide/runtime-conf.html#cloud-object-storage-credentials-secret-cos-secret) for an example of how to define your secret on the Kubernetes cluster hosting your runtime.

We have a secret defined on the Operate First Kubeflow Namespace called `opf-datacatalog-bucket` available for the `opf-datacatalog` bucket which can be used for the `Cloud Object Storage Credentials Secret` field if you are using the `opf-datacatalog` bucket here.

### Create runtime to be used in Kubeflow pipeline (using CLI)

If you are more familiar with using CLI from the terminal you can use the following steps to create a runtime to run an AI Pipeline.

1. Open Terminal in JupyterLab

2. Run the following command with your specific inputs (CLOUD_OBJECT_STORAGE_ENDPOINT, CLOUD_OBJECT_STORAGE_USERNAME, CLOUD_OBJECT_STORAGE_PASSWORD, CLOUD_OBJECT_BUCKET_NAME):

```bash
elyra-metadata install runtimes --display_name="KFP operate first" --api_endpoint="http://istio-ingressgateway-istio-system.apps.zero.massopen.cloud/pipeline" --engine=Tekton --cos_endpoint=CLOUD_OBJECT_STORAGE_ENDPOINT --cos_username=CLOUD_OBJECT_STORAGE_USERNAME --cos_password=CLOUD_OBJECT_STORAGE_PASSWORD --cos_bucket=CLOUD_OBJECT_BUCKET_NAME
```

To learn more about creating a Kubeflow pipeline runtime, check the following [link](https://elyra.readthedocs.io/en/v2.0.1/user_guide/runtime-conf.html).

## Create Elyra AI Pipeline using the UI

A pre-made pipeline called [elyra-aidevsecops-tutorial.pipeline](../../elyra-aidevsecops-tutorial.pipeline) already exists at the root of the repository. You can directly start with the pre-made pipeline and jump to step 3 to make sure that the image runtime for each notebook is selected along with the desired Resources, Environment Variables and Output Files.

To create a new pipeline from scratch, go through the following steps:

1. Open new Elyra Pipeline Editor

<div style="text-align:center">
<img alt="New Elyra Pipeline Editor" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/NewElyraPipelineEditor.png">
</div>

2. Insert all steps you want, moving notebooks to the editor and connect them using [Elyra][1] UI.

3. Click on 3 dots on the node, or the notebook and go to `Properties` to insert inputs for each step/notebook in terms of image runtime, environment variables, resources, file dependencies and output files.

<div style="text-align:center">
<img alt="Pipeline Steps Inputs" src="https://raw.githubusercontent.com/AICoE/elyra-aidevsecops-tutorial/master/docs/images/NotebookProperties.png">
</div>

4. Here is what each field in the node properties can be used for:

- **Filename**: This is the name of the node. this would be pre-filled when selecting a script or a notebook's properties.
- **Runtime Image**: Select the runtime image that was created in the previous steps. This identifies the container image required to run this node.
- **CPU, GPU, RAM**: Specify the resource requirements needed to run this script or notebook.
- **File Dependencies**: Any files that the notebook is dependent on (notebooks and scripts) such as for importing methods from can be specified here.
- **Environment Variables**: Specify the environment variables which are utilized within the notebooks and scripts here. To avoid exposing credentials of your secure bucket, you can use the Kubernetes Secret provided above in the Kubeflow Pipelines Runtime Configuration.
- **Output Files**: You can specify any files which are created during the execution and which might be needed by subsequent steps here.


<div style="text-align:center">
<img alt="Pipeline Steps Inputs" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/AIPipelineStepInputs.png">
</div>

The notebooks can exchange data using a cloud object storage and also using the Output Files which can be used to make certain files generated during execution available to all subsequent pipeline steps.

The `download_dataset` and `training` step of the pipeline have some mandatory and optional environment variables for running in automation which need to be set during this step of setting up the pipeline.

List of Environment Variables that need to be configured for the notebooks to run:
- The `download_dataset` step uses Output Files to make certain files available to the training step during execution. Make sure that the output files `data/raw/xdata.pkl`, `data/raw/xtestdata.pkl`, `data/raw/ydata.pkl`, `data/raw/ytestdata.pkl` are specified for the `download_dataset` step.
- Env variable `AUTOMATION` must be configured as 1 for both the notebooks to run in the pipeline.
- The `training` step also needs the cloud storage environment credentials like the `OBJECT_STORAGE_BUCKET_NAME` and `OBJECT_STORAGE_ENDPOINT_URL` to store the trained model on the S3 bucket.

  Please note, the `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` environment variables needed to run the `training` notebook are already defined in the Kubeflow Pipelines Runtime Configuration and can be accessed from there. If you are using the `Cloud Object Storage Credentials Secret`, that would contain both the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

The following images show the minimum list of environment variables that need to be configured for the `download_dataset` and `training` notebooks to run in Automation as outlined above.

<div style="text-align:center">
<img alt="Download Dataset Properties" src="https://raw.githubusercontent.com/AICoE/elyra-aidevsecops-tutorial/master/docs/images/DownloadDatasetProperties.png">
</div>

<div style="text-align:center">
<img alt="Training Properties" src="https://raw.githubusercontent.com/AICoE/elyra-aidevsecops-tutorial/master/docs/images/TrainingProperties.png">
</div>

5. To explain what each node in the pipeline is doing, you can add comments and describe your steps (Optional) by clicking on the Comment icon on the top panel.

<div style="text-align:center">
<img alt="Elyra AI Pipeline example" src="https://raw.githubusercontent.com/AICoE/elyra-aidevsecops-tutorial/master/docs/images/AddComments.png">
</div>

6. Save your AI Pipeline.

<div style="text-align:center">
<img alt="Elyra AI Pipeline example" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/AIPipeline.png">
</div>

You can find the above pipeline [here](../../elyra-aidevsecops-tutorial.pipeline).

## Next Step

[Run and Debug AI Pipeline](./run-ai-pipeline.md)

## References

* [Elyra][1]

[1]: https://github.com/elyra-ai/elyra
