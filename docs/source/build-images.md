# Create a first release and image of your project

This document describes how the [AICoE CI][1] and Thoth pipelines can be used to create the images, and where you can find the images for this project. For the purpose of this tutorial, the required images have already been created using these pipelines.

Please note that in order to execute the steps below for your own repo, you will first need to configure your repo to use AICoE CI and Thoth. To do that, you can follow the instructions [here][2].

## Ask for new release

Some of the pipelines used in Thoth project are maintained by bots. Therefore you can simply open an issue asking for a release (e.g patch, minor, major) and the bots will handle your request. Once the request is completed, the bot will also automatically close the issue, as you can see from the images below:

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
