Feature: Successful login

  Scenario: Login with valid credentials
    Given I am on the Demo login page
    When I fill the account information for account standarduser into the username field and the password field
    And I click the login button
    Then I am redirected to the demo main page
    And I verify the App Logo exists
