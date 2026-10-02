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
DSCH_BRD_ICN = (By.XPATH, "(//a[@class='ng-star-inserted'])[1]")
DSCH_BRD_TXT = (By.XPATH, "//h2[@class='mb-0']")
DVC_ONLN_ICN = (By.XPATH, "(//div[@class='card overflowhidden number-chart d-flex flex-column'])[1]")
FLTR_DVC_FUNNEL = (By.XPATH, "//i[@class='fa fa-filter']")
CHCK_BX_DVC_ONLN = (By.NAME, "checkbox1")
CHCK_BX_DVC_OFFLN =(By.XPATH, "//span[contains(text(), 'Offline Devices')]")
CHCK_BX_INVENTORY = (By.XPATH, "//span[contains(text(), 'Inventory')]")

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

# 7. Сlick on Device online and open Devices page
wait.until(EC.element_to_be_clickable(DVC_ONLN_ICN)).click()

# 8. Click on Filter Devices and open Search page
wait.until(EC.element_to_be_clickable(FLTR_DVC_FUNNEL)).click()

# 9. Make sure that only Online Devices checkbox is checked in the Search page
onln_dvc_chck_chckd = wait.until(EC.presence_of_element_located(CHCK_BX_DVC_ONLN)).is_selected()
print(f'Online Devices checkbox is checked: "{onln_dvc_chck_chckd}"')
# Make sure Offline Devices checkbox is not checked in the Search page
offln_dvc_chck_chckd = wait.until(EC.presence_of_element_located(CHCK_BX_DVC_OFFLN)).is_selected()
print(f'Offline Devices checkbox is checked: "{offln_dvc_chck_chckd}"')
# Make sure Inventory checkbox is not checked in the Search page
inventory_chckd = wait.until(EC.presence_of_element_located(CHCK_BX_INVENTORY)).is_selected()
print(f'Inventory checkbox is checked: "{inventory_chckd}"')

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()