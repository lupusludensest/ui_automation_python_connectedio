# Created by rapid at 9/23/2020
Feature: # C5154_Verify_if_the_"Inventory"_card_is_working

  Scenario: # C5154_Verify_if_the_"Inventory"_card_is_working
    Given Loginpage
    Then Login with the given credentials
    Then Click on the INVENTORY card
    And https://devcloud.connectedio.com/devices is open
    And Inventory status in FILTERS field