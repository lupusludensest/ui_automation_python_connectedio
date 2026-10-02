from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
LOGIN_EMAIL = (By.XPATH, "//input[@placeholder='Email address']")
LOGIN_PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
LOGIN_BTN = (By.CSS_SELECTOR, "button.btn.btn-primary.text-uppercase.w-100.font-weight-bold.gradient-btn.shadow-1.border-0")
POP_UP_WNDW_OK_BTN = (By.XPATH, "//div[@class='swal2-actions']//button[@class='swal2-confirm btn btn-outline-primary btn-sm btn-custom swal2-styled']")
DSCH_BRD_ICN = (By.XPATH, "(//a[@class='ng-star-inserted'])[1]")
DSCH_BRD_TXT = (By.XPATH, "//h2[@class='mb-0']")
DVC_LCTNS_TXT_HR = (By.XPATH, "(//h2[@class='ng-tns-c6-0'])[5]")
QSTN_CRCL_DVC_LCTNS_SCTN = (By.XPATH, "(//i[@class='fa  fa-question-circle'])[4]")
QSTN_CRCL_DVC_LCTNS_TXT = (By.XPATH, "//span[@tool-tip='Current locations of the device(s).']")
DVC_LCTNS_DRP_DWN_MN = (By.ID, "groups")
DVC_LCTNS_DRP_DWN_MN_LST = (By.XPATH, "//option[@class='ng-tns-c6-0']")


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


# 6. Click Dashboard menu icon and make sure Dashboard page reloaded
wait.until(EC.element_to_be_clickable(DSCH_BRD_ICN)).click()
dsch_brd_txt = wait.until(EC.visibility_of_element_located(DSCH_BRD_TXT)).text
print(f'Dashboard is here: "{dsch_brd_txt}"\n')
assert 'Dashboard' in dsch_brd_txt

# 7. Make sure the Device Locations block is present on the screen
dvc_lctns_txt_hr = wait.until(EC.visibility_of_element_located(DVC_LCTNS_TXT_HR)).text
print(f'Device Locations: "{dvc_lctns_txt_hr}"\n')
assert 'Device   Locations' in dvc_lctns_txt_hr

# 8. Mouse hover question mark in top right of the block and make sure tooltip appears
target = wait.until(EC.element_to_be_clickable(QSTN_CRCL_DVC_LCTNS_SCTN))
actions = ActionChains(driver)
actions.move_to_element(target)
actions.click_and_hold(target)
actions.perform()
question_mark = wait.until(EC.visibility_of_element_located(QSTN_CRCL_DVC_LCTNS_TXT))
tool_tip_text = question_mark.get_attribute('tool-tip')
print(f'Tool-tip text is here: "{tool_tip_text}"\n')
expected_text = 'Current locations of the device(s).'
actual_text = tool_tip_text
if expected_text in actual_text:
    print(f'Expected "{expected_text}", and got: "{actual_text}"\n')
else:
    print(f'Expected "{expected_text}", but got: "{actual_text}"\n')

# 9.  Make sure that click on Device Locations drop-down list is working
target = wait.until(EC.element_to_be_clickable(DVC_LCTNS_DRP_DWN_MN))
actions = ActionChains(driver)
actions.move_to_element(target)
actions.click_and_hold(target)
actions.perform()
len_gprs_drp_dwn_mn = len(wait.until(EC.presence_of_all_elements_located(DVC_LCTNS_DRP_DWN_MN_LST)))
print(f'Elements in the Drop-down menu: "{len_gprs_drp_dwn_mn}"\n')


# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()

