# How to run an AI Pipeline with Elyra



1. Access the [Elyra][1] UI by opening the `*.pipeline` file you created in the previous step. Click the "Run" button in the upper left of the UI to start the AI Pipeline.

<div style="text-align:center">
<img alt="Elyra AI Pipeline play" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/PlayAIPipeline.png">
</div>

2. After clicking "Run", you will be presented with a dialogue box where you need to select which runtime environments to use as well as add a name for your pipeline. Click "OK" to submit your pipeline.

<div style="text-align:center">
<img alt="Elyra AI Pipeline run inputs" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/AIPipelineRunInputs.png">
</div>

3. Now your pipeline has been submitted, move to the [Kubeflow Pipeline UI](http://istio-ingressgateway-istio-system.apps.zero.massopen.cloud/pipeline/#/experiments) to see what is happening.

<div style="text-align:center">
<img alt="Kubeflow Pipeline UI" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/KFPUI.png">
</div>

4. From here you can check the status of each step in the pipeline directly from the UI and debug from the logs if any problems occur.

<div style="text-align:center">
<img alt="Successfull Kubeflow Pipeline" src="https://raw.githubusercontent.com/thoth-station/elyra-aidevsecops-tutorial/master/docs/images/SuccessfullKubeflowPipeline.png">
</div>

Once the pipeline completes successfully, the model is stored in your bucket. You can check from your terminal with the [aws CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) using the following command:

```bash
  aws s3 --profile moc-pipeline-kfp --endpoint https://s3-openshift-storage.apps.zero.massopen.cloud/ ls s3://{your_bucket}/{your_project_name}/models/
```

where `moc-pipeline-kfp` is the aws profile containing `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to access your bucket.

## Additional Resources

For more examples on how to create AI pipelines with Elyra, you can use this [link](https://github.com/elyra-ai/examples/tree/master/pipelines/hello_world_kubeflow_pipelines).

## Next Step
[Deploy your model](/docs/source/deploy-model.md)

## References

* [Elyra][1]

[1]: https://github.com/elyra-ai/elyra
