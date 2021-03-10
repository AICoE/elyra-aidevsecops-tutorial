# Deploy your model

There are different ways to deploy a model and different tools that can be used for that (e.g. Seldon, Tf-Serving, TensorRT), but for this tutorial we created a simple Flask application that can be easily deployed.

## Create Flask application

Once you trained your model and it is stored on Ceph, you can start working on your inference application to expose your model.

For the purpose of this tutorial you can reuse the [application](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/wsgi.py) created using Flask, that
exposes some useful endpoints (e.g `/predict` and `/metrics`).

## Make new release

[Create release and build image](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/docs/source/build-images.md)

## Deploy application

### Requirements

- Image Name: `quay.io/thoth-station/elyra-aidevsecops-tutorial:v0.5.0`

- [DeploymentConfig](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/manifests/base/deploymentconfig.yaml)

- [Route](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/manifests/base/route.yaml)

- [Service](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/manifests/base/service.yaml)

### On Operate First using ArgoCD

[ArgoCD][2], used for Continuous Deployment of your applications, is available on Operate First and you can request the Operate First team to be used for your application.

There are typically two steps you need to follow in order to have a new application deployed on [Operate First][1]:

1. Create all manifests for your project (e.g. deployment, service, routes, workflows, pipelines) and place them in your repo under `/manifests`.

2. [Request support for deployment of your application](https://github.com/operate-first/support/issues/new?assignees=&labels=onboarding&template=onboarding_argocd.md&title=).

In this way [ArgoCD][2] will be used to maintain your application always in sync with your current changes. Once you create a new release of your application (e.g. you changed your model, you added a new metric, you added a new feature) and a new image is available, you need to update the [imagestreamtag](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/bb6fad2441e8df8aa56c2c0e6b5ac45a2cda42eb/manifests/overlays/test/imagestreamtag.yaml#L10) so that ArgoCD can deploy new version.

Note: [AICoE Pipeline][3] can also update automatically the [imagestreamtag](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/bb6fad2441e8df8aa56c2c0e6b5ac45a2cda42eb/manifests/overlays/test/imagestreamtag.yaml#L10) once a new release is created.

Once everything is synced to the cluster, you can monitor your application from the [ArgoCD][2] using this [link](https://argocd-server-argocd.apps.zero.massopen.cloud/applications) as shown in the image below:

<div style="text-align:center">
<img alt="Argo CD UI" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/ArgoCDUI.png">
</div>

### Using Openshift CLI

1. Open a terminal in Jupyterlab

2. Login from the terminal `oc login $CLUSTER_URL`.

3. Insert your credentials `USERNAME` and `PASSWORD`.

4. Make sure you are in `elyra-aidevsecops-tutorial` directory (you can run `pwd` command in the terminal to check your current path).

5. Create Service using `oc apply -f ./manifests/base/service.yaml`.

6. Create Route using `oc apply -f ./manifests/base/route.yaml`.

7. Create DeploymentConfig using `oc apply -f ./manifests/deploymentconfig.yaml`.

## References

* [Operate First][1]
* [ArgoCD][2]
* [AICoE Pipeline][3]

[1]: https://www.operate-first.cloud/
[2]: https://argoproj.github.io/argo-cd/
[3]: https://github.com/AICoE/aicoe-ci
