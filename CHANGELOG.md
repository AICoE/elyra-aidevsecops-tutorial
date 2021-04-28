
## Release 0.1.0 (2021-01-26T08:49:31)
### Features
* Remove jupyter from dev package (#22)
* Fix context path overalys for deployment (#19)
* Adjust pre-commit (#21)
* Create flask app with endpoints to request prediction and metrics (#12)
* Add overlays (#18)
* Add manifests (#15)
* Update aicoe yaml (#16)
* Update thoth yaml (#13)

## Release 0.2.0 (2021-01-26T13:43:11)
### Features
* Use smart changelog (#33)
* Add flask exporter prometheus (#31)
* Adjust deploy in .aicoe.yaml for handling correctly the overlays context path (#29)
* Add gunicorn (#32)
* Add bot approvers for release (#27)

## Release 0.2.1 (2021-01-26T17:38:06)
### Features
* Update wsgi.py (#40)
* Adjust context path for image tag update (#39)
* Add WIP (#37)

## Release 0.2.2 (2021-01-27T13:54:16)
### Features
* Update wsgi.py (#42)
* :ship: Deploy the Tag v0.2.1 for elyra-aidevsecops-tutorial

## Release 0.2.3 (2021-02-01T14:50:58)
### Features
* Fix broken link. (#51)
* :ship: Deploy the Tag v0.2.2 for elyra-aidevsecops-tutorial (#50)

## Release 0.3.0 (2021-02-10T15:51:32)
### Features
* Include option to use Ceph for Kubeflow Pipeline on Tekton (#57)
* Update download dataset notebook (#54)
* :ship: Deploy the Tag v0.2.3 for elyra-aidevsecops-tutorial

## Release 0.4.0 (2021-02-15T14:56:19)
### Features
* update ci config to support build and delivery from overlay (#70)
* Restore overlay for training (#71)
* adjust-overlays (#69)
* Correct notebook link and add one image in docs (#67)
* Correct sentence (#66)
* Add screenshots on how to run the Elyra AI Pipeline (#65)
* Add image and step on how to start new pipeline editor in Elyra (#64)
* Correct name image (#62)
* Improve doc tutorial (#46)
* :ship: Deploy the Tag v0.3.0 for elyra-aidevsecops-tutorial
### Improvements
* Add notebook dependencies in notebooks and overlays matchin notebook kernels and dependencies using jupyterlab-requirements (#68)
* Add notebook to test deployed model (#61)

## Release 0.5.0 (2021-02-22T07:45:11)
### Features
* Update description of successfull pipeline (#88)
* Add store model ceph (#86)
* Add completed pipeline (#85)
* Connect once to S3 (#84)
* adjust-notebook (#83)
* Add missing package to overlay (#82)
* Optional loading of the model from Ceph (#79)
* Add latency to output of predicted model (#78)
* Add link to AICOE yaml for clarification (#77)
* Adjust image links (#76)
* Updated steps in the tutorial (#75)
### Improvements
* Adjust test script and test notebook (#87)

## Release 0.6.0 (2021-02-26T14:43:24)
### Features
* Correct requirements (#114)
* Add missing references
* Update reference (#112)
* Refactor and correct errors (#111)
* Configure overlays directory (#109)
* Add links manifest (#108)
* Add Openshift example (#107)
* Final changes (#106)
* Describe where to find information for the bucket (#104)
* Add URL GitHub repo to be cloned (#103)
* Make pre-commit happy (#102)
* Add inputs for Kubeflow Pipeline inputs (#101)
* Improve Runtime images part (#100)
* Add Kebechet update image (#99)
* Add Tekton pipelines overlays builds images (#97)
* Change section order (#96)
* :ship: Deploy the Tag v0.5.0 for elyra-aidevsecops-tutorial
* Add description on how to Push changes to GitHub (#93)
* Update image for runtime images creation using command palette (#92)
* Update notebook dependencies (#91)
### Improvements
* Describe Git Extenstion use (#105)
* Add ArgoCD image and description (#98)
* Add links to KFP and Tekton (#94)
* Adjust software stack not to use * (#95)

## Release 0.7.0 (2021-04-28T06:28:23)
### Features
* Make tutorial an exeriment to be spawned by JH on Operate First (#138)
* Delete CODEOWNERS
* Fix pipeline GitHub URL (#135)
* Add correct KFP URL to run pipeline (#128)
* Adjust KFP UI URL (#134)
* Add alternative to create runtime images and runtime through CLI
* Split cases for model deployment
* Separate personas
* update link for KFP
* Use correct Ceph URL
* Update ArgoCD URL
* make-pre-commit happy
* Reaplace cnv with zero
* Post workshop errors correction (#120)
* :sparkles: let's run pre-commit
* Update .aicoe-ci.yaml
* Update OWNERS
### Improvements
* use only overlays (#127)
### Other
* remove unusued env variables
