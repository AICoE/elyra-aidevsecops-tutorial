# Test inference application deployed

## Using notebook in JupyterHub

If you want to test your application deployed in the cluster from JH image you can use the following notebook:

- Test model [Jupyter notebook](https://github.com/thoth-station/elyra-aidevsecops-tutorial/blob/master/notebooks/test_deployed_model.ipynb);

(You need to have credentials (token) for the access to [Operate First][1] cluster and have access to the namespace where the application is deployed to run the above notebook).

## From your local machine

If you want to test the application created in this tutorial from your local machine:

PRE-REQUISITE: Make sure you are logged in the cluster where the model is deployed.

1. Install dependencies using [Pipenv](https://github.com/pypa/pipenv).

```bash
  pipenv install
```

or [micropipenv](https://pypi.org/project/micropipenv/):

```bash
  micropipenv install
```

2. Start application.

```bash
  pipenv run python3 wsgi.py
```

3. Run test that will show the input image and then return the prediction from the model.

```bash
  pipenv run python3 src/test.py
```

If you want to test the application deployed you need to provide the URL:

```bash
  THOTH_AIDEVSECOPS_TUTORIAL_MODEL_URL=<MODEL_DEPLOYED_URL> pipenv run python3 src/test.py
```

## References

* [Operate First][1]

[1]: https://www.operate-first.cloud/
