from behave import *

use_step_matcher("re")


@then("Click on Settings button in right up corner and verify it has Reboot item in the drop-down menu")
def clck_on_sttngs_it_hs_reboot(context):
    """
    Click on Settings button in right up corner and verify it has Reboot item in the drop-down menu
    """
    context.app.main_page.clck_on_sttngs_it_hs_reboot()