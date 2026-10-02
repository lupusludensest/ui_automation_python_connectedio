# Created by rapid at 9/17/2020
Feature: C5150 Verify if the Device online card is working

  Scenario: C5150 Verify if the Device online card is working
    Given Loginpage
    Then Login with the given credentials
    Then Click on DEVICE ONLINE card
    Then Words Device Management Portal are here on the page
    Then Word Online is here on the page

