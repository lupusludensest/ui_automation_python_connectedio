from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
LOGIN_EMAIL = (By.XPATH, "//input[@placeholder='Email address']")
LOGIN_PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
LOGIN_BTN = (By.CSS_SELECTOR, "button.btn.btn-primary.text-uppercase.w-100.font-weight-bold.gradient-btn.shadow-1.border-0")
POP_UP_WNDW_OK_BTN = (By.XPATH, "//div[@class='swal2-actions']//button[@class='swal2-confirm btn btn-outline-primary btn-sm btn-custom swal2-styled']")
DVCS_ICN = (By. XPATH, "//i[@class='fa fa-hdd-o']")
ADD_NW_DVC_RGHT_CRNR = (By.XPATH, "//span[contains(text(), ' Add New Device ')]")
DVC_IMEI_FLD = (By.XPATH, "//input[@placeholder='IMEI']")
DVC_NAME_FLD = (By.XPATH, "//input[@placeholder='Device name']")
DVC_SRL_NMBR_FLD = (By.XPATH, "//input[@placeholder='Serial number']")
DVC_ADD_SAVE_BTN = (By.XPATH, "(//button[@type='submit'])[1]")
IMEI_HR = (By.XPATH, "//a[contains(text(), '356961071557824')]")
EMEI_CLCK = (By.XPATH, "(//a[@class='ng-star-inserted'])[5]")
# MODEL_TYPE = (By.XPATH, "(//span[@class='ng-tns-c8-1'])[10]")
# MODEL_TYPE = (By.XPATH, "(//li[@class='ng-tns-c8-1'])[2]")
# MODEL_TYPE = (By.XPATH, "(//span[@class='ng-tns-c11-17'])[10]")
# MODEL_TYPE = (By.XPATH, "(//span[@class='ng-tns-c11-24'])[10]")
MODEL_TYPE = (By.XPATH, "//*[contains(text(), 'ER2000T-NA-CAT1')]")
FRM_VRSN = (By.XPATH, "(//span[@class='ng-tns-c8-1'])[11]")
MDM_FRM = (By.XPATH, "(//span[@class='ng-tns-c8-1'])[12]")
LAST_HEARD = (By.XPATH, "(//strong[@class='d-block mb-1'])[5]")
UPTIME = (By.XPATH, "(//strong[@class='d-block mb-1'])[6]")
CHCK_BX_FOR_DLT = (By.XPATH, "(//div[@class='fancy-checkbox devicelist-checkbox select-all'])[1]")
GEAR_BTN = (By.XPATH, "//button[@class='btn btn-default btn-sm dropdown-toggle px-3 dropdown-toggle']")
RMV_DVCS_BTN = (By.XPATH, "(//a[@class='dropdown-item ng-star-inserted'])[2]")
DLT_BTN_DVCS = (By.XPATH, "//button[@class='btn btn-sm btn-danger']")
SCCSS_DLT_NO_DT_AVLBL = (By.XPATH, "//div[contains(text(), 'No Data Available')]")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://devcloud.connectedio.com' )

# 2. Send Login e-mail
wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).clear()
wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).send_keys('gurovvic@gmail.com') # vadim@mailinator.com

# 3. Send Password
wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).clear()
wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).send_keys('MyUSA2016!@') # manicpiano731

# 4. Click on Login button
wait.until(EC.element_to_be_clickable(LOGIN_BTN)).click()

# 5. Click on pop-window OK button
wait.until(EC.element_to_be_clickable(POP_UP_WNDW_OK_BTN)).click()

# 6. Go to the Devices page https://devcloud.connectedio.com/devices
wait.until(EC.element_to_be_clickable(DVCS_ICN)).click()
expected_text = 'https://devcloud.connectedio.com/devices'
actual_text = driver.current_url
assert expected_text in actual_text
if expected_text == actual_text:
    print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
else:
    print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

# 7. Click Add new device button on the right up corner
wait.until(EC.element_to_be_clickable(ADD_NW_DVC_RGHT_CRNR)).click()

# 8. Fill required Device IMEI field
wait.until(EC.presence_of_element_located(DVC_IMEI_FLD)).clear()
wait.until(EC.presence_of_element_located(DVC_IMEI_FLD)).send_keys('356961071557824')

# 9. Fill Device Name field if any
wait.until(EC.presence_of_element_located(DVC_NAME_FLD)).clear()
wait.until(EC.presence_of_element_located(DVC_NAME_FLD)).send_keys('TVM Test123 jjnkjn')

# 10. Fill required Serial Number field
wait.until(EC.presence_of_element_located(DVC_SRL_NMBR_FLD)).clear()
wait.until(EC.presence_of_element_located(DVC_SRL_NMBR_FLD)).send_keys('1806208A0279')

# 11. Select Tags if any
# No tags here to select

# 12. Click Save and refresh the page
wait.until(EC.element_to_be_clickable(DVC_ADD_SAVE_BTN)).click()
driver.refresh()

# 13.
# Pay attention to the following device details: IMEI, Model, Firmware version, Modem firmware, Last heard, Uptime.
# Success is here - device is on the page
actual_text = wait.until(EC.visibility_of_element_located(IMEI_HR)).text
print(f'IMEI: "{actual_text}"\n')
expected_text = '356961071557824'
assert expected_text in actual_text
if expected_text == actual_text:
    print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
else:
    print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

#  14. Choose any device with IMEI number which is highlighted in blue active IMEI number and click on an active IMEI number
wait.until(EC.element_to_be_clickable(EMEI_CLCK)).click()

# 15. Verify that model of device is ER2000T-NA-CAT1
actual_text = wait.until(EC.visibility_of_element_located(MODEL_TYPE)).text
print(f'Model: "{actual_text}"\n')
expected_text = 'ER2000T-NA-CAT1'
assert expected_text in actual_text
if expected_text == actual_text:
    print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
else:
    print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

# 16. Verify that Firmware version is VR2 4.0
actual_text = wait.until(EC.visibility_of_element_located(FRM_VRSN)).text
print(f'Firmware version: "{actual_text}"\n')
expected_text = 'VR2 4.0'
assert expected_text in actual_text
if expected_text == actual_text:
    print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
else:
    print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

# 17. Verify that Modem firmware is 20.00.524
actual_text = wait.until(EC.visibility_of_element_located(MDM_FRM)).text
print(f'Modem firmware: "{actual_text}"\n')
expected_text = '20.00.524'
assert expected_text in actual_text
if expected_text == actual_text:
    print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
else:
    print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

# 18. Verify that Last heard is here
actual_text = wait.until(EC.visibility_of_element_located(LAST_HEARD)).text
print(f'Last heard is here: "{actual_text}"\n')
expected_text = 'Last heard'
assert expected_text in actual_text
if expected_text == actual_text:
    print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
else:
    print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

# 19. Verify that Uptime is here
actual_text = wait.until(EC.visibility_of_element_located(UPTIME)).text
print(f'Uptime is here: "{actual_text}"\n')
expected_text = 'Uptime'
assert expected_text in actual_text
if expected_text == actual_text:
    print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
else:
    print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

# 20. Delete device
# Go to the Devices page https://devcloud.connectedio.com/devices
wait.until(EC.element_to_be_clickable(DVCS_ICN)).click()
sleep(2)
# Mark checkbox
wait.until(EC.element_to_be_clickable(CHCK_BX_FOR_DLT)).click()
# Click gearbutton
wait.until(EC.element_to_be_clickable(GEAR_BTN)).click()
# Click remove devices button
wait.until(EC.element_to_be_clickable(RMV_DVCS_BTN)).click()
# Click delete button
wait.until(EC.element_to_be_clickable(DLT_BTN_DVCS)).click()
# Verify Success after delete is here
actual_text = wait.until(EC.visibility_of_element_located(SCCSS_DLT_NO_DT_AVLBL)).text
print(f'No Data Available: "{actual_text}"\n')
expected_text = 'No Data Available'
assert expected_text in actual_text
if expected_text == actual_text:
    print(f'Expected "{expected_text}", and got: "{actual_text}" \n')
else:
    print(f'Expected "{expected_text}", but got: "{actual_text}" \n')

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()