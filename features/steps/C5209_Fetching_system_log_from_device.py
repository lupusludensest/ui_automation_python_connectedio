from behave import *

@then("Add a new device to the Device online")
def add_new_dvc_onln(context):
    """
    Add a new device to the Device online
    """
    context.app.main_page.add_new_dvc_onln()

@then("Verify the device system log is displayed {text_hr}")
def system_log_txt_hr(context, text_hr):
    """
    Verify the device system log is displayed
    """
    context.app.main_page.system_log_txt_hr(text_hr)

@then("Click on the Close icon at the top right corner of the system log")
def clck_close_systemlog(context):
    """
    Click on the Close icon at the top right corner of the system log
    """
    context.app.main_page.clck_close_systemlog()