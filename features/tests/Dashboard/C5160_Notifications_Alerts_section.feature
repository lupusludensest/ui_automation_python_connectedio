# Created by rapid at 9/29/2020
Feature: # C5160 Notifications Alerts section

  Scenario: # C5160 Notifications Alerts section
    Given Loginpage
    Then Login with the given credentials
    Then Click Dashboard menu icon and make sure Dashboard page reloaded
    Then Make sure Notifications / Alerts block is present on the screen
    And Hover over question mark in top right of the block and make sure tooltip appears
    Then Make sure that click on column header Groups makes it active by moving underscore sign = 0px none to it
    Then Verify Device inactive column highlighted grey 128, 128, 128, 1 when hover over it and hold
    And The inscription No Data Available is in the center and does not shift when switching columns
    Then Click on Device and verify text No Data Available is here
    Then Locations of the No Data Available if Groups is active=undescored 0px none
    Then Locations of the No Data Available if Device is active=undescored 0px none
    Then Verify the inscription No Data Available is in the center and does not shift when switching columns

