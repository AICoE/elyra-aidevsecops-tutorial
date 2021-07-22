# Test your deployed inference application

If you want to test the application that you just deployed in the cluster, run this [integration test](../../features) using the [behave][1] package.

Behave uses behavior-driven development (BDD), an agile software development technique that encourages and facilitates collaboration between developers, QA engineers and business participants.

1. Create a virtual environment and install your dependencies using [thamos][2](the CLI tool for interacting with Thoth and included as a dependency to this repo) from the root directory of this tutorial. Be sure to select the appropriate overlay, which in this case is `test-model`.

```bash
  python3 -m venv venv/ && . venv/bin/activate && thamos install -r test-model
```

2. Run the [behave][1] command from the root directory of the tutorial.

```bash
  DEPLOYED_MODEL_URL=http://elyra-aidevsecops-tutorial-thoth-deployment-examples.apps.zero.massopen.cloud behave
```

Below is an example of the output you should expect to see if the [behave][1] command ran correctly:

```bash
  Scenario: Deployment metrics gathering                    # features/gather_deployment_metrics.feature:2
      Given dataset is available                            # features/steps/model_deployment.py:42
      Given deployment is accessible                        # features/steps/model_deployment.py:56
      When I run test to gather metrics on predict endpoint # features/steps/model_deployment.py:72
      Then I should get model and application metrics       # features/steps/model_deployment.py:128

  1 feature passed, 0 failed, 0 skipped
  1 scenario passed, 0 failed, 0 skipped
  4 steps passed, 0 failed, 0 skipped, 0 undefined
  Took 0m3.394s
```

3. You can also check the metrics produced by running the following command:

```bash
  cat metrics.json
```

```python
{'average_latency': 0.03846242621075362, 'average_error': 0.001}
```

## Next Step:

[Monitor your model and application with Prometheus and Grafana](/docs/source/monitor-model.md)

## References

* [behave][1]
* [thamos][2]

[1]: https://behave.readthedocs.io/en/stable/
[2]: https://github.com/thoth-station/thamos
