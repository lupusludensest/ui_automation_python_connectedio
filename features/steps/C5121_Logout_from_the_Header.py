from behave import *

@then("Hover over the Logout button at the right corner of the Header and click on the button Logout")
def clck_hdr_lgt_btn(context):
    """
    Hover over the Logout button at the right corner of the Header and click on the button Logout
    """
    context.app.main_page.clck_hdr_lgt_btn()