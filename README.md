
# Elyra AIDevSecOps Tutorial

As a Data Scientist on a rhel8 workstation, I want to run a toolbox container image, so that I can start developing notebooks with Elyra locally.

## AIDevSecOps

Data Scientists are not so different from developers and DevSecOps practices can be applied to MLOps ones. (AIDevSecOps).

Developers (Data Scienstist included) can rely on AI for support on their daily work.

[Project Thoth][1] develops tools that can enhance developers work, reducing their workload on mundane tasks that can be automatically handlded by bots.
This tutorial show one example of how AI ([Project Thoth][1]) can support AIDevSecOps and it will be focused on the use of an AI centric tool called [Elyra][2],
JupyterLab extensions to handle notebooks and Python scripts, backed by AI pipelines.

For the purpose of this tutorial we focus on local use of [Elyra][2].

## Preliminary steps

### Create your toolbox container

```shell
  toolbox create --image quay.io/thoth-station/thoth-toolbox:v0.5.4
```

This will create a container called `thoth-toolbox-<version-id>`.

More information about [Thoth toolbox container](https://github.com/thoth-station/thoth-toolbox).

### Enter the toolbox

```shell
  toolbox enter --container thoth-toolbox-v0.5.4
```

### Install podman

```shell
  sudo dnf install -y podman
```

### Start Elyra to work on your AI project

```shell
  podman run -p 8080:8080 quay.io/thoth-station/s2i-lab-elyra:v0.0.4  start-singleuser.sh --ip="0.0.0.0" --port=8080 --debug
```

## Start AI project

1. Download your data with a [Python script](https://github.com/thoth-station/elyra-aidevsecops-tutorial/src/data/download_dataset_from_tf.py) or [Jupyter notebook](https://github.com/thoth-station/elyra-aidevsecops-tutorial/notebooks/download_dataset.ipynb);

2. Train the model in a [Jupyter notebook](https://github.com/thoth-station/elyra-aidevsecops-tutorial/notebooks/training.ipynb) and store model locally;

3. Create and run your [AI pipeline](https://github.com/thoth-station/elyra-aidevsecops-tutorial/tutorial.pipeline) on Elyra to retrain your model automatically using step 1. and 2.;

4. Create your [application](https://github.com/thoth-station/elyra-aidevsecops-tutorial/wsgi.py) to expose endpoints (e.g /predict and /metrics).

5. Deploy your application.

## Test endpoints locally

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

## GitOps, reproducibility, portability and traceability with AI support

Nowadays, developers (including Data Scientists) use Git and GitOps practices to store, share all notebooks, sources on development platforms (e.g. GitHub).
GitOps best practices help reproducibility and traecability for all projects avaialble. One of the most important requirement for reproducibility is dependencies management.

Having dependencies clearly stated allow for reusability and portability of notebooks, which can be reused in another projects.

[Project Thoth][1] helps developers keep these depencies up to date, moreover improve developers work creating software stacks for their project that satisfies developers requirements.
These requirments might across the AIDevSecOps lifecycle of a project, therefore the software stack requirements can change as well.

For the purpose of this tutorial the type of recommendation requested is: performance. See [.thoth.yaml file](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/.thoth.yaml).

The project template used can be found here: [project-template][3] which show correlation between data scientists requirements and AI dev ops engineers ones.

## References

 * [Project Thoth][1]
 * [Elyra][2]
 * [project-template][3]

[1]: https://thoth-station.ninja/
[2]: https://github.com/elyra-ai/elyra
[3]: https://github.com/aicoe-aiops/project-template
