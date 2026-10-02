# Created by rapid at 9/8/2020
Feature: # C5472 Add New User

  Scenario: # C5472 Add New User
    Given Loginpage
    Then Login with the given credentials
    Then Click on the Users button
    Then Click on the Quick actions button
    Then Select Add in the drop-down menu
    Then Fill out the required fields
    And Click on the Add button
    Then Verify the words Verification Pending is here