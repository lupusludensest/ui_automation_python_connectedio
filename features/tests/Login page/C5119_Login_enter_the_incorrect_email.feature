# Created by rapid at 9/12/2020
Feature: # C5119 Login enter the incorrect email address

  Scenario: # C5119 Login enter the incorrect email address and verify Invalid Login or Password is here
    Given Loginpage
    Then Enter valid, but the incorrect email address in the line "Email address" vadim_wrong@mailinator.com
    Then Enter the correct password in the line "Password" manicpiano731
    Then Verify Invalid Login or Password is on login pop_up