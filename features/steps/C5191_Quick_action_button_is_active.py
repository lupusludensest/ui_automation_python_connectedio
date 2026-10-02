from behave import *

use_step_matcher("re")


@then("Click on Quick Action button and verify it has consequences")
def clck_on_quick_actns_consqncs_hr(context):
    """
    Click on Quick Action button and verify it has consequences
    """
    context.app.main_page.clck_on_quick_actns_consqncs_hr()