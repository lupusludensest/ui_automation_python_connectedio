# Created by rapid at 9/24/2020
Feature: # C5155 Verify if the Inventory card shows the proper number of devices

  Scenario: # C5155 Verify if the Inventory card shows the proper number of devices
    Given Loginpage
    Then Login with the given credentials
    Then Verify if the number of devices on the INVENTORY card should match the number of devices with online status on the Devices page