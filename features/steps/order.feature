Feature: Order a Product

  Scenario: Ordering a product
    Given I am on the inventory page
    When user sorts products from low price to high price
    And user adds the lowest priced product
    And user clicks on cart
    And user clicks on checkout
    And user enters first name "John"
    And user enters last name "Doe"
    And user enters zip code "123"
    And user clicks continue button
    Then I verify in the checkout overview page if the total amount for the added item is $8.63
    When user clicks finish button
    Then "Thank you" header is shown in the checkout complete page