
# Elyra AIDevSecOps Tutorial

This tutorial is used to discuss the interface between Data Science and Dev/DevOps using project templates, pipelines and bots.
Moreover, it wants to highlight that Data Scientists are not so different from developers and DevSecOps practices and tools can be applied to MLOps ones.

The demo application used is the "hello world" for AI: MNIST Classification.

## Environment required

This tutorial has the following environment requirements to be run:

- [Open Data Hub][3] v1.0,
- [Openshift][11] (Enterprise Kubernetes),
- Cloud Object Storage (e.g. Ceph, minio).
- [Tekton][10], used in CI/CD systems, to run pipelines created by humans or machines.
- [ArgoCD][12], used for Continuous Deployment of your applications.
- Tutorial [container image](https://quay.io/repository/thoth-station/s2i-lab-elyra?tag=ml-prague-workshop&tab=tags):

```bash
jupyterhub==1.2.1
jupyterlab>=3.*
elyra>=2*
jupyterlab-requiremnts>=0.4.5
```

### Operate First Open Environment

[Operate First][2] Open Infrastructure environment has been selected to run this tutorial. It fullfills all the requirement stated above. If you are interested in using it, just get in touch with Operate First team, it's an open source initiative.

You can find some notes also regarding other environments in the different sections of the tutorial.

## Tools

In this tutorial the following technologies are going to be used:

- [JupyterHub][4], to launch images with Jupyter tooling.
- [Elyra][5], which is a set of AI-centric extensions to JupyterLab Notebooks (e.g. interface with Kubeflow Pipeline, Git, Python scripts).
- [Project Thoth][6] Extension for Dependency Management on JupyterLab. If you want to know more, have a look at this [repo]((https://github.com/thoth-station/jupyterlab-requirements)).
- [Kubeflow Pipelines][9], to allow end to end experiment using pipelines.

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

## Project templates

The project template used can be found here: [project-template][1].
It shows correlation between data scientists (e.g. data, notebooks, models) requirements and AI dev ops engineers ones (e.g. manifests).
Using a project template allows for shareability because anyone taking the project or look for something specific about the project can immediately identify
all the resources needed.

# Tutorial Steps

0. [Pre-requisities](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/docs/source/pre-requisite.md)

## ML Lifecycle/Source Lifecycle

1. [Setup your initial environment](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/docs/source/setup-initial-environment.md)

2. [Explore notebooks and manage dependencies](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/docs/source/explore-notebooks-and-manage-dependencies.md)

3. [Push changes to GitHub](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/docs/source/push-changes.md)

4. [Create release, build image or overlays builds for different images](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/docs/source/build-images.md)

4.1 [Benefit from bots to keep your dependencies fresh and up to date](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/docs/source/use-bots.md)

5. [Create an AI Pipeline](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/docs/source/create-ai-pipeline.md)

6. [Run and debug AI Pipeline](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/docs/source/run-ai-pipeline.md)

## DevOps Lifecycle

7. [Deploy Inference Application](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/docs/source/deploy-model.md)

8. [Test Deployed inference application](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/docs/source/test-model.md)

9. [Monitor your inference application deployed](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/docs/source/monitor-model.md)

NOTE: Each of the steps above can be repetaed if you are following ML lifecycle (e.g. changes in the dependencies, changes in the notebooks, new model stored).

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
* [Openshift][11]
* [ArgoCD][12]

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
[11]: https://www.openshift.com/
[12]: https://argoproj.github.io/argo-cd/
