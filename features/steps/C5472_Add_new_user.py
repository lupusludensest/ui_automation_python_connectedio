from behave import *

@given("Loginpage")
def open_homepage(context):
    """
    Loginpage
    """
    context.app.main_page.open_page()

@then("Login with the given credentials")
def lgn_w_gn_crdntls(context):
    """
    Login with the given credentials
    """
    context.app.main_page.lgn_w_gn_crdntls()

@then("Click on the Users button")
def clck_usrs_btn(context):
    """
    Click on the Users button
    """
    context.app.main_page.clck_usrs_btn()

@then("Click on the Quick actions button")
def clck_qck_actns_btn(context):
    """
    Click on the Quick actions button
    """
    context.app.main_page.clck_qck_actns_btn()

@then("Select Add in the drop-down menu")
def slct_add_drp_dwn_mn(context):
    """
    Select Add in the drop-down menu
    """
    context.app.main_page.slct_add_drp_dwn_mn()

@then("Fill out the required fields")
def fll_rqrd_flds(context):
    """
    Fill out the required fields
    """
    context.app.main_page.fll_rqrd_flds()

@step("Click on the Add button")
def clck_n_add_btn(context):
    """
    Click on the Add button
    """
    context.app.main_page.clck_n_add_btn()

@then("Verify the words {text_hr} is here")
def vrf_usr_is_hr(context, text_hr):
    """
    Verify the word Verification Pending is here
    """
    context.app.main_page.vrf_usr_is_hr(text_hr)