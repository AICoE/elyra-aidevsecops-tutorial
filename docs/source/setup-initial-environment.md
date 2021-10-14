# Setup initial environment

In this tutorial we rely on a [project template][1] in order to have a common structure that can be easily used by data scientists and devops engineers. Having structure in a project ensures all the pieces required for the ML and DevOps lifecycles are present and easily discoverable.

If you want to use this template for your AI project, go to the project template [here][1] and click the `Use the template` button provided in the repository.

<div style="text-align:center">
<img alt="AI Project Template" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/AIProjectTemplate.png">
</div>

## 1. Fork this repo from GitHub into your account

To begin, you'll need to fork this repository to create your own copy. If you're unsure how, look at [Fork a Repo](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) from GitHub docs.

## 2. Access the Elyra image in JupyterHub

### Access JupyterHub set up by Project Meteor

If you are viewing this tutorial in the Jupyter Book rendered by [Project Meteor][2], you can simply hover over the rocket icon on the top right of the page, and click on the `JupyterHub` option. This will take you to a JupyterLab environment spawned with the Elyra AIDevSecOps Tutorial image. Alternatively, you can also access this environment by clicking the `JupyterHub` button on the spawning page of the Meteor web application.
Moreover, using Meteor, the URL of your GitHub repo already add your repo to [JupyterLab Git](https://github.com/jupyterlab/jupyterlab-git) extension. Therefore that repo is already synced and managed by the extension.

### Access JupyterHub set up by Operate First

If you're viewing this tutorial outside of the Jupyter Book rendered by Project Meteor, you can instead access the [JupyterHub][3] deployed on the [Operate First][4] cluster.

1. Click this [link](https://jupyterhub-opf-jupyterhub.apps.smaug.na.operate-first.cloud/) to visit the Operate First JupyterHub.

    <div style="text-align:center">
    <img alt="Jupyter Hub UI" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/JupyterHubNewUI.png">
    </div>

2. Select the image called `AICoE Elyra AIDevSecOps Tutorial Notebook Image`.

3. Select `Large` for container size.

4. Insert the environment variables required using the add button in JupyterLab UI:

    - `AWS_ACCESS_KEY_ID`
    - `AWS_SECRET_ACCESS_KEY`
    - `OBJECT_STORAGE_ENDPOINT_URL`
    - `OBJECT_STORAGE_BUCKET_NAME`

## 3. Clone your repo using Jupyterlab Git Extension

Once your image is ready and you are in the Jupyterlab UI, you can use the Git extension provided to clone this repo.

1. Click the Git extension button from Jupyterlab UI:

    <div style="text-align:center">
    <img alt="Look for Git extension button" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/ElyraGitExtension.png">
    </div>

2. Take HTTPS link of the GitHub repo you want to clone, for this tutorial use your forked one from this repo:

    <div style="text-align:center">
    <img alt="Take link from forked repo" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/TakeLinkForkedRepo.png">
    </div>

3. Insert the link taken from your forked repo in the JupyterLab Git Extension: e.g. `https://github.com/thoth-station/elyra-aidevsecops-tutorial.git`

    <div style="text-align:center">
    <img alt="Clone your repo" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/CloneYourRepo.png">
    </div>

## Next Step

[Explore notebooks and manage dependencies](./explore-notebooks-and-manage-dependencies.md)

## References

* [Project template][1]
* [Project Meteor][2]
* [JupyterHub][3]
* [Operate First][4]

[1]: https://github.com/aicoe-aiops/project-template
[2]: https://github.com/AICoE/meteor
[3]: https://jupyter.org/hub
[4]: https://www.operate-first.cloud/
