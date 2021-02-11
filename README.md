
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

From [Open Data Hub][3] tools in particular we will use:

- [JupyterHub][4], to launch images with Jupyter tooling.
- [Elyra][5], which is a set of AI-centric extensions to JupyterLab Notebooks (e.g. interface with Kubeflow Pipeline, Git, Python scripts).

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

## 1. Set your project using a template

In this tutorial we rely on [project-template][1] as described above to have a common structures that can be easily used by data scientists and devops in order to find all the bits required from ML lifecycle and from the DevOps lifecycle.

In order to use this template go to [project-template][1] and select `use the template` from the button provided in template repositories.

<div style="text-align:center">
<img alt="AI Project Template" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/AIProjectTemplate.png">
</div>

## 2. Fork this repo from GitHub into your account

Check [Fork a repo](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) from GitHub docs.

## 3. Get access to Operate First and open JupyterHub to spawn the Elyra image

Get access to Operate First environment and become a user there, so that you can benefit from all the tools and support and you can focus on your AI project.

1. Get familiar with [Operate First][2] environment.

2. Access [JupyterHub][4] and select Elyra image.

<div style="text-align:center">
<img alt="Jupyter Hub UI" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/JupyterHubUI.png">
</div>

Each of the following steps is iterative if you are following ML Ops lifecycle (e.g. you need to change your model, new dependency is added). Using the tools described you can see that using AI, bot and automated pipelines will off load lot of work from developers (including data scientists) that can be focused on other more important aspects of the AI project.

## 4. Clone your repo from Elyra

Once you are logged in into Elyra image provided by ODH, you can use the Git extension provided to clone [this repo](https://github.com/thoth-station/elyra-aidevsecops-tutorial.git).

- Click the Git extension button:

<div style="text-align:center">
<img alt="Look for Git extension button" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/ElyraGitExtension.png">
</div>

- Insert the link to the GitHub repo you want to clone:

<div style="text-align:center">
<img alt="Clone your repo" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/CloneYourRepo.png">
</div>

## 5. Start working on your notebooks

## Manage dependencies for your new notebook

Use [jupyterlab extension for dependency management enhanced by AI](https://github.com/thoth-station/jupyterlab-requirements).
For each notebook you can follow similar pattern, in this way you can guarantee all notebooks are in sync with their dependencies and you are using the correct kernel.

For the purpose of this tutorial you fill find the following notebooks:

1. Download your data with a [Python script](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/src/data/download_dataset_from_tf.py) or [Jupyter notebook](https://github.com/thoth-station/elyra-aidevsecops-tutorial/notebooks/download_dataset.ipynb);

2. Train the model in a [Jupyter notebook](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/notebooks/training.ipynb) and store model locally or Ceph;

## 6. Store your changes on your GitHub repo

Whenever you finish working on your project or you need to stop, push your changes to GitHub, so that all your work can be saved. In order to do that:

- You can use your Github token directly from Elyra UI.

### Create GitHub token

If you don't have a GitHub token, you can create one following GitHub docs: [create GitHub token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).

## 7. Create a first release and image of your project

## Use automated pipelines and benefit from AI and bots

Using AICoE tooling you can rely on bots helping you as described above"

1. Verify that [.aicoe.yaml](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/.aicoe-ci.yaml) is correctly created and you have checks set.
Have a look at [AICoE Pipeline][8] description docs for more information.

<div style="text-align:center">
<img alt="Open Issue Release" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/OpenIssueRelease.png">
</div>

<div style="text-align:center">
<img alt="Pull Request Release" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/PullRequestRelease.png">
</div>

The changelog is created using AI model that cluster pull requests. You can find more information about `glyph project` [here](https://github.com/thoth-station/glyph).

## Verify your image is on your registry

Once the image has been created you can find it in your registry (e.g. Quay):

<div style="text-align:center">
<img alt="Image on Registry" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/ImageRegistry.png">
</div>

## Dependencies updates in the repo

When you install [Kebechet Bot][7] you can benefit from automatic pipelines and dependency management updates.
You get automatic updates for your dependencies in case of CVE, new packages releases, performance changes.

## 8. Run Elyra AI Pipeline

## Add image runtime

Now that your image is available we need to add it to Elyra:

1. Open tab to manage image runtime for Elyra

<div style="text-align:center">
<img alt="Manage Image Runtime Elyra" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/ManageRuntimeImageSettings.png">
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

## Request bucket for running the pipeline

Using Operate First you can request one once you get access to your namespace:

- [create a new bucket](https://github.com/operate-first/support/blob/main/docs/claiming_object_store.md).

## Create runtime to be used in Kubeflow pipeline

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

## Create Elyra AI Pipeline

1. Insert all steps you want and connect them using Elyra UI.

2. Insert inputs for each step/notebook in terms of image runtime, environment variables and resources.

3. Add comments and describe your steps (Optional)

4. Save your AI Pipeline

<div style="text-align:center">
<img alt="Elyra AI Pipeline example" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/AIPipeline.png">
</div>

You can find the above pipeline [here](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/tutorial.pipeline).

## Run AI Pipeline

Run your pipeline and move to [Kubeflow Pipeline UI](http://ml-pipeline-ui-kubeflow.apps.cnv.massopen.cloud/#/pipelines) to see what is happening.

For more examples on how to create an AI pipeline in Elyra, you can use this [link](https://github.com/elyra-ai/examples/tree/master/pipelines/hello_world_kubeflow_pipelines).

Once the pipeline finished you will you have your model stored on Ceph, you can check from your terminal using:

```bash
  ws s3 --profile moc-pipeline-kfp --endpoint https://rgw-openshift-storage.apps.cnv.massopen.cloud/ ls s3://{your_bucket}/{your_project_name}/models/
```

where `moc-pipeline-kfp` is the aws profile containing `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to access your bucket.

## 9. Create an application to expose your model (simple case using Flask)

Once you trained your model and you stored it on Ceph, you can start working on your application to expose your model.

For the purpose of this tutorial you can reuse the [application](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/wsgi.py) created using Flask, that 
exposes some useful endpoints (e.g `/predict` and `/metrics`).

## 10. Deploy your model on Operate First

These are the typical steps you need to follow to have a new application deployed on [Operate First][2]:

1. Create all manifests for your project (e.g. deployment, service, routes, workflows, pipelines) and place them in your repo under `/manifests`.

2. [Request access to a namespace](https://github.com/operate-first/support/issues/new?assignees=&labels=onboarding&template=onboarding_to_cluster.md&title=) where you want to deploy your application.

3. [Request support for deployment of your application](https://github.com/operate-first/support/issues/new?assignees=&labels=onboarding&template=onboarding_argocd.md&title=).

In this way [ArgoCD](https://argoproj.github.io/argo-cd/) will be used to maintain your application always in sync with your current changes once you make a new release (e.g. you changed your model, you added a new metric, you added a new feature).

## 11. Test prediction from deployed application

### Using notebook in JupyterHub

If you want to test your application deployed in the cluster from JH you can use the following notebook:

- Test model [Jupyter notebook](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/notebooks/training.ipynb);

(You need to have credentials for the access to Operate First Openshift cluster and have access to the namespace you deployed your model to run the above notebook)

### From your local machine

If you want to test the application created in this tutorial from your local machine:

PRE-REQUISITE: Make sure you are logged in the cluster where the model is deployed.

1. Install dependencies using [Pipenv](https://github.com/pypa/pipenv)

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

## 12. Monitor your model and application with Prometheus and Grafana

1. (WIP) Request Prometheus scraping the model endpoint `/metrics`.

2. (WIP) Create new Grafana dashbord for the model to see how the application and model are performing.

## References

* [project-template][1]
* [Operate First][2]
* [Open Data Hub][3]
* [JupyterHub][4]
* [Elyra][5]
* [Project Thoth][6]
* [Kebechet Bot][7]
* [AICoE Pipeline][8]

[1]: https://github.com/aicoe-aiops/project-template
[2]: https://www.operate-first.cloud/
[3]: https://opendatahub.io/
[4]: https://jupyter.org/hub
[5]: https://github.com/elyra-ai/elyra
[6]: https://thoth-station.ninja/
[7]: https://github.com/marketplace/khebhut
[8]: https://github.com/AICoE/aicoe-ci
