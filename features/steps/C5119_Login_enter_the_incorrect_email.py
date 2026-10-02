from behave import *

@then('Enter valid, but the incorrect email address in the line "Email address" {email}')
def entr_vld_wrng_eml(context, email):
    """
    Enter valid, but the incorrect email address in the line "Email address"'
    """
    context.app.main_page.entr_vld_wrng_eml(email)

@then('Enter the correct password in the line "Password" {pswd}')
def entr_vld_crct_pswd(context, pswd):
    """
    Enter the correct password in the line "Password" manicpiano731
    """
    context.app.main_page.entr_vld_crct_pswd(pswd)

@then("Verify {vrf_invld_lgn_r_pswd_hr} is on login pop_up")
def vrf_invld_lgn_r_pswd_hr(context, vrf_invld_lgn_r_pswd_hr):
    """
    Verify Invalid Login or Password is on login pop_up
    """
    context.app.main_page.vrf_invld_lgn_r_pswd_hr(vrf_invld_lgn_r_pswd_hr)