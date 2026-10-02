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
INVNTR_ELMNT = (By.CSS_SELECTOR, "div.card.overflowhidden.number-chart.d-flex.flex-column")
INVNTR_TXT = (By.CSS_SELECTOR, "span.pr-2")

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

# 6. Click on the INVENTORY  card
invntr_elmnt = (wait.until(EC.presence_of_all_elements_located(INVNTR_ELMNT)))[2]
invntr_elmnt.click()

# 7. Verify https://devcloud.connectedio.com/devices is open
expected_text = 'https://devcloud.connectedio.com/devices'
actual_text = driver.current_url
assert expected_text in actual_text
if expected_text == actual_text:
    print(f'Expected "{expected_text}", and got: "{actual_text}" ')
else:
    print(f'Expected "{expected_text}", but got: "{actual_text}" ')

# 8. Verify Inventory is here
expected_text = 'Inventory'
actual_text = wait.until(EC.presence_of_element_located((INVNTR_TXT))).text
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()