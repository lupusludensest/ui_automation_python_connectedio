from behave import *

@then("Click on the DATA USAGE card with Cellular data used")
def clck_on_dt_usg(context):
    """
    Click on the DATA USAGE card with Cellular data used
    """
    context.app.main_page.clck_on_dt_usg()


@then("Verify that the DATA USAGE card has rotated to WAN data used and he DATA USAGE card has rotated back to Cellular data used")
def cllr_or_wan_txts_hr(context):
    """
    Verify that the DATA USAGE card has rotated to WAN data used and he DATA USAGE card has rotated back to Cellular data used
    """
    context.app.main_page.cllr_or_wan_txts_hr()