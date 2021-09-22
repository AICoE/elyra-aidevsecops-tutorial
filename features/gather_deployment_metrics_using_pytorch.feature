Feature: Gather metrics deployed model using Pytorch dataset
    Scenario: Deployment metrics gathering
        Given dataset is available from Pytorch
        Given deployment is accessible
        When I run test to gather metrics on predict endpoint
        Then I should get model and application metrics
