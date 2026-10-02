# Created by rapid at 9/16/2020
Feature: # C5149 Verify if all cards and sections are present

  Scenario: # C5149 Verify if all cards and sections are present
    Given Loginpage
    Then Login with the given credentials
    Then Check if all elements are present. 6.1. Cards: "DEVICE ONLINE", 6.2. "DEVICE OFFLINE",  6.3. "INVENTORY", 6.4. "ALERT/NOTIFICATION", 6.5. "DATA USAGE"
    Then Check if sections are present. 7.1 "Data Usage Details", 7.2. "Notifications/Alerts", 7.3. "Groups", 7.4. "Signal Strength", 7.5. "Device Location".

