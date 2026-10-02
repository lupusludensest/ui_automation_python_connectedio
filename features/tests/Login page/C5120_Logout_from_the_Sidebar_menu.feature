# Created by rapid at 9/13/2020
Feature: # C5120 Logout from the Sidebar_menu

  Scenario: # C5120 Logout from the Sidebar_menu and verify the login page will open after logout
    Given Loginpage
    Then Login with the given credentials
    Then Click on the User name in the Sidebar menu
    Then Hover over the Logout button in the dropdown menu and click on the button Logout
    And https://devcloud.connectedio.com/ is open