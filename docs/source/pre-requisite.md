# Pre-requisites

In this section, the user can find the requirements that should be available before starting the tutorial.

## Login

### Operate First Login

Using [Operate First][1] you just need:

- Gmail account required to login to [JupyterHub][2].

### Other environments Login

For other environment you might receive Openshift credentials.

## GitHub account

The project is based on GitHub, if you don't have one just following this [link](https://docs.github.com/en/github/getting-started-with-github/signing-up-for-a-new-github-account).

## GitHub token

If you don't have a GitHub token, you can create one following GitHub docs: [create GitHub token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).

## Namespace for deployment

### Operate First namespace for deployment

Using [Operate First][1] you can `request access to a namespace` where you want to deploy your application using this [link](https://github.com/operate-first/support/issues/new?assignees=&labels=onboarding&template=onboarding_to_cluster.md&title=).

### Other environments namespace for deployment

If you have a different environment, you usually receive one by default or you need to ask admins to create a namespace for you.

## Cloud object storage

### Operate First Cloud object storage

Using [Operate First][1] you can `request a new bucket` once you get a namespace. In order to do that, use the following [link](https://github.com/operate-first/support/issues/new?assignees=&labels=user-support&template=ceph_bucket_request.md&title=).

Once you created a new bucket in your namespace, you can login in the cluster using the following [link](https://console-openshift-console.apps.cnv.massopen.cloud/k8s/cluster/projects) and in your namespace you will find:

- `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`in a Secret Object with the bucket name you crated.

- `OBJECT_STORAGE_ENDPOINT_URL`, `OBJECT_STORAGE_BUCKET_NAME` in a ConfigMap Object with the bucket name you crated.

### Other Cloud object storages

You can use your own bucket credentials, setting them as env variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.
You also need to have `OBJECT_STORAGE_ENDPOINT_URL`, `OBJECT_STORAGE_BUCKET_NAME`.

## Kubeflow Pipeline endpoint

### Operate First KFP endpoint

For [Operate First][1] you can find the Kubeflow Pipeline UI at this [link](http://ml-pipeline-ui-kubeflow.apps.cnv.massopen.cloud/#/pipelines).

## References

* [Operate First][1]
* [JupyterHub][2]

[1]: https://www.operate-first.cloud/
[2]: https://jupyter.org/hub
