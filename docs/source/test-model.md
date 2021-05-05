# Test inference application deployed

If you want to test your application deployed in the cluster you can run the [integration test](https://github.com/thoth-station/elyra-aidevsecops-tutorial/tree/master/features) using [behave][1] package.

Behave uses Behavior-driven development (or BDD), an agile software development technique that encourages and faciliate collaboration between developers, QA and non-technical or business participants.

1. Install [thamos][2] using pip:

```bash
  pip install thamos
```

2. Create an env and install dependencies using [thamos][2] from the root directory of the tutorial, selecting the appropriate overlays `test-model`.

```bash
  python3 -m venv venv/ && . venv/bin/activate && thamos install -r test-model
```

3. Run [behave][1] command from the root directory of the tutorial.

```bash
  DEPLOYED_MODEL_URL=http://elyra-aidevsecops-tutorial-thoth-deployment-examples.apps.zero.massopen.cloud behave
```

Example of the output received:

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

4. Checking metrics produced running

```bash
  cat metrics.json
```

```python
{'average_latency': 0.03846242621075362, 'average_error': 0.001}
```

## References

* [behave][1]
* [thamos][2]

[1]: https://behave.readthedocs.io/en/stable/
[2]: https://github.com/thoth-station/thamos
