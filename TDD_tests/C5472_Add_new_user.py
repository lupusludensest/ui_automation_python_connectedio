from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from random import randint

driver = webdriver.Chrome()
driver.maximize_window()

# Locators
LOGIN_EMAIL = (By.XPATH, "//input[@placeholder='Email address']")
LOGIN_PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
LOGIN_BTN = (By.CSS_SELECTOR, "button.btn.btn-primary.text-uppercase.w-100.font-weight-bold.gradient-btn.shadow-1.border-0")
# POP_UP_WNDW_OK_BTN = (By.CSS_SELECTOR, "button.swal2-confirm.btn.btn-outline-primary.btn-sm.btn-custom.swal2-styled")
POP_UP_WNDW_OK_BTN = (By.XPATH, "//div[@class='swal2-actions']//button[@class='swal2-confirm btn btn-outline-primary btn-sm btn-custom swal2-styled']")
# USERS = (By.CSS_SELECTOR, "i.fa.fa-users")
# USERS = (By.XPATH, "(//a[@class='ng-star-inserted'])[4]")
# USERS = (By.XPATH, "(//i[@class='fa fa-users'])[1]")
USERS = (By.XPATH, "(//li[@class='ng-star-inserted'])[5]")
# QUICK_ACTIONS = (By.XPATH, "//button[@class='btn btn-default btn-sm dropdown-toggle dropdown-toggle']")
QUICK_ACTIONS = (By.XPATH, "//div[@class='btn-group action-button dropdown']//span[contains(text(), 'Quick actions')]")
ADD_MENU =  (By.CSS_SELECTOR, "i.fa.fa-user-plus")
FIRST_NAME = (By.XPATH, "//input[@formcontrolname='firstName']")
LAST_NAME = (By.XPATH, "//input[@formcontrolname='lastName']")
EMAIL = (By.XPATH, "//input[@formcontrolname='email']")
TELEPHONE = (By.XPATH, "//input[@formcontrolname='telephone']")
SELECT_ROLE = (By.ID, "role")
ADDRESS_1 = (By.XPATH, "//input[@formcontrolname='address1']")
ADDRESS_2 = (By.XPATH, "//input[@formcontrolname='address2']")
CITY = (By.XPATH, "//input[@formcontrolname='city']")
ZIP_CODE = (By.XPATH, "//input[@formcontrolname='zipCode']")
COUNTRY = (By.CSS_SELECTOR, "select.form-control.ng-touched.ng-dirty.ng-valid")
STATE = (By.XPATH, "//select[@formcontrolname='state']")
ADD_BTN = (By.CSS_SELECTOR, "button.btn.btn-sm.btn-primary.px-4.py-2.text-uppercase")
TEXT_HR = (By.XPATH, "//td[@style='text-align: left;']")
USERS_VERIFY = (By.CSS_SELECTOR, "a.text-primary.ng-star-inserted")

# Explicit wait
wait = WebDriverWait(driver, 15)

# 1. Open the url
driver.get( 'https://devcloud.connectedio.com' )

# 2. Send Login e-mail
wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).clear()
wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).send_keys('gurovvic@gmail.com') # vadim@mailinator.com

# 3. Send Password
wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).clear()
wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).send_keys('MyUSA2016!@')  # manicpiano731

# 4. Click on Login button
wait.until(EC.element_to_be_clickable(LOGIN_BTN)).click()

# 5. Click on pop-window OK button
wait.until(EC.element_to_be_clickable(POP_UP_WNDW_OK_BTN)).click()

# 6. Click on Users button
wait.until(EC.element_to_be_clickable(USERS)).click()

# 7. Click on Quick Actions button
wait.until(EC.element_to_be_clickable(QUICK_ACTIONS)).click()

# 8. Click on Add button
wait.until(EC.element_to_be_clickable(ADD_MENU)).click()

# 9. Fill out the First Name field
wait.until(EC.presence_of_element_located(FIRST_NAME)).clear()
wait.until(EC.presence_of_element_located(FIRST_NAME)).send_keys('Roman')

# 10. Fill out the Last Name field
wait.until(EC.presence_of_element_located(LAST_NAME)).clear()
wait.until(EC.presence_of_element_located(LAST_NAME)).send_keys('Ivanov')

# Generators of password, name and email
password = str(randint(999, 9999))
name = 'name' + password
email = (name + '@sample.com')

# 11. Fill out the Email field
wait.until(EC.presence_of_element_located(EMAIL)).clear()
wait.until(EC.presence_of_element_located(EMAIL)).send_keys(email)

# 12. Fill out the Telephone field
wait.until(EC.presence_of_element_located(TELEPHONE)).clear()
wait.until(EC.presence_of_element_located(TELEPHONE)).send_keys('7895678956')

# 13. Choose admin in the drop-down menu
element = wait.until(EC.visibility_of_element_located((SELECT_ROLE)))
select = Select(element)
select.select_by_value("admin")

# 14. Fill out the Adress1 field
wait.until(EC.presence_of_element_located(ADDRESS_1)).clear()
wait.until(EC.presence_of_element_located(ADDRESS_1)).send_keys('1933, 84 street')

# 14. Fill out the Adress2 field
wait.until(EC.presence_of_element_located(ADDRESS_2)).clear()
wait.until(EC.presence_of_element_located(ADDRESS_2)).send_keys('Just test')

# 15. Fill out the City field
wait.until(EC.presence_of_element_located(CITY)).clear()
wait.until(EC.presence_of_element_located(CITY)).send_keys('Brooklyn')

# 16. Fill out the Zip Code field
wait.until(EC.presence_of_element_located(ZIP_CODE)).clear()
wait.until(EC.presence_of_element_located(ZIP_CODE)).send_keys('11214')

# 17. Choose Select Country in the drop-down menu United States
wait.until(EC.element_to_be_clickable(COUNTRY)).click()
wait.until(EC.presence_of_element_located(COUNTRY)).send_keys('United States')

# 18. Choose Select State in the drop-down menu New York
wait.until(EC.element_to_be_clickable(STATE)).click()
wait.until(EC.presence_of_element_located(STATE)).send_keys('New York')

# 19. Click on Add button
wait.until(EC.element_to_be_clickable(ADD_BTN)).click()

# 20. Verify Verification Pending is here
expected_text = 'Verification Pending'
actual_text = wait.until(EC.presence_of_element_located((TEXT_HR))).text
print(f'Actual text: "{actual_text}"')
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()