# Created by rapid at 10/3/2020
Feature: # C5162 Signal Strength section

  Scenario: # C5162 Signal Strength section
    Given Loginpage
    Then Login with the given credentials
    Then Click Dashboard menu icon and make sure Dashboard page reloaded
    And Make sure Signal Strength is on the screen
    Then Mouse hover question mark in top right of the Signal Strength block and make sure tooltip appears
    Then The inscription No Data Available is in the center of Signal Strength block
