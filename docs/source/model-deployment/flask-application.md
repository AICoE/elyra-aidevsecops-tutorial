# Deploy your model as a Flask application

## Create your Flask app

Once you've trained your model and it's stored on Ceph, you can start working on an inference application to make your model available for use by others.

For the purpose of this tutorial you can reuse the [application](../../../wsgi.py) created with Flask. This app exposes some useful endpoints for serving and monitoring our model (e.g `/predict` and `/metrics`).

### 1. Make a new release

[Create a new release and build the image](../build-images.md)

### 2. Deploy your application

#### **Requirements**

- Image Name: `quay.io/thoth-station/elyra-aidevsecops-tutorial:v0.5.0`

- [DeploymentConfig](../../../manifests/base/deploymentconfig.yaml)

- [Route](../../../manifests/base/route.yaml)

- [Service](../../../manifests/base/service.yaml)

#### **Using Operate First with ArgoCD**

[ArgoCD][2] is a tool used for Continuous Deployment of applications and is available for use on the Operate First. You can make a request to the Operate First team to use ArgoCD for your application.

There are two steps you need to follow in order to have a new application deployed on [Operate First][1]:

1. Create all the manifests for your project (e.g. deployment, service, routes, workflows, pipelines) and place them in your repo under `/manifests`.

2. Submit an issue to [operate-first/support](https://github.com/operate-first/support/issues/new?assignees=&labels=onboarding&template=onboarding_argocd.md&title=) to request deployment of your application.

This way [ArgoCD][2] will be used to maintain your application and keep it in sync with all of your current changes. Once you create a new release of your application (e.g. you change your model, you add a new metric, you add a new feature, etc.) and a new image is available, all you need to do is update the [imagestreamtag](../../../manifests/overlays/test/imagestreamtag.yaml#L10) so that ArgoCD can deploy new version.

Note: An [AICoE Pipeline][3] can also automatically update the [imagestreamtag](../../../manifests/overlays/test/imagestreamtag.yaml#L10) once a new release is created.

Once everything is synced to the cluster, you can monitor your application from the [ArgoCD][2] UI using this [link](https://argocd-server-argocd.apps.moc-infra.massopen.cloud/applications) as shown in the image below:

<div style="text-align:center">
<img alt="Argo CD UI" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/ArgoCDUI.png">
</div>

#### **Using OpenShift CLI**

Alternatively, you can also deploy your app manually to a cluster using the following OpenShift CLI commands.

1. Open a terminal in Jupyterlab

2. Login from the terminal: `oc login $CLUSTER_URL`.

3. Insert your credentials `USERNAME` and `PASSWORD`.

4. Make sure you are in `elyra-aidevsecops-tutorial` directory (you can run `pwd` command in the terminal to check your current path).

5. Create the Service using: `oc apply -f ./manifests/base/service.yaml`.

6. Create the Route using: `oc apply -f ./manifests/base/route.yaml`.

7. Create the DeploymentConfig using: `oc apply -f ./manifests/deploymentconfig.yaml`.

Once your pods deploy your Flask app should be ready to serve inference requests from the exposed Route.

## Next Steps
[Test your deployed inference application](/docs/source/test-model.md)


## References

* [Operate First][1]
* [ArgoCD][2]
* [AICoE Pipeline][3]

[1]: https://www.operate-first.cloud/
[2]: https://argoproj.github.io/argo-cd/
[3]: https://github.com/AICoE/aicoe-ci
