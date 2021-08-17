# Dependencies updates in the repo

If you want to manage your project dependency updates automatically, you can install and set up the [Kebechet bot][1] in your repo. Kebechet regularly checks if your project is using the optimal set of dependencies in terms of  CVE vulnerabilities, newer package releases, and performance changes. If it finds that the dependencies can be updated, it automatically opens a PR on your repo to make the required updates!

An example of the Kebechet bot in action can be seen below.

<div style="text-align:center">
<img alt="Kebechet Automatic Update" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/KebechetAutomaticUpdate.png">
</div>

## Set up Thoth bots on your fork

Adding Thoth's bots takes just a few steps! Start by installing the Kebechet GitHub application by [following this link](https://github.com/apps/khebhut). It can be configured on an organization or on a single repository. To test out the Kebechet bot in this tutorial, select your profile for the organization, and specify the `elyra-aidevsecops-tutorial` as the repository.

Once the application is installed, you will need to add Thoth's bots as collaborators. Navigate to your fork of `elyra-aidevsecops-tutorial`. Under the repository's **Settings**, go to **Manage Access** and click on "Invite a collaborator" and add Sesheta. Sesheta is a friendly Thoth bot who is used to help automate tasks. You might have already done this step when [building an image](build-images.md), in which case you do not have to invite Sesheta again. Please note: there is sometimes a delay in Sesheta's invite acceptance. Please note: Sesheta does not accept invites instantaneously and automatically (see [this issue](https://github.com/AICoE/aicoe-ci/issues/126) for more details). [Follow this link](https://github.com/AICoE/aicoe-ci/issues/new?assignees=goern%2Charshad16&labels=area%2Fcyborgs%2Cbot%2Csig%2Fcyborgs&template=request_sesheta.yaml&title=Help+with+Sesheta+invite) and fill out the form to have Sesheta accept your invitation.

<div style="text-align:center">
<img alt="Invite Sesheta" src="https://raw.githubusercontent.com/aicoe/elyra-aidevsecops-tutorial/master/docs/images/InviteSesheta.png">
</div>

Kebechet requires a configuration file ([.thoth.yaml](../../.thoth.yaml)) at the root level of the project. In this tutorial, the file is already present, so you will not need to add it. To configure this on your own fork, you will need to update the managers section to include your GitHub username. An example snippet of `.thoth.yaml` highlightling the changes to be made is shown below.

      ```yaml
      managers:
        - name: pipfile-requirements
        - name: update
          configuration:
            labels: [bot]
        - name: info
        - name: version
          configuration:
            maintainers:
              - goern   # UPDATE TO HAVE YOUR OWN USERNAME
              - fridex
            assignees:
              - sesheta
            labels: [bot]
            changelog_file: true
      ```

To learn more about Thoth bots and services, please check out the guide [here][2].

## Next Step

[Create an AI Pipeline](./create-ai-pipeline.md)

## References

* [Kebechet][1]
* [Bots and CI Services Setup Instructions][2]

[1]: https://github.com/thoth-station/kebechet
[2]: https://github.com/AICoE/aicoe-ci/blob/master/docs/thoth-bots-setup.md#instructions-to-setup-bots-and-ci-services
