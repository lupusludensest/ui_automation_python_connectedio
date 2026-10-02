from behave import *

@step("Click System log subsection")
def clck_systemlog(context):
    """
    Click System log subsection
    """
    context.app.main_page.clck_systemlog()