from behave import *

@then('Click on DEVICE ONLINE card')
def clck_on_dvc_nln(context):
    """
    Click on "DEVICE ONLINE" card
    """
    context.app.main_page.clck_on_dvc_nln()


@then("Words {dvc_mngmnt_ptrl_hr} are here on the page")
def dvc_mngmnt_ptrl_hr(context, dvc_mngmnt_ptrl_hr):
    """
    Words Device Management Portal are here on the page
    """
    context.app.main_page.dvc_mngmnt_ptrl_hr(dvc_mngmnt_ptrl_hr)


@then("Word {onln_hr} is here on the page")
def onln_hr(context, onln_hr):
    """
    Word Online is here on the page
    """
    context.app.main_page.onln_hr(onln_hr)