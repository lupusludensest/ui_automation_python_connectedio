from behave import *

@then("Click on ALERT/NOTIFICATION card")
def clck_on_alrt_ntfctn_crd(context):
    """
    Click on ALERT/NOTIFICATION card
    """
    context.app.main_page.clck_on_alrt_ntfctn_crd()


@then("Verify Alert Dashboard words on the page")
def alrt_dshbrd_wrds_on_pg(context):
    """
    Verify Alert Dashboard words on the page
    """
    context.app.main_page.alrt_dshbrd_wrds_on_pg()