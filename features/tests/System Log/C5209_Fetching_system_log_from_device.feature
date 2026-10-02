# Created by rapid at 11/4/2020
Feature: # C5209 Fetching system log from device

  Scenario: # C5209 Fetching system log from device
   Given Loginpage
   Then Login with the given credentials
   And Click Dashboard menu icon and make sure Dashboard page reloaded
   Then Click on DEVICE ONLINE card
   And Add a new device to the Device online
   And Choose any device with IMEI number which is highlighted in blue active IMEI number and click on an active IMEI number
   Then Click on Quick action button
   And Click System log subsection
   Then Verify the device system log is displayed System Log
   Then Click on the Close icon at the top right corner of the system log
   Then Delete device