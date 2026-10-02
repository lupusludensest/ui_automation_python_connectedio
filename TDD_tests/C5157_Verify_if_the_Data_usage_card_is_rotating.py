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
DT_USG_CRD = (By.CSS_SELECTOR, "div.card.overflowhidden.number-chart.p-4")
CLLR = (By.XPATH, "(//strong[@class='ng-tns-c6-0'])[1]")
WAN = (By.XPATH, "(//strong[@class='ng-tns-c6-0'])[4]")

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

# 6. Click on the DATA USAGE card with Cellular data used
wait.until(EC.element_to_be_clickable(DT_USG_CRD)).click()

# 7. Verify that the DATA USAGE card has rotated to WAN data used and he DATA USAGE card has rotated back to Cellular data used
cllr_txt = wait.until(EC.visibility_of_element_located(CLLR)).text
wan_txt = wait.until(EC.visibility_of_element_located(WAN)).text
assert cllr_txt == 'Cellular' and wan_txt == 'WAN'
print(f'Text is here: "{cllr_txt}" or "{wan_txt}"')

# TXT_1 = (By.XPATH, "(//div[@class='card overflowhidden number-chart p-4'])[1]")
# wait.until(EC.element_to_be_clickable(TXT_1)).click()
# txt_1 = wait.until(EC.visibility_of_element_located(TXT_1)).text
# print(f'TXT_1 {txt_1}')
#
# TXT_2 = (By.XPATH, "(//div[@class='card overflowhidden number-chart p-4'])[2]")
# wait.until(EC.element_to_be_clickable(TXT_2)).click()
# txt_2 = wait.until(EC.visibility_of_element_located(TXT_2)).text
# print(f'TXT_2 {txt_2}')

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()