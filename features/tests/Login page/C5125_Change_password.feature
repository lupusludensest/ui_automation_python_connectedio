# Created by rapid at 9/15/2020
Feature: # C5125 Change_password

  Scenario: # C5125 Change password and verify the message is displayed: "Old and new password cannot be same."
    Given Loginpage
    Then Login with the given credentials
    Then Go to the "Change Password" page https://devcloud.connectedio.com/profile/change-password
    And https://devcloud.connectedio.com/profile/change-password is open
    Then Enter the old password in the field "New Password" MyUSA2016!@
    And Enter the old password in the field "Confirm New Password" MyUSA2016!@
    Then Click on the button "Save"
    And Verify the words Old and new password cannot be same. is on the page
