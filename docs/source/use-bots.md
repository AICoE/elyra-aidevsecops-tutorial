# Dependencies updates in the repo

If you want to manage your project dependency updates automatically, you can install and set up the [Kebechet bot][1] in your repo. Kebechet regularly checks if your project is using the optimal set of dependencies in terms of  CVE vulnerabilities, newer package releases, and performance changes. If it finds that the dependencies can be updated, it automatically opens a PR on your repo to make the required updates!

An example of the Kebechet bot in action can be seen below.

<div style="text-align:center">
<img alt="Kebechet Automatic Update" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/KebechetAutomaticUpdate.png">
</div>

To learn more about Thoth bots and services, please check out the guide [here][2].

## Next Step

[Create an AI Pipeline](./create-ai-pipeline.md)

## References

* [Kebechet][1]
* [Bots and CI Services Setup Instructions][2]

[1]: https://github.com/thoth-station/kebechet
[2]: https://github.com/AICoE/aicoe-ci/blob/master/docs/thoth-bots-setup.md#instructions-to-setup-bots-and-ci-services
