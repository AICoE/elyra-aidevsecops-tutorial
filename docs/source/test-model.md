# Test inference application deployed

If you want to test your application deployed in the cluster you can run the following integration test using [behave][1] package.

1. Install [thamos][2] using pip:

```bash
  pip install thamos
```

1. Create an env and install dependencies using dependencies using [thamos][2] from the root directory of the tutorial.

```bash
  python3 -m venv venv/ && . venv/bin/activate && thamos install -r test-model
```

2. Run behave command from the root directory of the tutorial.

```bash
  DEPLOYED_MODEL_URL=<MODEL_DEPLOYED_URL> behave
```

## References

* [behave][1]
* [thamos][2]

[1]: https://behave.readthedocs.io/en/stable/
[2]: https://github.com/thoth-station/thamos
