
# Elyra AIDevSecOps Tutorial

This repo contains a demo application (MNIST Classication).
It is used to discuss the interface between Data Science and Dev/DevOps using project templates, pipelines and bots.

## AIDevSecOps

Data Scientists are not so different from developers and DevSecOps practices can be applied to MLOps ones. (AIDevSecOps).

Developers (Data Scienstist included) can rely on AI for support on their daily work.

[Project Thoth][1] develops tools that can enhance developers work, reducing their workload on mundane tasks that can be automatically handlded by bots.
This tutorial show one example of how AI ([Project Thoth][1]) can support AIDevSecOps and it will be focused on the use of an AI centric tool called [Elyra][2],
JupyterLab extensions to handle notebooks and Python scripts, backed by AI pipelines.

## GitOps, reproducibility, portability and traceability with AI support

Nowadays, developers (including Data Scientists) use Git and GitOps practices to store, share all notebooks, sources on development platforms (e.g. GitHub).
GitOps best practices help reproducibility and traecability for all projects avaialble. One of the most important requirement for reproducibility is dependencies management.

Having dependencies clearly stated allow for reusability and portability of notebooks, which can be reused in another projects.

[Project Thoth][1] helps developers keep these depencies up to date, moreover improve developers work creating software stacks for their project that satisfies developers requirements.
These requirments might across the AIDevSecOps lifecycle of a project, therefore the software stack requirements can change as well.

For the purpose of this tutorial the type of recommendations requested are different depending on the step of the pipeline required. See [.thoth.yaml file](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/.thoth.yaml).

## Project templates

The project template used can be found here: [project-template][3] which show correlation between data scientists requirements and AI dev ops engineers ones.

- The use of github templates for actions that can be automated by bots (e.g. release (patch, minor, major), deliver container image, dependency updates)

- The use of overlays directory ([WIP](https://github.com/aicoe-aiops/project-template/issues/28)) highlights the different requirements that are used during ML project lifecycle. The management and optimization of each step can be done automatically using Thoth recommendation engine and bots. Different images corresponding to the overlays can be created automatically and used in a pipeline (e.g Elyra using Kubeflow Pipeline).

## Environment and tools

This tutorial has been created using [Operate First][4] infrustructure and [Open Data Hub][5] tools provided, available on [Operate First][4].
If you are interested in using it, just get in touch, it's an open source initiative.

From [Open Data Hub][5] tools in particular we will use:

- [JupyterHub][6], to launch images with Jupyter tooling.
- [Elyra][2], which is a set of AI-centric extensions to JupyterLab Notebooks.

The use of the notebook is powered by Thoth Extension for Dependency Management on JupyterLab ([WIP](https://github.com/thoth-station/jupyterlab-requirements/issues/53)).
If you want to know more, have a look at this [video](https://www.youtube.com/watch?v=IBzTOP4TCdA).

## Automated piipelines and bots


# Tutorial

## 1. Set your project using a template

In this tutorial we rely on [project-template][3] as described above to have a common structures that easily understood by data scientists and dev ops in order to find all the bits required from ML lifecycle and from the DevOps lifecycle.

## 2. Start working on your project through Elyra


Get access to Operate First environment and become a user there, so that you can benefit from all the tooling and support and you can focus on your AI project.

1. Access [Operate First][4] environment.

2. Access [JupyterHub][6] and select Elyra image.


## 3. Start creating your code and notebooks

1. Download your data with a [Python script](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/src/data/download_dataset_from_tf.py) or [Jupyter notebook](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/notebooks/download_dataset.ipynb);

2. Train the model in a [Jupyter notebook](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/notebooks/training.ipynb) and store model locally;

3. Create and run your [AI pipeline](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/tutorial.pipeline) on Elyra to retrain your model automatically using step 1. and 2;

Whenever you finish working on your project or you need to stop, push your changes to GitHub, so that all your work can be traced and not lost. In order to do that:

- You can use your token
- You can create an SSH key and linked it to your GitHub project.

## 4. Create an application to expose your model (simple case using Flask for example)

Create your [application](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/wsgi.py) to expose endpoints (e.g `/predict` and `/metrics`).

## 5. Create an image

Using Thoth/AICoE tooling you can rely on bots helping you:

1. Install [Kebechet][7] bot to benefit from automatic pipelines and dependency management:

- you can use Kebechet to create release about your project (have a look at [.thoth.yaml](https://github.com/thoth-station/thamos) description);

- you can use Kebechet to create image on registry (e.g. quay) (have a look at [.aicoe.yaml](https://github.com/AICoE/aicoe-ci) description);

- you get checks on your Pull Requests (have a look at [.aicoe.yaml](https://github.com/AICoE/aicoe-ci) description);

- you get automatic updates for your dependencies in case of CVE, new releases, performance changes;

- you get smart changelog creation using AI model in Kebechet after you ask for release.

## 6. Deploy your model on Operate First

These are the typical steps you need:

1. Create all manifests for deployment (e.g. deployment, service, routes)

2. Request access to a namespace

3. Request support for deployment of your application.

## 7. Test prediction

If you want to test the deployment:

1. Run test that will show the input image and then return the prediction from the model.

```shell
  THOTH_AIDEVSECOPS_TUTORIAL_MODEL_URL=<MODEL_DEPLOYED_URL> pipenv run python3 src/test.py
```

If you want to test locally:

1. Install dependencies using pipenv

```shell
  pipenv install
```

or micropipenv:

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

## 8. Monitor your model and application with Prometheus and Grafana

1. Request Prometheus scraping the model endpoint `/metrics`.

2. Request creation of new Grafana dashbord for the model to see how the application and model are performing.


## References

 * [Project Thoth][1]
 * [Elyra][2]
 * [project-template][3]
 * [Operate First][4]
 * [Open Data Hub][5]
 * [JupyterHub][6]
 * [Kebechet][7]

[1]: https://thoth-station.ninja/
[2]: https://github.com/elyra-ai/elyra
[3]: https://github.com/aicoe-aiops/project-template
[4]: https://www.operate-first.cloud/
[5]: https://opendatahub.io/
[6]: https://jupyter.org/hub
[7]: https://github.com/marketplace/khebhut
