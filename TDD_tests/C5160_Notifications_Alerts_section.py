from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
LOGIN_EMAIL = (By.XPATH, "//input[@placeholder='Email address']")
LOGIN_PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
LOGIN_BTN = (By.CSS_SELECTOR, "button.btn.btn-primary.text-uppercase.w-100.font-weight-bold.gradient-btn.shadow-1.border-0")
POP_UP_WNDW_OK_BTN = (By.XPATH, "//div[@class='swal2-actions']//button[@class='swal2-confirm btn btn-outline-primary btn-sm btn-custom swal2-styled']")
DT_USG_CRD = (By.CSS_SELECTOR, "div.card.overflowhidden.number-chart.p-4")
CLLR = (By.XPATH, "(//strong[@class='ng-tns-c6-0'])[1]")
WAN = (By.XPATH, "(//strong[@class='ng-tns-c6-0'])[4]")
DSCH_BRD_ICN = (By.XPATH, "(//a[@class='ng-star-inserted'])[1]")
DSCH_BRD_TXT = (By.XPATH, "//h2[@class='mb-0']")
NTFCTNS_ALRTS_TXT = (By.XPATH, "(//div[@class='card dashboard-card notification-card'])")
NTFCTNS_ALRTS_TL_TIP = (By.XPATH, "//span[@tool-tip='Alerts related to device(s)/group(s).']")
CLCK_ON_GRPS_TB = (By.XPATH, "(//a[@class='nav-link'])[5]")
DVC_GRY = (By.XPATH, "(//li[@class='nav-item ng-star-inserted'])[4]")
NO_DT_WHEN_GRPS = (By.XPATH, "(//div[@class='no-data'])[2]")
CLCK_ON_DVC_TB = (By.XPATH, "(//li[@class='nav-item ng-star-inserted'])[4]")
NO_DT_WHEN_DVC = (By.XPATH, "(//div[@class='no-data'])[2]")

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


# 7. Make sure Notifications Alerts block is present on the screen
ntfctbs_alrts_txt = wait.until(EC.visibility_of_element_located(NTFCTNS_ALRTS_TXT)).text
print(f'Notifications / Alerts is here: "{ntfctbs_alrts_txt}"\n')
assert 'Notifications / Alerts' in ntfctbs_alrts_txt


# 8. Hover over question mark in top right of the block and make sure tooltip appears
target = wait.until(EC.element_to_be_clickable(NTFCTNS_ALRTS_TL_TIP))
actions = ActionChains(driver)
actions.move_to_element(target)
actions.click_and_hold(target)
actions.perform()
question_mark = wait.until(EC.visibility_of_element_located(NTFCTNS_ALRTS_TL_TIP))
tool_tip_text = question_mark.get_attribute('tool-tip')
print(f'Text is here: "{tool_tip_text}"\n')
expected_text = 'Alerts related to device(s)/group(s).'
actual_text = tool_tip_text
if expected_text in actual_text:
    print(f'Expected "{expected_text}", and got: "{actual_text}"\n')
else:
    print(f'Expected "{expected_text}", but got: "{actual_text}"\n')


# 9. Make sure that click on column header Groups makes it active by moving underscore sign = 0px none to it
wait.until(EC.element_to_be_clickable(CLCK_ON_GRPS_TB)).click()
undescore_line =  wait.until(EC.visibility_of_element_located(CLCK_ON_GRPS_TB)).value_of_css_property("border-bottom")
print(f'Underscore symbol: "{undescore_line}"\n')
assert '0px none' in undescore_line
expected_text = '0px none'
actual_text = undescore_line
if expected_text in actual_text:
    print(f'Expected "{expected_text}", and got: "{actual_text}"\n')
else:
    print(f'Expected "{expected_text}", but got: "{actual_text}"\n')


# 10. Verify Device inactive column highlighted grey = 128, 128, 128, 1 when hover over it and hold
target = wait.until(EC.element_to_be_clickable(DVC_GRY))
actions = ActionChains(driver)
actions.move_to_element(target)
actions.click_and_hold(target)
actions.perform()
question_mark = wait.until(EC.visibility_of_element_located(DVC_GRY))
gb_inctv_clmn =  wait.until(EC.visibility_of_element_located(DVC_GRY)).value_of_css_property("color")
assert '128, 128, 128, 1' in gb_inctv_clmn
expected_text = '128, 128, 128, 1'
actual_text = gb_inctv_clmn
if expected_text in actual_text:
    print(f'Expected "{expected_text}", and got: "{actual_text}"\n')
else:
    print(f'Expected "{expected_text}", but got: "{actual_text}"\n')


# 11. The inscription No Data Available is in the center and does not shift when switching columns
# Groups is active=undescored and verify text No Data Available is here
no_dt_when_grps = wait.until(EC.visibility_of_element_located(NO_DT_WHEN_GRPS)).text
print(f'Text is here: "{no_dt_when_grps}"\n')
assert 'No Data Available' in no_dt_when_grps


# Click on Device and verify text No Data Available is here
wait.until(EC.element_to_be_clickable(CLCK_ON_DVC_TB)).click()
no_dt_when_dvc = wait.until(EC.visibility_of_element_located(NO_DT_WHEN_DVC)).text
print(f'Text is here: "{no_dt_when_dvc}"\n')
assert 'No Data Available' in no_dt_when_dvc


# Locations of the No Data Available if Groups is active=undescored 0px none
e_grps = wait.until(EC.visibility_of_element_located(NO_DT_WHEN_GRPS))
location_grps = e_grps.location
size_grps = e_grps.size
print(f'Groups is active=undescored location: "{location_grps}"\n')
print(f'Groups is active=undescored size: "{size_grps}"\n')


# Locations of the No Data Available if Device is active=undescored
e_dvc = wait.until(EC.visibility_of_element_located(NO_DT_WHEN_DVC))
location_dvc = e_dvc.location
size_dvc = e_dvc.size
print(f'Device is active=undescored location: "{location_dvc}"\n')
print(f'Device is active=undescored size: "{size_dvc}"\n')


# Verify the inscription No Data Available is in the center and does not shift when switching columns
if location_grps == location_dvc and size_grps == size_dvc:
    print(f'Ok, because "{location_grps}"="{location_dvc}" and\n "{size_grps}"="{size_dvc}"\n')

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()