# Created by rapid at 9/22/2020
Feature: # C5153 Verify if the Device offline card shows the proper number of devices

  Scenario: # C5153 Verify if the Device offline card shows the proper number of devices
    Given Loginpage
    Then Login with the given credentials
    Then Verify if the number of devices on the DEVICE OFFLINE card should match the number of devices with online status on the Devices page