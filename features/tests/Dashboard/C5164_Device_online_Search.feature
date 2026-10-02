# Created by rapid at 10/5/2020
Feature: # C5164 Device online Search

  Scenario: # C5164 Device online Search
    Given Loginpage
    Then Login with the given credentials
    Then Click Dashboard menu icon and make sure Dashboard page reloaded
    And Click on DEVICE ONLINE card
    Then Click on Filter Devices and open Search page
    Then Make sure that only Online Devices checkbox is checked in the Search page