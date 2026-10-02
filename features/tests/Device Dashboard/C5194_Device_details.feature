# Created by rapid at 10/16/2020
Feature: # C5194_Device_details

  Scenario: # C5194_Device_details
    Given Loginpage
    Then Login with the given credentials
    And Go to the Devices page https://devcloud.connectedio.com/devices
    Then Click Add new device button on the right up corner
    Then Fill required Device IMEI field 356961071557824
    And Fill Device Name field if any TVM Test123 jjnkjn
    Then Fill required Serial Number field 1806208A0279
    And Click Save and refresh the page
    Then Success is here - device is on the page
    Then IMEI 356961071557824 is here
    Then Model ER2000T-NA-CAT1 is here
    And Firmware version VR2 4.0 is here
    And Modem firmware 20.00.524 is here
    Then Words Last heard is here
    And Section Uptime is here
    Then Delete device

