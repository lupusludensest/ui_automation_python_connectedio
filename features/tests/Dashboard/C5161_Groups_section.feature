# Created by rapid at 10/2/2020
Feature: # C5161 Groups section

  Scenario: # C5161 Groups section
    Given Loginpage
    Then Login with the given credentials
    Then Click Dashboard menu icon and make sure Dashboard page reloaded
    And Make sure Groups block is on the screen
    Then Mouse hover question mark in top right of the Groups block and make sure tooltip appears
    And The inscription No Data Available is in the center of Groups block
    Then Make sure that click on Groups drop-down list is working
    Then Tooltip appears when mouse hover question mark in top right of the Groups block