from behave import *

@then("Click on Quick action button")
def clck_on_quick_actions_in_rght_up_crnr(context):
    """
    Click on Quick action button
    """
    context.app.main_page.clck_on_quick_actions_in_rght_up_crnr()

@then("Click Refresh subsection")
def clck_on_rfrsh_sbsctn(context):
    """
    Click Refresh subsection
    """
    context.app.main_page.clck_on_rfrsh_sbsctn()

@then("Verify Refresh subsection is active and {text} appeares")
def rfrsh_sbsctn_actv(context, text):
    """
    Verify Refresh subsection is active and Fetching data from device... appeares
    """
    context.app.main_page.rfrsh_sbsctn_actv(text)
