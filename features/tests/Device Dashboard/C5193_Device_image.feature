# Created by rapid at 10/14/2020
Feature: # C5193 Device image

  Scenario: # C5193 Device image
    Given Loginpage
    Then Login with the given credentials
    And Go to the Devices page https://devcloud.connectedio.com/devices
    Then Click Add new device button on the right up corner
    Then Fill required Device IMEI field 356961071557824
    And Fill Device Name field if any TVM Test123 jjnkjn
    Then Fill required Serial Number field 1806208A0279
    And Click Save and refresh the page
    Then Success is here - device is on the page
    Then Choose any device with IMEI number which is highlighted in blue active IMEI number and click on an active IMEI number
    Then Verify that model of device is ER2000T-NA-CAT1
    And Device image should be present with the correct layout at the top left corner of page
    And The image of the device should correspond to the model in the description ER2000T1
    Then Delete device