Feature: Gather metrics deployed model
    Scenario: Deployment metrics gathering
        Given dataset is available from Tensorflow
        Given deployment is accessible
        When I run test to gather metrics on predict endpoint
        Then I should get model and application metrics
