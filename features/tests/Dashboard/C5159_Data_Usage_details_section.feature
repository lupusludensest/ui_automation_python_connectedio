# Created by rapid at 9/27/2020
Feature: # C5159 Data Usage details section

  Scenario: # C5159 Data Usage details section
    Given Loginpage
    Then Login with the given credentials
    Then Click Dashboard menu icon and make sure Dashboard page reloaded
    Then Make sure Data Usage Details block DATA USAGE is present on the screen
    And Hover over question mark in top right of the block and make sure tooltip WAN/Cellular data usage classified periodically. appears
    And Change in drop-down changes the columns = click on Today option from drop-down menu
    Then The inscription No Data Available is in the center
    Then Verify GB inactive column highlighted grey 128, 128, 128, 1 when hover over it and hold