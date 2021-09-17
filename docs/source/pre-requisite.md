# Pre-requisites

| Requirement | Notes | 
| --- | --- |
| GitHub account |
 The project is based on GitHub, if you don't have one just following this [link](https://docs.github.com/en/github/getting-started-with-github/signing-up-for-a-new-github-account). |
| GitHub token |
 If you don't have a GitHub token, you can create one following GitHub docs: [create GitHub token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token). |
| [Red Hat Openshift][1] |
 Using [Operate First][2] you can find a deployed [Red Hat Openshift][1] available to [Operate First][2] community |
| [Open Data Hub][3] |
 Using [Operate First][2] you can find a community supported [Open Data Hub][3] with all tools for Data Science (e.g. [JupyterHub][4], [Elyra][5], [Kubeflow Pipelines][6], [Seldon][7], [Prometheus][8], [Grafana][9], [Superset][10]) running on [Red Hat Openshift][1] |
| Kuberneetes namespace |
 Using [Operate First][2] you can `request access to a namespace` where you want to deploy your application using this [link](https://github.com/operate-first/support/issues/new?assignees=first-operator&labels=kind%2Fonboarding%2Carea%2Fcluster&template=onboarding_to_cluster.yaml&title=NEW+PROJECT%3A+%3Cname%3E). If you have a different environment, you usually receive one by default or you need to ask admins to create a namespace for you. |
| Cloud object storage | Using [Operate First][2] you can `request a new bucket` once you get a namespace. In order to do that, use the following [link](https://github.com/operate-first/support/issues/new?assignees=first-operator&labels=kind%2Fonboarding%2Carea%2Fbucket&template=ceph_bucket_request.yaml&title=BUCKET%3A+%3Cname%3E).

Once you created a new bucket in your namespace, you can login in the cluster using the following [link](https://console-openshift-console.apps.zero.massopen.cloud/k8s/cluster/projects) and in your namespace you will find:

- `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in a Secret Object with the bucket name you created.

- `OBJECT_STORAGE_ENDPOINT_URL`, `OBJECT_STORAGE_BUCKET_NAME` in a ConfigMap Object with the bucket name you created.

NOTE: _You can also use your own bucket credentials and/or other registries accessible publicly. You will need the environment variables `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `OBJECT_STORAGE_ENDPOINT_URL`, and `OBJECT_STORAGE_BUCKET_NAME`._ |
| JupyterLab environment with [jupyterlab-requirements][11] library and [Elyra][5] |
 Using [Operate First][1], you can login in [JupyterHub][4] with your GitHub Account and you can spawn the image called `Elyra AIDevSecOpsTutorial`. If you use [Meteor][12], it will build a [JupyterHub][4] environment for your project from the GitHub repository URL you provide to it. (e.g. [URL](https://github.com/pacospace/elyra-aidevsecops-tutorial)|
| [Kubeflow Pipeline][6] |
 Using [Operate First][2] you will find [Kubeflow Pipeline][6] deployed and ready for use with [Elyra][5]. You can find the Kubeflow Pipeline UI at this [link](http://istio-ingressgateway-istio-system.apps.zero.massopen.cloud/_/pipeline/#/pipelines). |


## Next Step

[Setup your initial environment](./setup-initial-environment.md)

## References

* [Red Hat Openshift][1]
* [Operate First][2]
* [Open Data Hub][3]
* [JupyterHub][4]
* [Elyra][5]
* [Kubeflow Pipelines][6]
* [Seldon][7]
* [Prometheus][8]
* [Grafana][9]
* [Superset][10]
* [jupyterlab-requirements][11]
* [Meteor][12]

[1]: https://www.openshift.com/
[2]: https://www.operate-first.cloud/
[3]: https://opendatahub.io/
[4]: https://jupyter.org/hub
[5]: https://github.com/elyra-ai/elyra
[6]: https://www.kubeflow.org/docs/pipelines/overview/pipelines-overview/
[7]: https://www.seldon.io/
[8]: https://prometheus.io/
[9]: https://grafana.com/
[10]: https://superset.apache.org/
[11]: https://github.com/thoth-station/jupyterlab-requirements
[12]: https://github.com/AICoE/meteor

