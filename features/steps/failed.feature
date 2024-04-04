Feature: Demo Failed Login Page

  Scenario: Login with LockedOutUser account
    Given I am on the demo login page
    When I fill the account information for account LockedOutUser into the username field and the password field
    And I click the login button
    Then I verify the error message contains the text "Sorry, this user has been banned"
