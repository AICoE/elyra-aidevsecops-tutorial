
# Elyra AIDevSecOps Tutorial

This tutorial is used to discuss the interface between data science and DevOps using project templates, pipelines and bots. It looks to highlight that data scientists are not so different from developers, and many MLOps practices and tools can be enhanced by DevSecOps techniques.

The demo application used is the "hello world" for AI: MNIST Classification.

## Environment required

This tutorial has the following environment requirements to be run. If you're running on Project Meteor which uses the Operate First environment, the environment requirements are already setup for you (see note below).

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

[Operate First][2] is an open infrastructure environment started at Red Hat's Office of the CTO. It has been selected to run this tutorial since it is an open source initiative that fulfills all the requirements stated above. Anyone with a Google account can log in and start developing. To learn more about Operate First, visit the [website](https://www.operate-first.cloud/) or [GitHub community](https://github.com/operate-first).


## Tools

In this tutorial the following technologies are going to be used:

- [JupyterHub][4] to launch images with Jupyter tooling
- [Elyra][5] supplies a set of extensions to JupyterLab notebooks to support AI projects
- [Project Thoth][6] extension for dependency management on JupyterLab
- [Kubeflow Pipelines][9] for end to end experiments using pipelines

## GitOps for reproducibility, portability, traceability with AI support

Nowadays, developers (including data scientists) use Git and GitOps practices to store and share code on development platforms such as GitHub. GitOps best practices allow for reproducibility and traceability in projects.

One of the most important requirements for reproducibility is dependency management. Having dependencies clearly stated allows portability of notebooks, so they can be shared safely with others and reused in other projects.

If you want to know more about this issue in the data science domain, have a look at this [article](https://developers.redhat.com/blog/2021/03/19/managing-python-dependencies-with-the-thoth-jupyterlab-extension/) or this [video](https://www.youtube.com/watch?v=ifyQ2oSxjnU).

[Project Thoth][6] keeps dependencies up to date by giving recommendations for a developer's daily tools. Thanks to this tooling, developers (including data scientists) do not have to worry about managing the dependencies after they are selected, since conflicts can be handled by Thoth bots and automated pipelines. Having this AI support can benefit AI projects, offering improvements such as performance improvements due to optimized dependencies and additional security since insecure libraries cannot be introduced. If you want to know more, have a look at this [repo](https://github.com/thoth-station/jupyterlab-requirements) or Thoth's [website](https://thoth-station.ninja/docs/developers/adviser/integration.html).

## Automated pipelines and bots for your GitHub project

- [Kebechet Bot][7] to keep your dependencies fresh and up to date receiving recommendations and justifications using AI.

- [AICoE Pipeline][8] to support your AI project lifecycle.

All these tools are integrated with the [project template][1], so most additions are already set for you.
These bots and pipelines exist to automate many of the manual GitOps tasks. For example, in order to deploy your application, you may need to create a container image. GitHub templates integrated with bots can provide you with automated pipelines triggered depending on what you need (e.g. release (patch, minor, major), deliver a container image, or update your dependencies).

## Project templates

The project template used can be found here: [project template][1]. It shows correlation between data scientist needs (e.g. data, notebooks, models) and AI DevOps engineers ones (e.g. manifests). Having structure in a project ensures all the pieces required for the ML and DevOps lifecycles are present and easily discoverable.

# Tutorial Steps

0. [Pre-requisities](./docs/source/pre-requisite.md)

## ML Lifecycle/Source Lifecycle

1. [Setup your initial environment](./docs/source/setup-initial-environment.md)

2. [Explore notebooks and manage dependencies](./docs/source/explore-notebooks-and-manage-dependencies.md)

3. [Push changes to GitHub](./docs/source/push-changes.md)

4. [Create release, build image or overlays builds for different images](./docs/source/build-images.md)

    * [Benefit from bots to keep your dependencies fresh and up to date](./docs/source/use-bots.md)

5. [Create an AI Pipeline](./docs/source/create-ai-pipeline.md)

6. [Run and debug AI Pipeline](./docs/source/run-ai-pipeline.md)

## DevOps Lifecycle

7. [Deploy Inference Application](./docs/source/deploy-model.md)

8. [Test Deployed inference application](./docs/source/test-model.md)

9. [Monitor your inference application deployed](./docs/source/monitor-model.md)

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
