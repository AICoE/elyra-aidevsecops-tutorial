
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

([WIP](https://github.com/thoth-station/jupyterlab-requirements/issues/53)) The use of the JupyterLab notebook is powered by Thoth Extension for Dependency Management on JupyterLab.
If you want to know more meanwhile, have a look at this [video](https://www.youtube.com/watch?v=IBzTOP4TCdA).

## GitOps, reproducibility, portability and traceability with AI support

Nowadays, developers (including Data Scientists) use Git and GitOps practices to store, share all code (e.g. notebooks, models) on development platforms (e.g. GitHub).
GitOps best practices help reproducibility and traecability for all projects avaialble.

One of the most important requirement for reproducibility is dependencies management. Having dependencies clearly stated allow for reusability and portability of notebooks,
which can be reused in another projects and shared safely with other Data Scientists.

(WIP) If you want to know more about this issue in the data science domain, have a look at this [article](https://github.com/thoth-station/jupyterlab-requirements).

[Project Thoth][6] helps developers keep these dependencies up to date integrating its recommendation in developers daily tools. If you want to know more have a look [here](https://thoth-station.ninja/docs/developers/adviser/integration.html).
Thanks to these tooling, the developers (including data scientists) do not have to worry about dependency management, which can be handled by bot and automated pipelines.
Moreover having AI support can lead to improvement in the developer of AI project, speeding up steps due to performance improvements or avoiding security issues due to the introduction
of libraries that should not be used production.

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

## 2. Start the environment

Get access to Operate First environment and become a user there, so that you can benefit from all the tools and support and you can focus on your AI project.

1. Get familiar with [Operate First][2] environment.

2. Access [JupyterHub][4] and select Elyra image.

<div style="text-align:center">
<img alt="Jupyter Hub UI" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/JupyterHubUI.png">
</div>

Each of the following steps is iterative if you are following ML Ops lifecycle (e.g. you need to change your model, new dependency is added). Using the tools described you can see that using AI, bot and automated pipelines will off load lot of work from developers (including data scientists) that can be focused on other more important aspects of the AI project.

## 3. Clone your repo and start working

Once you are logged in into Elyra image provided by ODH, you can use the Git extension provided to clone [this repo](https://github.com/thoth-station/elyra-aidevsecops-tutorial.git).

- Click the Git extension button:

<div style="text-align:center">
<img alt="Look for Git extension button" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/ElyraGitExtension.png">
</div>

- Insert the link to the GitHub repo you want to clone:

<div style="text-align:center">
<img alt="Clone your repo" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/CloneYourRepo.png">
</div>

## Manage dependencies for your new notebook

(WIP) Use Jupyterlab requirements. For each notebook you can follow similar pattern, in this way you can guarantee all notebooks are in sync with their dependencies and you are using the correct kernel.

## Start working on your notebooks

For the purpose of this tutorial you fill find the following steps:

1. Download your data with a [Python script](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/src/data/download_dataset_from_tf.py) or [Jupyter notebook](https://github.com/thoth-station/elyra-aidevsecops-tutorial/notebooks/download_dataset.ipynb);

2. Train the model in a [Jupyter notebook](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/notebooks/training.ipynb) and store model locally;

3. Create your [Elyra AI pipeline](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/tutorial.pipeline) on Elyra to retrain your model automatically using step 1. and 2;

        <div style="text-align:center">
        <img alt="Elyra AI Pipeline example" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/AI-pipeline.png">
        </div>

4. Create runtime to be used in Kubeflow pipeline.

    - Select the Runtime Tab (there are more buttons to see Runtimes in the menu tab or in the pipeline editor as well):

<div style="text-align:center">
<img alt="Look for Git extension button" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/ElyraGitExtension.png">
</div>

    - Start creating new Runtime:

<div style="text-align:center">
<img alt="Clone your repo" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/CloneYourRepo.png">
</div>

    - Insert all inputs for the Runtime:

<div style="text-align:center">
<img alt="Clone your repo" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/CloneYourRepo.png">
</div>

    (WIP) Show inputs for Kubeflow pipeline.

    (WIP) Show how to [create a new bucket](https://github.com/operate-first/support/blob/main/docs/claiming_object_store.md) for storing your results.

5. Run your pipeline and move to Kubeflow Pipeline UI provided to see what is happening.

For more examples on how to create an AI pipeline in Elyra, you can use this [link](https://github.com/elyra-ai/examples/tree/master/pipelines/hello_world_kubeflow_pipelines).

## Store your changes on your GitHub repo

(WIP) Whenever you finish working on your project or you need to stop, push your changes to GitHub, so that all your work can be save. In order to do that:

- You can create an SSH key and link it to your GitHub project.

- You can use your Github token.

## 4. Create an application to expose your model (simple case using Flask for example)

Once you trained your model and you stored it (locally in this case), you can start working on your application to expose your model.

For the purpose of this tutorial we show how to create a simple [application](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/wsgi.py) using Flask
exposing some useful endpoints (e.g `/predict` and `/metrics`).

## Use automated pipelines and benefit from AI and bots

Using AICoE tooling you can rely on bots helping you as described above:

When you install [Kebechet Bot][7] you can benefit from automatic pipelines and dependency management updates:

- (WIP) you can use Kebechet to create release about your project (have a look at [.thoth.yaml](https://github.com/thoth-station/thamos) description);

- (WIP) you can use Kebechet to create image on registry (e.g. quay) (have a look at [.aicoe.yaml](https://github.com/AICoE/aicoe-ci) description);

- (WIP) you get checks on your Pull Requests (have a look at [.aicoe.yaml](https://github.com/AICoE/aicoe-ci) description);

- (WIP) you get automatic updates for your dependencies in case of CVE, new releases, performance changes;

- (WIP) you get smart changelog creation using AI model in Kebechet after you ask for release.

## 5. Deploy your model on Operate First

These are the typical steps you need to follow to have a new application deployed on [Operate First][2]:

1. Create all manifests for your project (e.g. deployment, service, routes, workflows, pipelines) and place them in your repo under `/manifests`.

2. [Request access to a namespace](https://github.com/operate-first/support/issues/new?assignees=&labels=onboarding&template=onboarding_to_cluster.md&title=) where you want to deploy your application.

3. [Request support for deployment of your application](https://github.com/operate-first/support/issues/new?assignees=&labels=onboarding&template=onboarding_argocd.md&title=).

In this way [ArgoCD](https://argoproj.github.io/argo-cd/) will be used to maintain your application always in sync with your current changes once you make a new release (e.g. you changed your model, you added a new metric, you added a new feature).

## 6. Test prediction

If you want to test the application created in this tutorial from your local machine:

1. Install dependencies using [Pipenv](https://github.com/pypa/pipenv)

        ```shell
          pipenv install
        ```

    or [micropipenv](https://pypi.org/project/micropipenv/):

        ```shell
          micropipenv install
        ```

2. Start application.

        ```shell
          pipenv run python3 wsgi.py
        ```

3. Run test that will show the input image and then return the prediction from the model.

        ```shell
          pipenv run python3 src/test.py
        ```

If you want to test the application deployed you need to provide the URL:

        ```shell
          THOTH_AIDEVSECOPS_TUTORIAL_MODEL_URL=<MODEL_DEPLOYED_URL> pipenv run python3 src/test.py
        ```

## 7. Monitor your model and application with Prometheus and Grafana

1. (WIP) Request Prometheus scraping the model endpoint `/metrics`.

2. (WIP) Request creation of new Grafana dashbord for the model to see how the application and model are performing.

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
[8]: https://github.com/marketplace/khebhut
