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
POP_UP_WNDW_OK_BTN = (By.CSS_SELECTOR, "button.swal2-confirm.btn.btn-outline-primary.btn-sm.btn-custom.swal2-styled")
USERS = (By.CSS_SELECTOR, "i.fa.fa-users")
QUICK_ACTIONS = (By.XPATH, "//button[@class='btn btn-default btn-sm dropdown-toggle dropdown-toggle']")
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
USERS_VERIFY = (By.CSS_SELECTOR, "a.text-primary.ng-star-inserted")

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

    def vrf_usr_is_hr(self, user):
        wait = WebDriverWait(self.driver, 10)
        expected_text = user
        actual_text = wait.until(EC.presence_of_element_located((By.LINK_TEXT, user))).text
        assert expected_text in actual_text
        print(f'Expected {user}, and got "{actual_text}" ')

        # Sleep to see what we have
        sleep(2)

        # Driver quit
        self.driver.quit()


