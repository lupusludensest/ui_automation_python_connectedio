# Created by rapid at 9/14/2020
Feature: # C5121 Logout from_the_Header

  Scenario: # C5121 Logout from_the_Header and verify the login page will open after logout
    Given Loginpage
    Then Login with the given credentials
    Then Hover over the Logout button at the right corner of the Header and click on the button Logout
    And https://devcloud.connectedio.com/ is open