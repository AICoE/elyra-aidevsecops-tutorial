# Deploy your model as a Flask application

## Create your Flask app

Once you've trained your model and it's stored on Ceph, you can start to work on an inference application to make your model accessible. In this tutorial, we will make a minimal [Flask](https://flask.palletsprojects.com/en/2.0.x/) + [gunicorn](https://docs.gunicorn.org/en/stable/index.html) that we can deploy on OpenShift to serve model inferences. We will also use [ArgoCD][2] for continuous deployment of our application as we make changes.

For the purpose of the tutorial you can reuse this [application script](../../../wsgi.py) created with Flask+gunicorn. This app exposes critical endpoints for serving and monitoring our model, such as `/predict` for generating model predictions from user provided inputs and `/metrics` to measure usage and model performance.

### 1. Make a new release

When you make any changes to your model, typically through retraining, and add a new one to Ceph, you will need to [create a new release and build the image](../thoth-aicoe-services.md) again. This is because you have made new changes to the model that are not reflected in the current image. Once the new tag is created, the pipeline will automatically update the tag where ArgoCD is looking for changes, and your new image will be rebuilt to include your new model and will be seamlessly redeployed.

### 2. Deploy your application

#### **Requirements for Tensorflow+Flask+Gunicorn**

- Image Name: `quay.io/thoth-station/elyra-aidevsecops-tutorial:v0.5.0`

- [DeploymentConfig](../../../manifests/overlays/inference/deploymentconfig.yaml): Deployment configs are templates for running applications on OpenShift. This will give the cluster the necessary information to deploy your Flask application.

- [Service](../../../manifests/base/service.yaml): A service manifest allows for an application running on a set of OpenShift pods to be exposed as a network service.

- [Route](../../../manifests/base/route.yaml): Routes are used to expose services. This route will give your model deployment a reachable hostname to interact with.

#### **Requirements for Pytorch+Flask+Gunicorn**

- Image Name: `quay.io/thoth-station/elyra-aidevsecops-pytorch-inference:v0.13.0`

- [DeploymentConfig](../../../manifests/overlays/pytorch-inference/deploymentconfig.yaml): Deployment configs are templates for running applications on OpenShift. This will give the cluster the necessary information to deploy your Flask application.

- [Service](../../../manifests/overlays/pytorch-inference/service.yaml): A service manifest allows for an application running on a set of OpenShift pods to be exposed as a network service.

- [Route](../../../manifests/overlays/pytorch-inference/route.yaml): Routes are used to expose services. This route will give your model deployment a reachable hostname to interact with.

#### **Requirements for NeuralMagic+Flask+Gunicorn**

NOTE: _Deepsparse deployment at the moment works only with CPU that supports avx2, avx512 flags (even better if [avx512_vnni](https://en.wikichip.org/wiki/x86/avx512_vnni) with VNNI is available: https://github.com/neuralmagic/deepsparse/issues/186). Please check your environment running `cat /proc/cpuinfo` to identify flags and verify if your machine supports the deployment. In the deployment manifests in `nm-inference` overlay you need to set the env variable NM_ARCH=avx2|avx512._

NOTE: Operate First has a [Grafana dashboard](http://grafana.operate-first.cloud/d/LCLH8kd7z/node-feature-discovery?orgId=1) showing what hardware and flags are available across all managed instances. In this way, we can identify the best place to deploy the model.

- Image Name: `quay.io/thoth-station/neural-magic-deepsparse:v0.13.0`

- [DeploymentConfig](../../../manifests/overlays/nm-inference/deploymentconfig.yaml): Deployment configs are templates for running applications on OpenShift. This will give the cluster the necessary information to deploy your Flask application.

- [Service](../../../manifests/overlays/nm-inference/service.yaml): A service manifest allows for an application running on a set of OpenShift pods to be exposed as a network service.

- [Route](../../../manifests/overlays/nm-inference/route.yaml): Routes are used to expose services. This route will give your model deployment a reachable hostname to interact with.


#### **Using Operate First with ArgoCD**

Once all manifests for your project (e.g. deployment, service, routes, workflows, pipelines) are created and placed in your repo under `/manifests` folder, you can make a request to the Operate First team to use ArgoCD for your application.

This way [ArgoCD][2] will be used to maintain your application and keep it in sync with all of your current changes. Once you create a new release of your application (e.g. you change your model, you add a new metric, you add a new feature, etc.) and a new image is available, all you need to do is update the [imagestreamtag](../../../manifests/overlays/inference/imagestreamtag.yaml#L10) so that ArgoCD can deploy new version.

Note: An [AICoE Pipeline][3] can also automatically update the [imagestreamtag](../../../manifests/overlays/test/imagestreamtag.yaml#L10) once a new release is created.

Once everything is synced to the cluster, you can monitor your application from the [ArgoCD][2] UI using this [link](https://argocd.operate-first.cloud/applications) as shown in the image below:

<div style="text-align:center">
<img alt="Argo CD UI" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/ArgoCDUI.png">
</div>

##### **During an Operate First based workshop**
There are two steps you need to follow in order to have a new application deployed on [Operate First][1] and maintained by ArgoCD.

1. Fork [workshop-apps](https://github.com/operate-first/workshop-apps) and clone it from the terminal of your image.

2. Run ./devconf-us-2021.sh script with your GitHub username as parameter:

```
$ ./devconf-us-2021.sh USERNAME
Generating 'apps/devconf-us-2021/USERNAME.yaml'
```

3. Commit, push to your fork of [workshop-apps](https://github.com/operate-first/workshop-apps) and create a PR against orginal repo.

##### **For application staying in Operate First**
Submit an issue to [operate-first/support](https://github.com/operate-first/support/issues/new?assignees=&labels=onboarding&template=onboarding_argocd.md&title=) to request deployment of your application.


#### **Using OpenShift CLI**

Alternatively, you can also deploy your app manually to a cluster using the following OpenShift CLI commands.

1. Open a terminal in Jupyterlab

2. Login from the terminal: `oc login $CLUSTER_URL`.

3. Insert your credentials `USERNAME` and `PASSWORD`.

4. Make sure you are in `elyra-aidevsecops-tutorial` directory (you can run `pwd` command in the terminal to check your current path).

5. `cd` to the overlay you want to deploy. (e.g. `cd manifests/overlays/{inference|pytorch-inference|nm-inference}`)

6. Create the Service using: `oc apply -f ./manifests/overlays/{inference|pytorch-inference|nm-inference}/service.yaml`.

6. Create the Route using: `oc apply -f ./manifests/overlays/{inference|pytorch-inference|nm-inference}/route.yaml`.

7. Create the DeploymentConfig using: `oc apply -f ./manifests/overlays/{inference|pytorch-inference|nm-inference}/deploymentconfig.yaml`.

Once your pods deploy, your Flask app should be ready to serve inference requests from the exposed Route.

## Next Steps
[Test your deployed inference application](/docs/source/test-model.md)


## References

* [Operate First][1]
* [ArgoCD][2]
* [AICoE Pipeline][3]

[1]: https://www.operate-first.cloud/
[2]: https://argoproj.github.io/argo-cd/
[3]: https://github.com/AICoE/aicoe-ci
