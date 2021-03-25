# Run AI Pipeline

Using [Elyra][1] UI:

1. Use play button to run the AI Pipeline.

<div style="text-align:center">
<img alt="Elyra AI Pipeline play" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/PlayAIPipeline.png">
</div>

2. Before starting the pipeline you need to select which runtime environment to use and add a name for your pipeline.

<div style="text-align:center">
<img alt="Elyra AI Pipeline run inputs" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/AIPipelineRunInputs.png">
</div>

Run your pipeline and move to [Kubeflow Pipeline UI](http://istio-ingressgateway-istio-system.apps.zero.massopen.cloud/pipeline/#/experiments) to see what is happening.

<div style="text-align:center">
<img alt="Kubeflow Pipeline UI" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/KFPUI.png">
</div>

For more examples on how to create an AI pipeline in Elyra, you can use this [link](https://github.com/elyra-ai/examples/tree/master/pipelines/hello_world_kubeflow_pipelines).

You can check the status of each step in the pipeline directly from the UI and debug from logs if any problems occur:

<div style="text-align:center">
<img alt="Successfull Kubeflow Pipeline" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/SuccessfullKubeflowPipeline.png">
</div>

The model is stored in your bucket, you can check from your terminal using [aws CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html):

```bash
  aws s3 --profile moc-pipeline-kfp --endpoint https://s3-openshift-storage.apps.zero.massopen.cloud/ ls s3://{your_bucket}/{your_project_name}/models/
```

where `moc-pipeline-kfp` is the aws profile containing `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to access your bucket.

## References

* [Elyra][1]

[1]: https://github.com/elyra-ai/elyra
