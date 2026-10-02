# Created by rapid at 11/8/2020
Feature: # C5210 Verify notification if fetching system log failed

  Scenario: # C5210 Verify notification if fetching system log failed
   Given Loginpage
   Then Login with the given credentials
   And Go to the Devices page https://devcloud.connectedio.com/devices
   Then Click Add new device button on the right up corner
   Then Fill required Device IMEI field 356961071557824
   And Fill Device Name field if any TVM Test123 jjnkjn
   Then Fill required Serial Number field 1806208A0279
   And Click Save and refresh the page
   Then Success is here - device is on the page
   And Choose any device with IMEI number which is highlighted in blue active IMEI number and click on an active IMEI number
   Then Click on Quick action button
   And Click System log subsection
   And Verify Refresh subsection is active and Fetching data from device... appeares
#  And Verify pop-up notification Failed. Device not reachable! appeares
   Then Delete device
