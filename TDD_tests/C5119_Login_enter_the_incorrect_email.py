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
# POP_UP_WNDW_OK_BTN = (By.CSS_SELECTOR, "button.swal2-confirm.btn.btn-outline-primary.btn-sm.btn-custom.swal2-styled")
POP_UP_WNDW_OK_BTN = (By.XPATH, "//div[@class='swal2-actions']//button[@class='swal2-confirm btn btn-outline-primary btn-sm btn-custom swal2-styled']")
INVLD_LGN_PSWRD_HR = (By.XPATH, "//div[contains(text(), 'Invalid Login or Password')]")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://devcloud.connectedio.com' )

# 2. Send valid but wrong Login e-mail
wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).clear()
wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).send_keys('gurovvic_wrong@gmail.com') # vadim_wrong@mailinator.com

# 3. Send Correct Password
wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).clear()
wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).send_keys('MyUSA2016!@') # manicpiano731

# 4. Click on Login button
wait.until(EC.element_to_be_clickable(LOGIN_BTN)).click()

# 5. Verify Invalid Login or Password is here
expected_text = 'Invalid Login or Password'
actual_text = wait.until(EC.presence_of_element_located((INVLD_LGN_PSWRD_HR))).text
print(actual_text)
assert expected_text in actual_text
print(f'Expected "{expected_text}", but got: "{actual_text}" ')

# Sleep to see what we have
sleep(2)

# Driver quit
# driver.quit()
