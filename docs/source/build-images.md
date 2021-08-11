# Create a first release and image of your project

This document describes how the [AICoE CI][1] and [Thoth](https://github.com/thoth-station) pipelines can be used to create the images for this project. **For the purpose of this tutorial, we have created the required images of the upstream repo. No action is required.** If you want to build these resources from your own fork, use the following instructions for image builds.

## Set up AICoE CI and Thoth bots on your fork

You will first need to configure your repo to use AICoE CI and Thoth. The [AICoE-CI tooling](https://github.com/AICoE/aicoe-ci) can be set up in just a few steps. Start by installing the AICoE CI GitHub application by [following this link](https://github.com/apps/aicoe-ci). When installing this application, select your profile for the organization, and specify the `elyra-aidevsecops-tutorial` as the repository.

### Invite Sesheta

Once the application is installed, you will need to add Thoth's bots as collaborators. Navigate to your fork of `elyra-aidevsecops-tutorial`. Under the repository's **Settings**, go to **Manage Access** and click on "Invite a collaborator" and add Sesheta. Sesheta is a friendly Thoth bot who is used to help automate tasks. Please note: Sesheta's invite acceptance is not instantaneous. [Follow this link](https://github.com/AICoE/aicoe-ci/issues/new?assignees=goern%2Charshad16&labels=area%2Fcyborgs%2Cbot%2Csig%2Fcyborgs&template=request_sesheta.yaml&title=Help+with+Sesheta+invite) and fill out the form to have Sesheta accept your invitation.

<div style="text-align:center">
<img alt="Invite Sesheta" src="https://raw.githubusercontent.com/aicoe/elyra-aidevsecops-tutorial/master/docs/images/InviteSesheta.png">
</div>

### Enable issues on your fork

Sesheta, the bot that will assist you in this tutorial, communicates through issues. On your fork, the issues tab may not be enabled automatically. In order to enable issues, go to the **Settings** tab and check the box next to "Issues".

<div style="text-align:center">
<img alt="Enable Fork Issues" src="https://raw.githubusercontent.com/aicoe/elyra-aidevsecops-tutorial/master/docs/images/EnableForkIssues.png">
</div>

### Set up robot account in Quay

The next step involves setting up a robot account on the image registry [Quay.io](https://quay.io/) and requires the user to have a Quay account.

First, you will need to create a robot in the organization or individual account. Under **Account Settings** on Quay, click on **Robot Accounts** tab, and "Create Robot Account" button. Enter a name for the account. The username will become namespace+accountname where namespace is the name of the user or organization.

<div style="text-align:center">
<img alt="Create Robot Account" src="https://raw.githubusercontent.com/AICoE/aicoe-ci/master/docs/quay-robots.png">
</div>

Once created, click on the robot account name. Find the "Kubernetes Secret" secret tab in the robot account popup, and copy the secret. [Open an issue](https://github.com/AICoE/aicoe-ci/issues/new/choose) including your Kubernetes secret requesting for it to be configured. Once the secret is passed, it is ready to be used in the `.aicoe-ci.yaml` file in the next step.

### Edit up `.aicoe-ci.yaml`

The last step is to add the [aicoe-ci configuration file](https://github.com/AICoE/aicoe-ci#aicoe-ci-configuration-file). Configuration files allows user assign details about the build requirements and specify base image and registry details for build and push. For the purpose of this tutorial, the [.aicoe-ci.yaml](../../.aicoe-ci.yaml) file is already present. However, you may need to edit some of the fields for your personal access, namely `registry-org`, `registry-project`, and `registry-secret`.

```yaml
build:
  build-stratergy: Dockerfile # Allowed values: Source, Dockerfile, Containerfile
  base-image: registry.access.redhat.com/ubi8/ubi:latest
  dockerfile-path: Dockerfile
  registry: quay.io # Image registry to be used. (default: quay.io)
  registry-org: thoth-station # Organization in Image Registry. (default: thoth-station)
  registry-project: example # project repository in Image Registry (ie, Quay) used to push image.
  registry-secret: thoth-station-thoth-pusher-secret # comes from robot account
```

For more detailed information on the config file and robot accounts, visit the [AICoE CI documentation](https://github.com/AICoE/aicoe-ci#configuring-build-requirements).

## Ask for new release

Some of the pipelines used in the Thoth project are maintained by bots. Therefore you can simply open an issue asking for a release (e.g patch, minor, major) and the bots will handle your request. Once the request is completed, the bot will also automatically close the issue, as you can see from the images below:

<div style="text-align:center">
<img alt="Open Issue Release" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/OpenIssueRelease.png">
</div>

<div style="text-align:center">
<img alt="Pull Request Release" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/PullRequestRelease.png">
</div>

Fun fact, the `CHANGELOG` in the release is also created using an AI model that clusters pull requests. You can find more information about this model in our [glyph][3] project.

Once the issue is closed by the bot, a new tag is created in the GitHub repo. This in turn triggers the Tekton pipelines in AICoE CI to start the build process and push the image on the registry according to the configuration defined in the [.aicoe-ci.yaml](../../.aicoe-ci.yaml).

In this case, the [.aicoe-ci.yaml](../../.aicoe-ci.yaml) has been populated with all information (e.g. base image, build strategy, registry where to push) related to building the image for the Elyra AIDevSecOps tutorial. To learn more about the configuration options available for the `.aicoe-ci.yaml`, please check out the [AICoE CI][1] documentation.

## Image available on quay

Once the image has been created by the Tekton pipelines, you can find it in your registry (e.g. Quay):

<div style="text-align:center">
<img alt="Image on Registry" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/ImageRegistry.png">
</div>

## Use of Overlays

If you have an `overlays` directory present in your repo, like this tutorial does, you can perform overlays builds using the [AICoE Pipeline][1]. This allows you to create different images optimized for the different steps in your AI pipeline. To see how the overlays build requirement can be set up, please check out the [.aicoe.yaml](../../.aicoe-ci.yaml#L5) config file in this project. Based on this configuration, the AICoE tooling would create as many images as the number of overlays, as you can see from the following images:

<div style="text-align:center">
<img alt="Image on Registry" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/TagReleasePipeline.png">
</div>

<div style="text-align:center">
<img alt="Image on Registry" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/OverlaysBuildsPipeline.png">
</div>

Note that all the requirements for the overlay are created using the Thoth resolution engine. You can find the inputs used for Thoth recommender in the [.thoth.yaml](../../.thoth.yaml#L5) config file.

Once the pipelines have finished execution, the images will be available on quay. You can find the images built for this tutorial at the links provided below. Note that these images have been named according to the overlays requested.

- [download-dataset overlay](../../overlays/download-dataset) -> quay.io/thoth-station/elyra-aidevsecops-dataset:v0.11.0 (download-dataset image)

- [training overlay](../../overlays/training/Pipfile) -> quay.io/thoth-station/elyra-aidevsecops-training:v0.11.0 (training image)

- [inference overlay](../../overlays/inference/Pipfile)  -> quay.io/thoth-station/elyra-aidevsecops-tutorial:v0.11.0 (inference image)

## Next Steps

[Benefit from bots to keep your dependencies fresh and up to date](/docs/source/use-bots.md)

## References

* [AICoE CI Pipeline][1]
* [Setting AICoE CI on a GitHub repo/org][2]
* [Project Glyph][3]

[1]: https://github.com/AICoE/aicoe-ci
[2]: https://github.com/AICoE/aicoe-ci#setting-aicoe-ci-on-github-organizationrepository
[3]: https://github.com/thoth-station/glyph
