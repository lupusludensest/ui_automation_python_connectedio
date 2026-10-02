# Created by rapid at 9/17/2020
Feature: # C5151 Verify if the Device online card shows the proper number of devices

  Scenario: # C5151 Verify if the Device online card shows the proper number of devices
    Given Loginpage
    Then Login with the given credentials
    Then Verify if the number of devices on the DEVICE ONLINE card should match the number of devices with online status on the Devices page