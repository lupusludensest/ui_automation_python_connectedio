from behave import *

@then("Make sure there are at least two Admins and one User role in the list of users")
def admns_n_usrs(context):
    """
    Make sure there are at least two Admins and one User role in the list of users
    """
    context.app.main_page.admns_n_usrs()


@then("Click on the Settings 'three vertical' dots from the rightmost side of the user")
def take_usr_t_dlt(context):
    """
    Click on the Settings (three vertical dots) from the rightmost side of the user
    """
    context.app.main_page.take_usr_t_dlt()


@then("Choose and click on 'Delete' from the dropdown menu")
def dlt_drp_dwn_mn(context):
    """
    Choose and chlick on 'Delete' from the dropdown menu
    """
    context.app.main_page.dlt_drp_dwn_mn()


@then("Confirm action by clicking OK button on the pop-up dialog window")
def cnfrm_dlt(context):
    """
    Confirm action by clicking OK button on the pop-up dialog window
    """
    context.app.main_page.cnfrm_dlt()


@then("Then Verify that there is for one user less after deleting")
def vrf_usr_dltd(context):
    """
    Then Verify that there is for one user less after deleting
    """
    context.app.main_page.vrf_usr_dltd()