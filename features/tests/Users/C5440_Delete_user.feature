# Created by rapid at 9/11/2020
Feature: # C5440 Delete User

  Scenario: # C5440 Delete User
    Given Loginpage
    Then Login with the given credentials
    Then Click on the Users button
    Then Make sure there are at least two Admins and one User role in the list of users
    Then Click on the Settings 'three vertical' dots from the rightmost side of the user
    Then Choose and click on 'Delete' from the dropdown menu
    Then Confirm action by clicking OK button on the pop-up dialog window
    Then Then Verify that there is for one user less after deleting