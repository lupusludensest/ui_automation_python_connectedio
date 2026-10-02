from behave import *

@step("Click on Filter Devices and open Search page")
def clck_on_fltr_dvcs(context):
    """
    Click on Filter Devices and open Search page
    """
    context.app.main_page.clck_on_fltr_dvcs()


@then("Make sure that only Online Devices checkbox is checked in the Search page")
def onln_dvcs_chck_box_chkd(context):
    """
    Make sure that only Online Devices checkbox is checked in the Search page
    """
    context.app.main_page.onln_dvcs_chck_box_chkd()