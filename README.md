# Elyra AIDevSecOps Tutorial

As a Data Scientist on a rhel8 workstation, I want to run a toolbox container image, so that I can start developing notebooks with Elyra locally.

## AIDevSecOps

Data Scientists are not so different from developers and DevSecOps practices can be applied to MLOps ones. (AIDevSecOps).

Developers (Data Scienstist included) can rely on AI for support on their daily work.

Project Thoth [1] develops tools that can enhance developers work, reducing their workload on mundane tasks that can be automatically handlded by bots.
This tutorial show one example of how AI (Project Thoth) can support AIDevSecOps and it will be focused on the use of an AI centric tool called Elyra,
JupyterLab extensions to handle notebooks and Python scripts, backed by AI pipelines.

For the purpose of this tutorial we focus on local use of Elyra.

More information about `Project Thoth <https://thoth-station.ninja/>`__.

More information about `Elyra <https://github.com/elyra-ai/elyra>`__.

## Preliminary steps

### Create your toolbox container

```shell
[user@hostname ~]$ toolbox create --image quay.io/thoth-station/thoth-toolbox:v0.5.4
Created container: thoth-toolbox-v0.5.4
Enter with: toolbox enter --container thoth-toolbox-v0.5.4
[user@hostname ~]$
```

This will create a container called `thoth-toolbox-<version-id>`.

More information about `Thoth toolbox container <https://github.com/thoth-station/thoth-toolbox>`__.

### Enter the toolbox

```shell
[user@hostname ~]$ toolbox enter --container thoth-toolbox-v0.5.4
⬢[user@toolbox ~]$
```

### Install podman

[user@hostname ~]$ sudo dnf install -y podman

### Start Elyra to work on your AI project

```shell
[user@hostname ~]$ podman run -p 8080:8080 quay.io/thoth-station/s2i-lab-elyra:v0.0.4  start-singleuser.sh --ip="0.0.0.0" --port=8080 --debug
```

## Start AI project

### Step 1: Download your data with a Python script

### Step 2: Process your data in a Jupyter notebook

### Step 3: Train the model in a Jupyter notebook

### Step 4: Create and run your AI pipeline

## GitOps, reproducibility, shareability and traceability with AI support

Nowadays, developers (including Data Scientists) use Git and GitOps practices to store, share all notebooks, sources on development platforms (e.g. GitHub).
GitOps best practices help reproducibility and traecability for all projects avaialble. One of the most important requirement for reproducibility is dependencies management.

Having dependencies clearly stated allow for reusability and portability of notebooks, which can be reused in another projects.

Project Thoth [1] helps developers keep these depencies up to date, moreover improve developers work creating software stacks for their project that satisfies developers requirements.
These requirments might across the AIDevSecOps lifecycle of a project, therefore the software stack requirements can change as well.

For the purpose of this tutorial the type of recommendation requested is: performance. See `.thoth.yaml file <https://github.com/aicoe-aiops/project-template>`__.

The project template is based on [2].

## References

- [1] `Project Thoth <https://thoth-station.ninja/>`__.

- [2] `Enhanced cookiecutter data science project template <https://github.com/aicoe-aiops/project-template>`__.
