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
USERS = (By.CSS_SELECTOR, "i.fa.fa-users")
ADMIN = (By.XPATH, "//b[contains(text(), 'admin')]")
USER = (By.XPATH, "//b[contains(text(), 'user')]")
THREE_DOTS = (By.ID, "dropdownBasic1")
DELETE_BTN = (By.XPATH, "//div[@class='dropdown']//a[contains(text(), 'Delete')]")
DELETE_OK_BTN = (By.CSS_SELECTOR, "button.swal2-confirm.btn.btn-outline-primary.btn-sm.btn-custom.swal2-styled")

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

# 6. Click on Users button
wait.until(EC.element_to_be_clickable(USERS)).click()

# 7. Make sure there are at list two Admins and one User role in the list of users
expected_text = 'ADMIN'
actual_text = wait.until(EC.presence_of_element_located((ADMIN))).text
assert expected_text in actual_text
print(f'Expected "{expected_text}", and got: "{actual_text}" ')
len_admins = len(wait.until(EC.presence_of_all_elements_located((ADMIN))))
print(f'Admins: "{len_admins}", type: "{type(len_admins)}"')
if len_admins < 2:
    print(f'ADMINS < 2, NOT OK, there is: {len_admins} admin, add to 2 admins')
    # Driver quit
    driver.quit()
else:
    print(f'ADMINS >=2, OK, there are: "{len_admins}" admins')

    expected_text = 'USER'
    actual_text = wait.until(EC.presence_of_element_located((USER))).text
    assert expected_text in actual_text
    print(f'Expected "{expected_text}", and got: "{actual_text}" ')
    len_users = len(wait.until(EC.presence_of_all_elements_located((USER))))
    if len_users >= 2:
        print(f'USERS >=1, OK, there are: "{len_users}" users')
    else:
        print(f'USERS < 1, NOT OK, there are: "{len_users}" users')

    total_users_admins_before_delete = len_admins + len_users
    print(f'Total admins and users before delete: "{total_users_admins_before_delete}"')

    # 8. Choose any username with Admin or User role except yours.
    # Click on the "Settings" (three vertical dots) from the rightmost side of the user.
    wait.until(EC.element_to_be_clickable(THREE_DOTS)).click()

    # 9. Select "Delete" from the dropdown menu.
    wait.until(EC.visibility_of_element_located(DELETE_BTN)).click()

    # 10. The pop-up dialog window "Delete user" appears after clicking on the "Delete" button.
    wait.until(EC.element_to_be_clickable(DELETE_OK_BTN)).click()

    # 11. The "Users" page has opened and user is not in the list of users.
    driver.refresh()
    len_admins = len(wait.until(EC.presence_of_all_elements_located((ADMIN))))
    len_users = len(wait.until(EC.presence_of_all_elements_located((USER))))
    total_admins_users_after_delete = len_admins + len_users
    if total_users_admins_before_delete - total_admins_users_after_delete == 1:
        print(f'Delete is OK: "{total_users_admins_before_delete}" - "{total_admins_users_after_delete}" = "{total_users_admins_before_delete - total_admins_users_after_delete}"')
    else:
        print(f'Delete is not OK')
    print(f'Total admins and users after delete: "{total_admins_users_after_delete}"')

    # Sleep to see what we have
    sleep(2)

    # Driver quit
    driver.quit()