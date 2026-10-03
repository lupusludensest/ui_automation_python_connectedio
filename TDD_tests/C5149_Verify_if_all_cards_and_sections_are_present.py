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
DVC_ONLN = (By.CSS_SELECTOR, "div.number>span")
DVC_ONLN_TXT = (By.XPATH, "(//div[@class='card overflowhidden number-chart d-flex flex-column'])[1]")
DVC_OFFLN = (By.XPATH, "(//div[@class='body information-card'])[2]")
INVNTR = (By.XPATH, "(//div[@class='body information-card'])[3]")
ALRT_NTFCTN = (By.XPATH, "(//div[@class='body information-card'])[4]")
DT_USG = (By.XPATH, "//h6[@class='tile-title text-uppercase']")
DT_USG_DTLS = (By.XPATH, "(//h2[@class='ng-tns-c6-0'])[1]")
NTFCTNS_ALRTS = (By.XPATH, "(//h2[@class='ng-tns-c6-0'])[2]")
GRPS = (By.XPATH, "(//h2[@class='ng-tns-c6-0'])[3]")
SGNL_STRNTH = (By.XPATH, "(//h2[@class='ng-tns-c6-0'])[4]")
DVC_LCTN = (By.XPATH, "//div[@class='col-6']//h2[@class='ng-tns-c6-0']")

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

# 6. Check if all elements are present.
# 6.1. Cards: "DEVICE ONLINE", 6.2. "DEVICE OFFLINE",
# 6.3. "INVENTORY", 6.4. "ALERT/NOTIFICATION", 6.5. "DATA USAGE"
#1
expected_text = 'DEVICE ONLINE'
actual_text = wait.until(EC.presence_of_element_located((DVC_ONLN_TXT))).text
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')
#2
expected_text = 'DEVICE OFFLINE'
actual_text = wait.until(EC.presence_of_element_located((DVC_OFFLN))).text
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')
#3
expected_text = 'INVENTORY'
actual_text = wait.until(EC.presence_of_element_located((INVNTR))).text
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')
#4
expected_text = 'ALERT/NOTIFICATION'
actual_text = wait.until(EC.presence_of_element_located((ALRT_NTFCTN))).text
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')
#5
expected_text = 'DATA USAGE'
actual_text = wait.until(EC.presence_of_element_located((DT_USG))).text
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

# 7. Check if sections are present.
# 7.1 "Data Usage Details", 7.2. "Notifications/Alerts",
# 7.3. "Groups", 7.4. "Signal Strength", 7.5. "Device Location".
#1
expected_text = 'Data Usage Details'
actual_text = wait.until(EC.presence_of_element_located((DT_USG_DTLS))).text
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')
#2
expected_text = 'Notifications / Alerts'
actual_text = wait.until(EC.presence_of_element_located((NTFCTNS_ALRTS))).text
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')
#3
expected_text = 'Groups'
actual_text = wait.until(EC.presence_of_element_located((GRPS))).text
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')
#4
expected_text = 'Signal Strength'
actual_text = wait.until(EC.presence_of_element_located((SGNL_STRNTH))).text
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')
#5
expected_text = 'Device   Locations'
actual_text = wait.until(EC.presence_of_element_located((DVC_LCTN))).text
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')

# Pictures
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
# driver = webdriver.Chrome(chrome_options=options)
images = driver.find_elements(By.TAG_NAME, "img")
pics_on_page = len(images)
for image in images:
    print(image.get_attribute('src'))
print(f'There are: "{pics_on_page}" images on the page')

# Sleep to see what we have
sleep(2)

# Driver quit
driver.quit()