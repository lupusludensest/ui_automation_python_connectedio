from behave import *

@then("Click on the INVENTORY card")
def clck_on_invntr_elmnt(context):
    """
    Click on the INVENTORY card
    """
    context.app.main_page.clck_on_invntr_elmnt()


@step("Inventory status in FILTERS field")
def invntr_sts_hr(context):
    """
    Inventory status in FILTERS field
    """
    context.app.main_page.invntr_sts_hr()