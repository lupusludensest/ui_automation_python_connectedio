from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from random import randint

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

# Locators
ADMIN1 = (By.CSS_SELECTOR, "tr.ng-star-inserted")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://devcloud.connectedio.com' )

# 2. Send Login e-mail
wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).clear()
wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).send_keys('vadim@mailinator.com')

# 3. Send Password
wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).clear()
wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).send_keys('manicpiano731')

# 4. Click on Login button
wait.until(EC.element_to_be_clickable(LOGIN_BTN)).click()

# 5. Click on pop-window OK button
wait.until(EC.element_to_be_clickable(POP_UP_WNDW_OK_BTN)).click()

# 6. Make sure there are at list two Admins and one User role in the list of users
expected_text = 'Admin'
actual_text = wait.until(EC.presence_of_element_located((By.XPATH, "//td[@style='text-align: left;']"))).text
assert expected_text in actual_text
print(f'Expected {expected_text}, but got: "{actual_text}" ')

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()