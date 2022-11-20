Feature: Registration on Parasoft website

    This file focuses on Registration process of the application https://parabank.parasoft.com/parabank/index.htm

    Background:

    @regression
    Scenario: Register to the website with valid details
        # Given I navigate to the registration page
        Given I provide my details in the registration form
        When I click register button
        Then the registration should be successful
    
    @regression
    Scenario: Login after successful registration
        # Given I navigate to the registration page
        Given I provide my details in the registration form
        And I click register button
        When the registration is successful
        Then I should be able to login with the registered creds

    @regression
    Scenario: Register again with the same details should not be allowed
        # Given I navigate to the registration page
        Given I provide my details in the registration form
        And I click register button
        And the registration is successful
        When I provide the same details again in the registration form
        And I click register button
        Then the registration should not be successful

    @api
    Scenario: Register via API 
        Given I send my details to registration api
        Then the response code is 200

    @api
    Scenario: Login after Register via API 
        Given I send my details to registration api
        Then the response code is 200
        # And I logout
        Then I should be able to login via the login api
