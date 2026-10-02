# Created by rapid at 9/25/2020
Feature: # C5156 Verify if the Alert Notification card is working

  Scenario: # C5156 Verify if the Alert Notification card is working
    Given Loginpage
    Then Login with the given credentials
    Then Click on ALERT/NOTIFICATION card
    Then Verify Alert Dashboard words on the page
    And https://devcloud.connectedio.com/alerts is open

