# Setup initial environment

## 1. Fork this repo from GitHub into your account

Check [Fork a repo](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo) from GitHub docs.

In this tutorial we rely on [project-template][1], as described above, in order to have a common structures that can be easily used by data scientists and devops. Have a structure for the projects in general allows others to find all the bits required for the ML lifecycle and from the DevOps lifecycle.

If you want to use this template for your AI project, go to [project-template][1] and select `use the template` from the button provided in template repositories.

<div style="text-align:center">
<img alt="AI Project Template" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/AIProjectTemplate.png">
</div>

## 2. Access JupyterHub and spawn the Elyra image

### Operate First access JupyterHub

1. You can get access [JupyterHub][3] on [Operate First][2] using the following [link](https://jupyterhub-opf-jupyterhub.apps.cnv.massopen.cloud/)

<div style="text-align:center">
<img alt="Jupyter Hub UI" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/JupyterHubUI.png">
</div>

2. Select Elyra image called `ml-prague-workshop:latest` from the list of images.

3. Select `Large` for container size.

4. Insert the environment variables required using add button in JupyterLab UI:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`.
- `OBJECT_STORAGE_ENDPOINT_URL`
- `OBJECT_STORAGE_BUCKET_NAME`.

## 3. Clone your repo using Jupyterlab Git Extension

Once your image is ready and you are in the Jupyterlab UI, you can use the Git extension provided to clone [this repo](https://github.com/thoth-station/elyra-aidevsecops-tutorial.git).

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

* [project-template][1]
* [Operate First][2]
* [JupyterHub][3]

[1]: https://github.com/aicoe-aiops/project-template
[2]: https://www.operate-first.cloud/
[3]: https://jupyter.org/hub
