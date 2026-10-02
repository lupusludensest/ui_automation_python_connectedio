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
# CLCK_TRNGL = (By.CSS_SELECTOR, "i.fas.fa-chevron-right")
CLCK_TRNGL = (By.XPATH, "//button[@class='d-block btn-togglr']")
USR_NM = (By.CSS_SELECTOR, "a.dropdown-toggle.user-name")
CHNG_PSWD = (By.XPATH, "//i[@class='fas fa-unlock-alt']")
NW_VLD_PSWD = (By.XPATH, "//input[@placeholder='New Password']")
CNFRM_NW_VLD_PSWD = (By. XPATH, "//input[@placeholder='Confirm New Password']")
SV_BTN = (By.CSS_SELECTOR, "i.fa.fa-save.mr-1")
SCSS_TXT_HR = (By.CSS_SELECTOR, "span.alert.w-100.alert-warning")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://devcloud.connectedio.com' )

# 2. Send Login e-mail
wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).clear()
wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).send_keys('gurovvic@gmail.com') # vadim@mailinator.com

# 3. Send Password
wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).clear()
wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).send_keys('MyUSA2016!@')

# 4. Click on Login button
wait.until(EC.element_to_be_clickable(LOGIN_BTN)).click()

# 5. Click on pop-window OK button
wait.until(EC.element_to_be_clickable(POP_UP_WNDW_OK_BTN)).click()

# 6. Click on triangle to enter the user
target = wait.until(EC.element_to_be_clickable(CLCK_TRNGL))
actions = ActionChains(driver)
actions.move_to_element(target)
sleep(2)
actions.click(target)
actions.perform()

# 7. Click on the User name in the Sidebar menu
wait.until(EC.element_to_be_clickable(USR_NM)).click()

# 8. Click on the Change Password button
wait.until(EC.element_to_be_clickable(CHNG_PSWD)).click()

# 9. Verify https://devcloud.connectedio.com/profile/change-password is open
expected_text = 'https://devcloud.connectedio.com/profile/change-password'
actual_text = driver.current_url
assert expected_text in actual_text
if expected_text == actual_text:
    print(f'Expected "{expected_text}", and got: "{actual_text}" ')
else:
    print(f'Expected "{expected_text}", but got: "{actual_text}" ')

# 10. Enter the old password in the field "New Password" MyUSA2016!@
wait.until(EC.presence_of_element_located(NW_VLD_PSWD)).clear()
wait.until(EC.presence_of_element_located(NW_VLD_PSWD)).send_keys('MyUSA2016!@')

# 11. Enter the same old password in the field "Confirm New Password"
wait.until(EC.visibility_of_element_located(CNFRM_NW_VLD_PSWD)).clear()
wait.until(EC.visibility_of_element_located(CNFRM_NW_VLD_PSWD)).send_keys('MyUSA2016!@')

# 12. Click on the button "Save"
wait.until(EC.element_to_be_clickable(SV_BTN)).click()

# 13. Verify the message is displayed: "Old and new password cannot be same."
expected_text = 'Old and new password cannot be same.'
actual_text = wait.until(EC.element_to_be_clickable(SCSS_TXT_HR)).text
assert expected_text in actual_text
if expected_text == actual_text:
    print(f'Expected "{expected_text}", and got: "{actual_text}" ')
else:
    print(f'Expected "{expected_text}", but got: "{actual_text}" ')

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()