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
GRPS_TXT_HR = (By.XPATH, "(//h2[@class='ng-tns-c6-0'])[3]")
QSTN_CRCL_MRK_GRPS_SCTN = (By.XPATH, "(//i[@class='fa  fa-question-circle'])[2]")
QSTN_CRCL_TL_TP_TXT = (By.XPATH, "(//span[@class='ml-2'])[1]")
NO_DT_IN_GRPS_BLCK = (By.XPATH, "(//div[@class='no-data'])[3]")
GRPS_DRP_DWN_MN = (By.ID, "more") # "(//span[@class='ng-tns-c5-3'])[3]" # "//div[@class='btn-group action-button show']" # "//button[@class='btn btn-default btn-sm dropdown-toggle dropdown-toggle']"
GRPS_DRP_DWN_MN_LST = (By.XPATH, "//div[@class='list-group']")
GRPS_TL_TIP = (By.XPATH, "//span[@tool-tip='Device(s) status based on groups.']")

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

# 7. Make sure Groups block is present on the screen
grps_txt_hr = wait.until(EC.visibility_of_element_located(GRPS_TXT_HR)).text
print(f'Groups is here: "{grps_txt_hr}"\n')
assert 'Groups' in grps_txt_hr

# 8. Mouse hover question mark in top right of the Groups block and make sure tooltip appears
target = wait.until(EC.element_to_be_clickable(QSTN_CRCL_MRK_GRPS_SCTN))
actions = ActionChains(driver)
actions.move_to_element(target)
actions.click_and_hold(target)
actions.perform()
question_mark = wait.until(EC.visibility_of_element_located(QSTN_CRCL_TL_TP_TXT))
tool_tip_text = question_mark.get_attribute('tool-tip')
print(f'Text is here: "{tool_tip_text}"\n')
expected_text = 'Device(s) status based on groups.'
actual_text = tool_tip_text
if expected_text in actual_text:
    print(f'Expected "{expected_text}", and got: "{actual_text}"\n')
else:
    print(f'Expected "{expected_text}", but got: "{actual_text}"\n')

# 9. The inscription No Data Available is in the center of Groups block
no_dt_in_grps_blck = wait.until(EC.visibility_of_element_located(NO_DT_IN_GRPS_BLCK)).text
print(f'Text is here: "{no_dt_in_grps_blck}"\n')
assert 'No Data Available' in no_dt_in_grps_blck
# is in the center of Groups block
e_grps = wait.until(EC.visibility_of_element_located(NO_DT_IN_GRPS_BLCK))
location_grps = e_grps.location
print(f'Location of "No Data Available": "{location_grps}"\n')
if {'x': 90, 'y': 1168} == location_grps:
    print(f'"No Data Available" is in the center of Groups block\n')
else:
    print(f'"No Data Available" is NOT in the center of Groups block\n')

# 10. Make sure that click on Groups drop-down list is working
target = wait.until(EC.element_to_be_clickable(GRPS_DRP_DWN_MN))
actions = ActionChains(driver)
actions.move_to_element(target)
actions.click_and_hold(target)
actions.perform()
len_gprs_drp_dwn_mn = len(wait.until(EC.presence_of_all_elements_located(GRPS_DRP_DWN_MN_LST)))
print(f'Elements in the Drop-down menu: "{len_gprs_drp_dwn_mn}"\n')

# 11. Tooltip appears when mouse hover question mark in top right of the Groups block
target = wait.until(EC.element_to_be_clickable(GRPS_TL_TIP))
actions = ActionChains(driver)
actions.move_to_element(target)
actions.click_and_hold(target)
actions.perform()
question_mark = wait.until(EC.visibility_of_element_located(GRPS_TL_TIP))
tool_tip_text = question_mark.get_attribute('tool-tip')
print(f'Text is here: "{tool_tip_text}"\n')
expected_text = 'Device(s) status based on groups.'
actual_text = tool_tip_text
if expected_text in actual_text:
    print(f'Expected "{expected_text}", and got: "{actual_text}"\n')
else:
    print(f'Expected "{expected_text}", but got: "{actual_text}"\n')


# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()