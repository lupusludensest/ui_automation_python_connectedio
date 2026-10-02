# Created by rapid at 9/26/2020
Feature: # C5157 Verify if the Data usage card is rotating

  Scenario: # C5157 Verify if the Data usage card is rotating
    Given Loginpage
    Then Login with the given credentials
    Then Click on the DATA USAGE card with Cellular data used
    Then Verify that the DATA USAGE card has rotated to WAN data used and he DATA USAGE card has rotated back to Cellular data used
