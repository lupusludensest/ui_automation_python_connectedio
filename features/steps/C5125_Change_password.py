from behave import *

from features.steps.env_values import resolve_env_value


@then('Go to the "Change Password" page https://devcloud.connectedio.com/profile/change-password')
def go_to_chng_pswrd_pg(context):
    """
    Hover over the Logout button at the right corner of the Header and click on the button Logout
    """
    context.app.main_page.go_to_chng_pswrd_pg()


@step("{url_is_here} is open")
def cng_pswd_url_opn(context, url_is_here):
    """
    https://devcloud.connectedio.com/profile/* is open
    """
    context.app.main_page.cng_pswd_url_opn(url_is_here)


@then('Enter the old password in the field "New Password" {old_pswd}')
def ntr_old_pswd(context, old_pswd):
    """
    Enter the old password in the field "New Password" MyUSA2016!@
    """
    context.app.main_page.ntr_old_pswd(resolve_env_value(old_pswd))


@step('Enter the old password in the field "Confirm New Password" {old_pswd}')
def cfrm_old_pswd(context, old_pswd):
    """
    Enter the old password in the field "Confirm New Password" MyUSA2016!@
    """
    context.app.main_page.cfrm_old_pswd(resolve_env_value(old_pswd))


@then('Click on the button "Save"')
def clck_on_btn_save(context):
    """
    Click on the button "Save"
    """
    context.app.main_page.clck_on_btn_save()


@step("Verify the message is displayed: Old and new password cannot be same.")
def clck_on_btn_save(context):
    """
    Verify the message is displayed: Old and new password cannot be same.
    """
    context.app.main_page.clck_on_btn_save()


@step("Verify the words {old_nw_r_nt_same} is on the page")
def old_new_r_nt_same(context, old_nw_r_nt_same):
    """
    Verify the words Old and new password cannot be same. is on the page
    """
    context.app.main_page.old_new_r_nt_same(old_nw_r_nt_same)

