
## Release 0.14.0 (2022-01-13T11:23:03)
### Features
* Update custom elyra base image
* :ship: Deploy the Tag pr-1 for elyra-aidevsecops-tutorial
* :ship: Deploy the Tag pr-1 for elyra-aidevsecops-tutorial
* :ship: Deploy the Tag v0.13.1 for elyra-aidevsecops-tutorial
* :ship: Deploy the Tag v0.13.1 for elyra-aidevsecops-tutorial
* :ship: Deploy the Tag v0.13.1 for elyra-aidevsecops-tutorial

## Release 0.13.1 (2021-10-20T17:26:16)
### Features
* update custom base image for correct jupyter version (#458)
* Fix build jupyter book (#457)

## Release 0.13.0 (2021-10-15T12:58:01)
### Features
* Add node selector to manifest (#455)
* update link to smaug cluster (#451)
* Fix links in main README (#447)
* Feature/neural magic extension of the Elyra Tutorial (#446)
* update pre-requisite
* Update models
* Update README.md
* Add link to video of the workshop at DevConf.US
* Add slide from workshop devconfus2021 (#288)
* :ship: Deploy the Tag v0.12.1 for elyra-aidevsecops-tutorial
### Improvements
* Remove html part and update overlays
### Other
* remove jbook html files

## Release 0.12.1 (2021-09-02T16:03:22)
### Features
* Use v0.3.3 custom elyra image
* Update deploy model with ArgoCD
* Add details on Git dialog form
* Merge content for book
* update TOC
* Adjust yaml
* Rename subsection
* rename section
* Update release
* Remove section
* Update push changes
* Update bots and release section
* Correct requirements
* Fix file format link
* Update manage dependencies section
* Update ArgoCD section (#263)
* update branding (#266)
* update which robot key is needed (#261)
* Use thoth-advise manager
* contact us prose (#255)
* update flask-app prose (#254)
* define prereqs with meteor (#252)
* add conclusion (#247)
* add instructions for kebechet (#235)
* :ship: Deploy the Tag v0.12.0 for elyra-aidevsecops-tutorial
### Bug Fixes
* fix env creds handling (#270)
* Fix incorrect instruction number rendering error (#262)
* fix links in pre-requisite.md (#251)
### Improvements
* added documentation for using secrets (#250)
* added more instructions to create pipeline (#237)
### Other
* Apply suggestions from code review

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

## Release 0.8.0 (2021-05-06T08:33:29)
### Features
* Add missing references (#153)
* Add variable to store metrics (#152)
* Update the aicoe-ci config file with proper image (#151)
* add datasets for pipeline (#144)
### Improvements
* Describe Integration test (#154)
* Use behave for gathering metrics and running integration test (#148)
* Download and test script (#146)
* Add test (#145)

## Release 0.8.1 (2021-06-24T14:37:34)
### Features
* add dependencies for experiment (#171)
* :ship: Deploy the Tag v0.8.0 for elyra-aidevsecops-tutorial
* :ship: Deploy the Tag v0.7.0 for elyra-aidevsecops-tutorial
* :ship: Deploy the Tag v0.6.0 for elyra-aidevsecops-tutorial
* Update .aicoe-ci.yaml (#163)
* :arrow_down_small: set the resource requirements as per usage (#162)
* add more metrics (#157)
* :hatched_chick: update the prow resource limits (#159)

## Release 0.9.0 (2021-07-01T13:22:05)
### Features
* Updated Training Notebook (#167)
* :ship: Deploy the Tag v0.8.1 for elyra-aidevsecops-tutorial

## Release 0.9.1 (2021-07-03T17:33:02)
### Features
* Add library
* :ship: Deploy the Tag v0.9.0 for elyra-aidevsecops-tutorial

## Release 0.10.0 (2021-07-14T18:14:56)
### Features
* Use new elyra custom image for build
* add relative links in md (#186)
* add configs and html for jupyterbook (#184)
* :ship: Deploy the Tag v0.9.1 for elyra-aidevsecops-tutorial
### Improvements
* Modify approvers and reviewers (#187)

## Release 0.10.1 (2021-07-15T16:01:46)
### Other
* remove package present in base image

## Release 0.11.0 (2021-07-27T13:22:00)
### Features
* Update build images documentation. (#209)
* proofread `README.md` (#203)
* modified create ai pipeline doc (#207)
* modifying notebooks for automation (#197)
* update model deployment docs (#208)
* proofread `setup-initial-environment.md` (#201)
* update `explore nb` markdown (#206)
* update pre-req.md (#205)
* proofread test-model.md (#200)
* :ship: Deploy the Tag v0.10.1 for elyra-aidevsecops-tutorial
### Improvements
* Update use-bots documentation and reference in README (#204)
* polish run-ai-pipeline.md (#202)

## Release 0.12.0 (2021-08-16T08:10:21)
### Features
* new base custom image
* add prose to set up aicoe-ci (#233)
* Update initial setup doc to specify when to use which JH instance. (#220)
* modified push changes doc (#221)
* :ship: Deploy the Tag v0.11.0 for elyra-aidevsecops-tutorial
### Bug Fixes
* fixing broken links (#214)
### Improvements
* added more instructions to run ai pipeline (#242)
