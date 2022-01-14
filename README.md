
# Elyra AIDevSecOps Tutorial

This tutorial is used to discuss the interface between Data Science and DevOps. It looks to highlight that data scientists are not so different from developers, therefore they need to know Git and follow best practices to maintain their dependencies and code, add tests and make release. All these tasks can be supported through pipelines and bots so that data scientists can focus on the main problem to solve. In other words in this tutorial you will learn how the ML lifecycle, practices and tools can be enhanced by DevSecOps techniques.


## What you will learn with this tutorial?

At the end of this tutorial you will be able to spawn images from [JupyterHub][1], manage dependencies for Jupyter Notebook using [Project Thoth][2] extension for dependency management on JupyterLab, learn about `overlays` concept, setup [AICoE CI][3] and [Kebechet Bot][4] to automate creation of images for overlays and maintenance of software stacks. Then you will learn how to create and run an [Elyra][5] AI pipeline with [Kubeflow Pipelines][6] using the images created. Finally, you will learn how to leverage [ArgoCD][7] and deploy AI model automatically.

The demo application selected for this tutorial is the `MNIST Classification`. The `MNIST Dataset` is described [here](http://yann.lecun.com/exdb/mnist/).
In this tutorial there are different variations:

- one using TensorFlow
- one using Pytorch and [Neural Magic](https://neuralmagic.com/) tools.


## Where you will run this tutorial?

[Operate First][8] is an open infrastructure environment started at Red Hat's Office of the CTO. It has been selected to run this tutorial since it is an open source initiative that fulfills all the requirements stated above. Anyone with a Google account can log in and start developing. To learn more about Operate First, visit the [website](https://www.operate-first.cloud/) or [GitHub community](https://github.com/operate-first).

[Operate First][8] hosts [Open Data Hub][9] with all the tools provided for Data Science projects (e.g. [JupyterHub][1], [Elyra][5], [Kubeflow Pipelines][6], [Seldon][10], [Prometheus][11], [Grafana][12], [Superset][13]) running on [Red Hat Openshift][14].


## Why does the tutorial repository have this structure?

The project template used can be found here: [project template][15]. It shows correlation between a data scientist needs (e.g. data, notebooks, models) and that of an AI DevOps engineer (e.g. manifests). Having structure in a project ensures all the pieces required for the ML and DevOps lifecycles are present and easily discoverable.


# Tutorial Steps

0. [Pre-requisities](./docs/source/pre-requisite.md)

## ML Lifecycle/Source Lifecycle

1. [Setup your initial environment](./docs/source/setup-initial-environment.md)

2. [Explore notebooks and manage dependencies](./docs/source/mnist-classification-application.md)

3. [Push changes to GitHub](./docs/source/push-changes.md)

4. [Setup bots and pipelines to create releases, build images and enable dependency management](./docs/source/thoth-aicoe-services.md)

5. [Create an AI Pipeline](./docs/source/create-ai-pipeline.md)

6. [Run and debug AI Pipeline](./docs/source/run-ai-pipeline.md)

## DevOps Lifecycle

7. [Deploy Inference Application](./docs/source/deploy-model.md)

8. [Test Deployed inference application](./docs/source/test-model.md)

9. [Monitor your inference application deployed](./docs/source/monitor-model.md)


## Workshops

Here you find a list of conferences where this tutorial has been used:

- [DevConf.US 2021](https://www.devconf.info/us/):
    - [presentation](./docs/presentations/ML-Prague-2021-Workshop.pdf)
    - [video](https://www.youtube.com/watch?v=s52dKDQEiZw&t=2s)

- [ML Prague 2021](https://www.mlprague.com/):
    - [presentation](./docs/presentations/ML-Prague-2021-Workshop.pdf)


## References

* [JupyterHub][1]
* [Project Thoth][2]
* [AICoE CI][3]
* [Kebechet Bot][4]
* [Elyra][5]
* [Kubeflow Pipelines][6]
* [ArgoCD][7]
* [Operate First][8]
* [Open Data Hub][9]
* [Seldon][10]
* [Prometheus][11]
* [Grafana][12]
* [Superset][13]
* [Red Hat Openshift][14]
* [project-template][15]

[1]: https://jupyter.org/hub
[2]: https://thoth-station.ninja/
[3]: https://github.com/AICoE/aicoe-ci
[4]: https://github.com/marketplace/khebhut
[5]: https://github.com/elyra-ai/elyra
[6]: https://www.kubeflow.org/docs/pipelines/overview/pipelines-overview/
[7]: https://argoproj.github.io/argo-cd/
[8]: https://www.operate-first.cloud/
[9]: https://opendatahub.io/
[10]: https://www.seldon.io/
[11]: https://prometheus.io/
[12]: https://grafana.com/
[13]: https://superset.apache.org/
[14]: https://www.openshift.com/
[15]: https://github.com/aicoe-aiops/project-template
