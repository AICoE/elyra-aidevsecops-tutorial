# Pre-requisites

In this section, the user can find the requirements needed for the tutorial:

- GitHub account
- GitHub token
- OpenShift Environment
- Namespace for deployment
- Cloud object storage

### GitHub account

The project is based on GitHub, if you don't have one just following this [link](https://docs.github.com/en/github/getting-started-with-github/signing-up-for-a-new-github-account).

### GitHub token

If you don't have a GitHub token, you can create one following GitHub docs: [create GitHub token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).

### OpenShift Environment

Using [Operate First][1] you just need a Google account to login to [JupyterHub][2]. Using Operate First is encouraged.
If you use a different environment, you will need to provide your own OpenShift credentials.

### Namespace for deployment

Using [Operate First][1] you can `request access to a namespace` where you want to deploy your application using this [link](https://github.com/operate-first/support/issues/new?assignees=&labels=onboarding&template=onboarding_to_cluster.md&title=).

If you have a different environment, you usually receive one by default or you need to ask admins to create a namespace for you.

### Cloud object storage

#### Operate First Cloud object storage

Using [Operate First][1] you can `request a new bucket` once you get a namespace. In order to do that, use the following [link](https://github.com/operate-first/support/issues/new?assignees=&labels=user-support&template=ceph_bucket_request.md&title=).

Once you created a new bucket in your namespace, you can login in the cluster using the following [link](https://console-openshift-console.apps.zero.massopen.cloud/k8s/cluster/projects) and in your namespace you will find:

- `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` in a Secret Object with the bucket name you created.

- `OBJECT_STORAGE_ENDPOINT_URL`, `OBJECT_STORAGE_BUCKET_NAME` in a ConfigMap Object with the bucket name you created.

#### Other Cloud object storages

You can also use your own bucket credentials. You will need the environment variables `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `OBJECT_STORAGE_ENDPOINT_URL`, and `OBJECT_STORAGE_BUCKET_NAME`.

### Kubeflow Pipeline endpoint

For [Operate First][1] you can find the Kubeflow Pipeline UI at this [link](http://istio-ingressgateway-istio-system.apps.zero.massopen.cloud/_/pipeline/#/pipelines).

## Next Step

[Setup your initial environment](./setup-initial-environment.md)

## References

* [Operate First][1]
* [JupyterHub][2]

[1]: https://www.operate-first.cloud/
[2]: https://jupyter.org/hub
