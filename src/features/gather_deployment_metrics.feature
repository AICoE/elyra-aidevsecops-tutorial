Feature: Model Deployed Test
    Scenario: Deployment metrics gathering
        Given dataset is available
        Given deployment is accessible using HTTP
        When I run test to gather metrics on predict endpoint
        Then I should get model and application metrics
