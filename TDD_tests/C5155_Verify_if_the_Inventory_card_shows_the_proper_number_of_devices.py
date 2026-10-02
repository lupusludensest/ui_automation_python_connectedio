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
# DVC_INVNTR = (By.XPATH, "(//div[@class='number'])[2]")
DVC_INVNTR = (By.CSS_SELECTOR, "div.number>span")
NO_DATA = (By.XPATH, "//div[@class='no-data']")
DVCS_TBL_EMPT = (By.XPATH, "(//div[@class='fancy-checkbox devicelist-checkbox select-all'])[2]")

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

# 6. Pay attention to the number of devices on the "INVENTORY" card
sleep(2)
txt_frm_invntr = (wait.until(EC.visibility_of_all_elements_located(DVC_INVNTR)))[2].text
print(f'Devices inventory: "{txt_frm_invntr}"')

# 7.1 Click on INVENTORY card
(wait.until(EC.visibility_of_all_elements_located(DVC_INVNTR)))[1].click()

# # 7.2 And if there are no data in Device Management Portal verify text No Data Available is here
no_data_available = wait.until(EC.element_to_be_clickable(NO_DATA)).text

# 7.3 If txt_frm_dvc_offln = 0 and no_data_available = 'No Data Available' stop and exit program
if txt_frm_invntr == '0' and no_data_available == 'No Data Available':
    print(f'Number of devices from INVENTORY element: "{txt_frm_invntr}", type: "{type(txt_frm_invntr)}";\nNo data avalable is here: "{no_data_available}", type "{type(no_data_available)}".')
    # Driver quit
    driver.quit()
    # break
else:

    # 8. Count the number of devices with offline status on the Devices page
    len_tbl = len(wait.until(EC.presence_of_all_elements_located(DVCS_TBL_EMPT)))
    print(f'Quantity of the strings in the devices table: "{len_tbl}"')

    # 9. Verify if the number of devices on the DEVICE ONLINE card should match the number of devices with online status on the Devices page
    assert txt_frm_invntr in str(len_tbl)
    print(f'Expected "{txt_frm_invntr}", and got: "{str(len_tbl)}" ')

    # Sleep to see what we have
    sleep(2)
    #
    # Driver quit
    driver.quit()