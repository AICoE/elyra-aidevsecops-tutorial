# Create a first release and image of your project

The following sub-sections of step 6 can be performed only if you have set your project with your pipelines.
In order to do that you can followin these instructions: [Setting AICoE CI and Thoth on your repo](https://github.com/AICoE/aicoe-ci#setting-aicoe-ci-on-github-organizationrepository).

For the purpose of the tutorial the images required are already created using these pipelines, therefore here you can find a description on how they have been created and where they are available.

## Ask for new release

Using pipelines like the AICoE tooling you can rely on bots helping you, as described above in the initial description.
These pipelines are described in [AICoE Pipeline][1] and you can use them for you projects if you are interested.

In this case the [.aicoe.yaml](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/.aicoe-ci.yaml) is created with all information relative to build (e.g. base image, build strategy, registry where to push) as described in [AICoE Pipeline][1] documentation.

Some of the pipelines used in Thoth project are maintained by bots. Therefore you can open an issue asking for release (e.g patch, minor, major) and the bots will handle your request. One the request will be completed the bot will automatically close the issue as you can see from the images below:

<div style="text-align:center">
<img alt="Open Issue Release" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/OpenIssueRelease.png">
</div>

<div style="text-align:center">
<img alt="Pull Request Release" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/PullRequestRelease.png">
</div>

The `CHANGELOG` after the release is created using AI model that cluster pull requests. You can find more information about `glyph project` [here](https://github.com/thoth-station/glyph).

Once the issue is closed by the bot, a tag is created in the GitHub project and a pipeline starts in order to build and push the image on the registry according to the requirements inserted in the [.aicoe.yaml](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/.aicoe-ci.yaml).

Once the new tag is created, Tekton pipelines from the AICoE are triggered.

## Image available on quay

Once the image has been created by the Tekton pipeline, you can find it in your registry (e.g. Quay):

<div style="text-align:center">
<img alt="Image on Registry" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/ImageRegistry.png">
</div>

## Use of Overlays

If you have overlays directory present, as for this tutorial, you can perform overlays builds thanks to the [AICoE Pipeline][1]. In this way you can create different images optimized for your steps in pipelines. In this case the AICoE tooling would create many images as number of overlays, as you can see from the following images:

<div style="text-align:center">
<img alt="Image on Registry" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/TagReleasePipeline.png">
</div>

<div style="text-align:center">
<img alt="Image on Registry" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/OverlaysBuildsPipeline.png">
</div>

Once the pipelines are completed the images will be available on quay.

You can find the images required for tutorial named after the overlays requested:

- [download-dataset overlay](https://github.com/thoth-station/elyra-aidevsecops-tutorial/tree/master/overlays/download-dataset) -> quay.io/thoth-station/elyra-aidevsecops-dataset:v0.5.0 (download-dataset image)

- [training overlay](https://github.com/thoth-station/elyra-aidevsecops-tutorial/tree/master/overlays/training) -> quay.io/thoth-station/elyra-aidevsecops-training:v0.5.0 (training image)

- [inference overlay](https://github.com/thoth-station/elyra-aidevsecops-tutorial/tree/master/overlays/inference)  -> quay.io/thoth-station/elyra-aidevsecops-tutorial:v0.5.0 (inference image)

You can check the overlays build requirement in the [.aicoe.yaml](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/c86ce9c08665c12df0adf829db31bd19e8c61455/.aicoe-ci.yaml#L5).

All requirements for the overlay are created using Thoth resolution engine, you can find the inputs used for Thoth recommender in the [.thoth.yaml](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/bb6fad2441e8df8aa56c2c0e6b5ac45a2cda42eb/.thoth.yaml#L5).

## References

* [AICoE Pipeline][1]

[1]: https://github.com/AICoE/aicoe-ci