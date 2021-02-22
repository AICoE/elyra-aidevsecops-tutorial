
# Elyra AIDevSecOps Tutorial

This tutorial is used to discuss the interface between Data Science and Dev/DevOps using project templates, pipelines and bots.

The demo application used is the "hello world" for AI: MNIST Classication

## Project templates

The project template used can be found here: [project-template][1].
It shows correlation between data scientists (e.g. data, notebooks, models) requirements and AI dev ops engineers ones (e.g. manifests).
Using a project template allows for shareability because anyone taking the project or look for something specific about the project can immediately identify
all the resources needed.

## Environment and tools

This tutorial has been created using [Operate First][2] infrustructure and the tools provided in [Open Data Hub][3], which is deployed on [Operate First][2].
If you are interested in using it, just get in touch, it's an open source initiative.

In particular in this tutorial we are going to use:

- [JupyterHub][4], to launch images with Jupyter tooling.
- [Elyra][5], which is a set of AI-centric extensions to JupyterLab Notebooks (e.g. interface with Kubeflow Pipeline, Git, Python scripts).
- [Kubeflow Pipelines][9], to allow end to end experiment using pipelines.
- [Tekton][10], used in CI/CD systems, can be adopted as backend of Kubeflow pipelines.

The use of the JupyterLab notebook is powered by Thoth Extension for Dependency Management on JupyterLab.
If you want to know more, have a look at this [repo]((https://github.com/thoth-station/jupyterlab-requirements)).

## GitOps, reproducibility, portability and traceability with AI support

Nowadays, developers (including Data Scientists) use Git and GitOps practices to store, share all code (e.g. notebooks, models) on development platforms (e.g. GitHub).
GitOps best practices help reproducibility and traceability for all projects available.

One of the most important requirement for reproducibility is dependencies management. Having dependencies clearly stated allow for reusability and portability of notebooks,
which can be reused in another projects and shared safely with other Data Scientists.

(WIP) If you want to know more about this issue in the data science domain, have a look at this [article](https://github.com/thoth-station/jupyterlab-requirements).

[Project Thoth][6] helps developers keep these dependencies up to date integrating its recommendation in developers daily tools. If you want to know more have a look [here](https://thoth-station.ninja/docs/developers/adviser/integration.html).
Thanks to this tooling, the developers (including data scientists) do not have to worry too much about dependency management (they still need to select their dependencies), which can be handled by a bot and automated pipelines.Hence, having AI support can lead to improvement in the development of AI project, speeding up steps due to performance improvements coming from dependencies and keeping your application secure because insecure libs cannot be introduced.

## Automated pipelines and bots for your GitHub project

- [Kebechet Bot][7] to keep your dependencies fresh and up to date receiving recommendations and justifications using AI.

- [AICoE Pipeline][8] to support your AI project lifecycle.

All these tools are integrated with the [project-template][1], therefore most of the things are already set for you.
One important task in order to mantain your code is to create tag on your project development lifecycle. Moreover in order to deploy your application you need to create a container image.
The use of github templates integrated with bots can provide you with automated pipelines triggered depending on what you need (e.g. release (patch, minor, major), deliver container image, dependency updates).

## AIDevSecOps

This tutorial wants to highlight that Data Scientists are not so different from developers and DevSecOps practices and tools can be applied to MLOps ones.

# Tutorial

## 0. Pre-requisites

There are two basics requirements for this tutorial:

- Gmail account required to login to [JupyterHub][4].

- GitHub account.

## 1. Fork this repo from GitHub into your account

Check [Fork a repo](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) from GitHub docs.

In this tutorial we rely on [project-template][1], as described above, in order to have a common structures that can be easily used by data scientists and devops. Have a structure for the projects in general allows others to find all the bits required for the ML lifecycle and from the DevOps lifecycle.

If you want to use this template for your AI project, go to [project-template][1] and select `use the template` from the button provided in template repositories.

<div style="text-align:center">
<img alt="AI Project Template" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/AIProjectTemplate.png">
</div>

## 2. Get access to Operate First and open JupyterHub to spawn the Elyra image

Get access to Operate First environment and become a user there, so that you can benefit from all the tools and support and you can focus on your AI project.

1. Get familiar with [Operate First][2] environment.

2. Access [JupyterHub][4] and select Elyra image called `ml-prague-workshop:latest` from the list of images.

Resources required for the tutorial: `default` for container size.

<div style="text-align:center">
<img alt="Jupyter Hub UI" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/JupyterHubUI.png">
</div>

NOTE: Each of the following steps is iterative if you are following ML Ops lifecycle (e.g. you need to change your model, new dependency is added). Having the tools described allows you to rely on AI, bots and automated pipelines to off load lot of work from developers (including data scientists) that can be focused on other more important aspects of the AI project.

## 3. Clone your repo from Elyra

Once you are logged in into Elyra image provided by ODH, you can use the Git extension provided to clone [this repo](https://github.com/thoth-station/elyra-aidevsecops-tutorial.git).

- Click the Git extension button:

<div style="text-align:center">
<img alt="Look for Git extension button" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/ElyraGitExtension.png">
</div>

- Insert the link to the GitHub repo you want to clone:

<div style="text-align:center">
<img alt="Clone your repo" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/CloneYourRepo.png">
</div>

## 4. Start working on your notebooks

## Manage dependencies for your new notebook

Use [jupyterlab extension for dependency management enhanced by AI](https://github.com/thoth-station/jupyterlab-requirements).
For each notebook you can follow similar pattern, in this way you can guarantee all notebooks are in sync with their dependencies and you are using the correct kernel.

For the purpose of this tutorial you fill find the following notebooks:

1. Download your data with a [Python script](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/src/data/download_dataset_from_tf.py) or [Jupyter notebook](https://github.com/thoth-station/elyra-aidevsecops-tutorial/notebooks/download_dataset.ipynb);

2. Train the model in a [Jupyter notebook](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/notebooks/training.ipynb) and store model locally or Ceph;

## 5. Store your changes on your GitHub repo

Whenever you finish working on your project or you need to stop, push your changes to GitHub, so that all your work can be saved. In order to do that:

1. Go to Git Box panel on the left and select Push Changs.

<div style="text-align:center">
<img alt="Use Button to Push Changes" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/UseButtonToPushChanges.png">
</div>

2. Insert username and token that to push to the GitHub repo.

<div style="text-align:center">
<img alt="Push Changes with GitHub token" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/PushGitHubToken.png">
</div>

Then go to your repo and open a Pull Request.

### Create GitHub token

If you don't have a GitHub token, you can create one following GitHub docs: [create GitHub token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).

## 6. Create a first release and image of your project

The following sub-sections of step 6 can be performed only if you have set your project with your pipelines.
For the purpose of the tutorial the images required are already created using these pipelines, therefore here you can find a description of how they have been created and where they are available.

## Ask for new release

Using pipelines like the AICoE tooling you can rely on bots helping you, as described above in the initial description.
These pipelines are described in [AICoE Pipeline][8] and you can use them for you projects if you are interested.

In this case the [.aicoe.yaml](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/.aicoe-ci.yaml) is created with all information relative to build (e.g. base image, build strategy, registry where to push) as described in [AICoE Pipeline][8] documentation.

The pipelines used in Thoth project are maintained by bots. Therefore you can open an issue asking for release (e.g patch, minor, major) and the bots will handle your request. One the request will be completed the bot will automatically close the issue as you can see from the images below:

<div style="text-align:center">
<img alt="Open Issue Release" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/OpenIssueRelease.png">
</div>

<div style="text-align:center">
<img alt="Pull Request Release" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/PullRequestRelease.png">
</div>

The changelog after the release is created using AI model that cluster pull requests. You can find more information about `glyph project` [here](https://github.com/thoth-station/glyph).

Once the issue is closed by the bot, a tag is created in the GitHub project and a pipeline starts in order to build and push the image on the registry according to the requirements inserted in the [.aicoe.yaml](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/.aicoe-ci.yaml).

## Image available on quay

Once the image has been created you can find it in your registry (e.g. Quay):

<div style="text-align:center">
<img alt="Image on Registry" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/ImageRegistry.png">
</div>

## Overlays

If you have overlays directory present, as for this tutorial, you can perform overlays builds thanks to the [AICoE Pipeline][8]. In this way you can create different images optimized for your steps in pipelines. In this case the AICoE tooling would create many images as number of overlays.

You can find the images required for tutorial named after the overlays requested:

- [download-dataset overlay](https://github.com/thoth-station/elyra-aidevsecops-tutorial/tree/master/overlays/download-dataset) -> quay.io/thoth-station/elyra-aidevsecops-dataset:v0.4.0 (download-dataset image)

- [training overlay](https://github.com/thoth-station/elyra-aidevsecops-tutorial/tree/master/overlays/training) -> quay.io/thoth-station/elyra-aidevsecops-training:v0.4.0 (training image)

- [inference overlay](https://github.com/thoth-station/elyra-aidevsecops-tutorial/tree/master/overlays/inference)  -> quay.io/thoth-station/elyra-aidevsecops-tutorial:v0.4.0 (inference image)

You can check the overlays build requirement in the [.aicoe.yaml](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/c86ce9c08665c12df0adf829db31bd19e8c61455/.aicoe-ci.yaml#L5).

All requirements for the overlay are created using Thoth resolution engine, you can find the inputs used for Thoth recommender in the [.thoth.yaml](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/bb6fad2441e8df8aa56c2c0e6b5ac45a2cda42eb/.thoth.yaml#L5).

## Dependencies updates in the repo

When you install [Kebechet Bot][7] you can benefit from automatic pipelines and dependency management updates.
You get automatic updates for your dependencies in case of CVE, new packages releases, performance changes.

## 7. Run AI Pipeline (using Elyra UI)

### Pre-requisites: Bucket to run Kubeflow pipeline

You can use your own bucket credentials, setting them as env variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

If you want a bucket from [Operate First][2], you need to follow the next steps:

1. [Request access to a namespace](https://github.com/operate-first/support/issues/new?assignees=&labels=onboarding&template=onboarding_to_cluster.md&title=) where you want to deploy your application.

2. [Request a new bucket](https://github.com/operate-first/support/issues/new?assignees=&labels=user-support&template=ceph_bucket_request.md&title=).

### Add runtime images

Now that your images are available we need to add them to Elyra:

1. Open command palette (Cntrl + Shift + C)

<div style="text-align:center">
<img alt="Manage Image Runtime Elyra" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/ManageRuntimeImageSettingsCM.png">
</div>

2. Click add button to create new image

<div style="text-align:center">
<img alt="Manage Image Runtime Elyra" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/AddRuntimeImage.png">
</div>

3. Fill all required fields to create image and save

<div style="text-align:center">
<img alt="Fill inputs Image Runtime Elyra" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/FillInputsRuntimeImage.png">
</div>

The image is now available and can be used into your AI pipeline

<div style="text-align:center">
<img alt="Updated Runtime Images List" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/UpdatedRuntimeImageList.png">
</div>

We repear the same steps to add `download-dateset` image and `training` image as we need them for the Elyra Pipeline.

### Create runtime to be used in Kubeflow pipeline

1. Select the Runtime Tab

NOTE: There are more buttons to see Runtimes in the menu tab or in the pipeline editor as well.

<div style="text-align:center">
<img alt="Elyra Runtime Tab" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/ElyraRuntimeTab.png">
</div>

2. Create new Runtime

<div style="text-align:center">
<img alt="Create new Runtime" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/CreateNewElyraRuntime.png">
</div>

3. Insert all inputs for the Runtime:

<div style="text-align:center">
<img alt="Insert inputs in Elyra Runtime" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/InsertInputsElyraRuntime.png">
</div>

### Create Elyra AI Pipeline using the UI

1. Open new Elyra Pipeline Editor

<div style="text-align:center">
<img alt="New Elyra Pipeline Editor" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/NewElyraPipelineEditor.png">
</div>

2. Insert all steps you want, moving notebooks to the editor and connect them using Elyra UI.

3. Insert inputs for each step/notebook in terms of image runtime, environment variables and resources.

<div style="text-align:center">
<img alt="Pipeline Steps Inputs" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/AIPipelineStepInputs.png">
</div>

4. Add comments and describe your steps (Optional).

5. Save your AI Pipeline.

<div style="text-align:center">
<img alt="Elyra AI Pipeline example" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/AIPipeline.png">
</div>

You can find the above pipeline [here](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/tutorial.pipeline).

### Run AI Pipeline

Using UI:

1. Use play button to run the AI Pipeline.

<div style="text-align:center">
<img alt="Elyra AI Pipeline play" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/PlayAIPipeline.png">
</div>

2. Before starting the pipeline you need to select which runtime environment to use and add a name for your pipeline.

<div style="text-align:center">
<img alt="Elyra AI Pipeline run inputs" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/AIPipelineRunInputs.png">
</div>

Run your pipeline and move to [Kubeflow Pipeline UI](http://ml-pipeline-ui-kubeflow.apps.cnv.massopen.cloud/#/pipelines) to see what is happening.

<div style="text-align:center">
<img alt="Kubeflow Pipeline UI" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/KFPUI.png">
</div>

For more examples on how to create an AI pipeline in Elyra, you can use this [link](https://github.com/elyra-ai/examples/tree/master/pipelines/hello_world_kubeflow_pipelines).

You can check the status of each step in the pipeline directly from the UI and debug from logs if any problems occur:

<div style="text-align:center">
<img alt="Successfull Kubeflow Pipeline" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/SuccessfullKubeflowPipeline.png">
</div>

The model is stored in your bucket, you can check from your terminal using [aws CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html):

```bash
  aws s3 --profile moc-pipeline-kfp --endpoint https://rgw-openshift-storage.apps.cnv.massopen.cloud/ ls s3://{your_bucket}/{your_project_name}/models/
```

where `moc-pipeline-kfp` is the aws profile containing `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to access your bucket.

## 8. Create an application to expose your model (simple case using Flask)

Once you trained your model and it is stored on Ceph, you can start working on your inference application to expose your model.

For the purpose of this tutorial you can reuse the [application](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/wsgi.py) created using Flask, that
exposes some useful endpoints (e.g `/predict` and `/metrics`).

## 9. Deploy your model on Operate First

These are the typical steps you need to follow to have a new application deployed on [Operate First][2]:

1. Create all manifests for your project (e.g. deployment, service, routes, workflows, pipelines) and place them in your repo under `/manifests`.

2. [Request support for deployment of your application](https://github.com/operate-first/support/issues/new?assignees=&labels=onboarding&template=onboarding_argocd.md&title=).

In this way [ArgoCD](https://argoproj.github.io/argo-cd/) will be used to maintain your application always in sync with your current changes. Once you create a new release of your application (e.g. you changed your model, you added a new metric, you added a new feature) and a new image is available, you need to update the [imagestreamtag](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/bb6fad2441e8df8aa56c2c0e6b5ac45a2cda42eb/manifests/overlays/test/imagestreamtag.yaml#L10) so that ArgoCD can deploy new version.

Note: [AICoE Pipeline][8] can also update automatically the [imagestreamtag](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/bb6fad2441e8df8aa56c2c0e6b5ac45a2cda42eb/manifests/overlays/test/imagestreamtag.yaml#L10) once a new release is created.

## 10. Test prediction from deployed application

### Using notebook in JupyterHub

If you want to test your application deployed in the cluster from JH you can use the following notebook:

- Test model [Jupyter notebook](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/notebooks/test_deployed_model.ipynb);

(You need to have credentials for the access to Operate First Openshift cluster and have access to the namespace you deployed your model to run the above notebook)

### From your local machine

If you want to test the application created in this tutorial from your local machine:

PRE-REQUISITE: Make sure you are logged in the cluster where the model is deployed.

1. Install dependencies using [Pipenv](https://github.com/pypa/pipenv).

```bash
  pipenv install
```

or [micropipenv](https://pypi.org/project/micropipenv/):

```bash
  micropipenv install
```

2. Start application.

```bash
  pipenv run python3 wsgi.py
```

3. Run test that will show the input image and then return the prediction from the model.

```bash
  pipenv run python3 src/test.py
```

If you want to test the application deployed you need to provide the URL:

```bash
  THOTH_AIDEVSECOPS_TUTORIAL_MODEL_URL=<MODEL_DEPLOYED_URL> pipenv run python3 src/test.py
```

## 11. Monitor your model and application with Prometheus and Grafana

1. Open issue in Operate First [Support] and equest Prometheus scraping the model endpoint `/metrics` for the application deployed in your namespace.

2. Create new Grafana dashbord for the metrics to see how the application and model are performing and open issue in Operate First [Support] on how to have your dashboard deployed.

## References

* [project-template][1]
* [Operate First][2]
* [Open Data Hub][3]
* [JupyterHub][4]
* [Elyra][5]
* [Project Thoth][6]
* [Kebechet Bot][7]
* [AICoE Pipeline][8]
* [Kubeflow Pipelines][9]
* [Tekton][10]

[1]: https://github.com/aicoe-aiops/project-template
[2]: https://www.operate-first.cloud/
[3]: https://opendatahub.io/
[4]: https://jupyter.org/hub
[5]: https://github.com/elyra-ai/elyra
[6]: https://thoth-station.ninja/
[7]: https://github.com/marketplace/khebhut
[8]: https://github.com/AICoE/aicoe-ci
[9]: https://www.kubeflow.org/docs/pipelines/overview/pipelines-overview/
[10]: https://tekton.dev/
