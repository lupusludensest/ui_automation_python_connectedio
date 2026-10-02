# Created by rapid at 10/4/2020
Feature: # C5163 Device Locations section

  Scenario: # C5163 Device Locations section
    Given Loginpage
    Then Login with the given credentials
    Then Click Dashboard menu icon and make sure Dashboard page reloaded
    And Make sure Device Locations words are on the screen
    And Mouse hover question mark in top right of the block and make sure tooltip appears
    Then Make sure that click on Device Locations drop-down list is working