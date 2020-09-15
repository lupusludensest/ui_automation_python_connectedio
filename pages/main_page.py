from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# Locators
LOGIN_EMAIL = (By.XPATH, "//input[@placeholder='Email address']")
LOGIN_PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
LOGIN_BTN = (By.CSS_SELECTOR, "button.btn.btn-primary.text-uppercase.w-100.font-weight-bold.gradient-btn.shadow-1.border-0")
# POP_UP_WNDW_OK_BTN = (By.CSS_SELECTOR, "button.swal2-confirm.btn.btn-outline-primary.btn-sm.btn-custom.swal2-styled")
POP_UP_WNDW_OK_BTN = (By.XPATH, "//div[@class='swal2-actions']//button[@class='swal2-confirm btn btn-outline-primary btn-sm btn-custom swal2-styled']")
USERS = (By.CSS_SELECTOR, "i.fa.fa-users")
# QUICK_ACTIONS = (By.XPATH, "//button[@class='btn btn-default btn-sm dropdown-toggle dropdown-toggle']")
QUICK_ACTIONS = (By.XPATH, "//div[@class='btn-group action-button dropdown']//span[contains(text(), 'Quick actions')]")
ADD_MENU = (By.CSS_SELECTOR, "i.fa.fa-user-plus")
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
ADMIN = (By.XPATH, "//b[contains(text(), 'admin')]")
USER = (By.XPATH, "//b[contains(text(), 'user')]")
THREE_DOTS = (By.ID, "dropdownBasic1")
DELETE_BTN = (By.XPATH, "//div[@class='dropdown']//a[contains(text(), 'Delete')]")
DELETE_OK_BTN = (By.CSS_SELECTOR, "button.swal2-confirm.btn.btn-outline-primary.btn-sm.btn-custom.swal2-styled")
INVLD_LGN_PSWRD_HR = (By.XPATH, "//div[contains(text(), 'Invalid Login or Password')]")
CLCK_TRNGL = (By.CSS_SELECTOR, "i.fas.fa-chevron-right")
USR_NM = (By.CSS_SELECTOR, "a.dropdown-toggle.user-name")
LGT_BTN = (By.CSS_SELECTOR, "i.fas.fa-power-off")
CLCK_LGT = (By.CSS_SELECTOR, "a.icon-menu.d-none.d-sm-block")

class MainPage(Page):

    # Add new user
    def lgn_w_gn_crdntls(self):
        wait = WebDriverWait(self.driver, 10)
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

    def clck_usrs_btn(self):
        wait = WebDriverWait(self.driver, 10)
        # 6. Click on Users button
        wait.until(EC.element_to_be_clickable(USERS)).click()

    def clck_qck_actns_btn(self):
        wait = WebDriverWait(self.driver, 10)
        # 7. Click on Quick Actions button
        wait.until(EC.element_to_be_clickable(QUICK_ACTIONS)).click()

    def slct_add_drp_dwn_mn(self):
        wait = WebDriverWait(self.driver, 10)
        # 8. Click on Add button
        wait.until(EC.element_to_be_clickable(ADD_MENU)).click()

    def fll_rqrd_flds(self):
        wait = WebDriverWait(self.driver, 10)
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

    def clck_n_add_btn(self):
        wait = WebDriverWait(self.driver, 10)
        # 19. Click on Add button
        wait.until(EC.element_to_be_clickable(ADD_BTN)).click()

    def vrf_usr_is_hr(self, text_hr):
        wait = WebDriverWait(self.driver, 10)
        expected_text = text_hr
        actual_text = wait.until(EC.presence_of_element_located((TEXT_HR))).text
        assert expected_text in actual_text
        print(f'Expected {text_hr}, and got "{actual_text}" ')

        # Sleep to see what we have
        sleep(2)

        # Driver quit
        self.driver.quit()

    def admns_n_usrs(self):
        # 7. Make sure there are at list two Admins and one User role in the list of users
        wait = WebDriverWait(self.driver, 15)
        expected_text = 'ADMIN'
        actual_text = wait.until(EC.presence_of_element_located((ADMIN))).text
        assert expected_text in actual_text
        print(f'Expected {expected_text}, but got: "{actual_text}" ')
        len_admins = len(wait.until(EC.presence_of_all_elements_located((ADMIN))))
        if len_admins >= 2:
            print(f'ADMINS >=2, OK, there are: {len_admins} admins')
        else:
            print(f'ADMINS !>=2, NOT OK, there are: {len_admins}')

        expected_text = 'USER'
        actual_text = wait.until(EC.presence_of_element_located((USER))).text
        assert expected_text in actual_text
        print(f'Expected {expected_text}, but got: "{actual_text}" ')
        len_users = len(wait.until(EC.presence_of_all_elements_located((USER))))
        if len_users >= 2:
            print(f'USERS >=1, OK, there are: {len_users} users')
        else:
            print(f'USERS !>=1, NOT OK, there are: {len_users} users')

        total_users_admins_before_delete = len_admins + len_users
        print(f'Total admins and users before delete: {total_users_admins_before_delete}')

    def take_usr_t_dlt(self):
        # 8. Choose any username with Admin or User role except yours.
        # Click on the "Settings" (three vertical dots) from the rightmost side of the user.
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(THREE_DOTS)).click()

    def dlt_drp_dwn_mn(self):
        # 9. Select "Delete" from the dropdown menu.
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.visibility_of_element_located(DELETE_BTN)).click()

    def cnfrm_dlt(self):
        # 10. The pop-up dialog window "Delete user" appears after clicking on the "Delete" button.
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(DELETE_OK_BTN)).click()

    def vrf_usr_dltd(self):
        # 11. The "Users" page has opened and user is not in the list of users.
        wait = WebDriverWait(self.driver, 15)
        len_admins = len(wait.until(EC.presence_of_all_elements_located((ADMIN))))
        len_users = len(wait.until(EC.presence_of_all_elements_located((USER))))
        total_users_admins_before_delete = len_admins + len_users
        self.driver.refresh()
        len_admins = len(wait.until(EC.presence_of_all_elements_located((ADMIN))))
        len_users = len(wait.until(EC.presence_of_all_elements_located((USER))))
        total_admins_users_after_delete = len_admins + len_users
        if total_users_admins_before_delete - total_admins_users_after_delete == 1:
            print(
                f'Delete is OK: {total_users_admins_before_delete} - {total_admins_users_after_delete} = {total_users_admins_before_delete - total_admins_users_after_delete}')
        else:
            print(f'Delete is not OK')
        print(f'Total admins and users after delete: {total_admins_users_after_delete}')

        # Sleep to see what we have
        sleep(2)

        # Driver quit
        self.driver.quit()

    def entr_vld_wrng_eml(self, email):
        # 1. Enter valid, but the incorrect email address in the line "Email address"
        wait = WebDriverWait(self.driver, 15)
        # Send Login e-mail
        wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).clear()
        wait.until(EC.presence_of_element_located(LOGIN_EMAIL)).send_keys(email)

    def entr_vld_crct_pswd(self, pswd):
        # 2. Send Correct Password
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).clear()
        wait.until(EC.presence_of_element_located(LOGIN_PASSWORD)).send_keys(pswd)
        # Click on Login button
        wait.until(EC.element_to_be_clickable(LOGIN_BTN)).click()

    def vrf_invld_lgn_r_pswd_hr(self, expected_text):
        # 3. Verify Invalid Login or Password is here
        wait = WebDriverWait(self.driver, 15)
        actual_text = wait.until(EC.presence_of_element_located((INVLD_LGN_PSWRD_HR))).text
        print(actual_text)
        assert expected_text in actual_text
        print(f'Expected {expected_text}, but got: "{actual_text}" ')

        # Sleep to see what we have
        sleep(2)

        # Driver quit
        self.driver.quit()

    def clck_usr_nm(self):
        # 6. Click on triangle to enter the user
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(CLCK_TRNGL))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        sleep(2)
        actions.click(target)
        actions.perform()

        # 7. Click on the User name in the Sidebar menu
        wait.until(EC.element_to_be_clickable(USR_NM)).click()

    def clck_lgt_btn(self):
        # 8. Hover over the "Logout" button in the dropdown menu and click on the button "Logout"
        wait = WebDriverWait(self.driver, 15)
        wait.until(EC.element_to_be_clickable(LGT_BTN)).click()
        self.driver.refresh()

    def vrf_lgn_pg_opn(self, url):
        # 9. Verify https://devcloud.connectedio.com is open
        expected_text = url
        actual_text = self.driver.current_url
        assert expected_text in actual_text
        if expected_text == actual_text:
            print(f'Expected {expected_text}, and got: "{actual_text}" ')
        else:
            print(f'Expected {expected_text}, but got: "{actual_text}" ')

        # Sleep to see what we have
        sleep(2)

        # Driver quit
        self.driver.quit()

    def clck_hdr_lgt_btn(self):
        # Hover over the "Logout" button at the right corner of the Header and click on the button "Logout"
        wait = WebDriverWait(self.driver, 15)
        target = wait.until(EC.element_to_be_clickable(CLCK_LGT))
        actions = ActionChains(self.driver)
        actions.move_to_element(target)
        actions.click(target)
        actions.perform()

        # Sleep to see what we have
        sleep(2)

        # Driver quit
        self.driver.quit()