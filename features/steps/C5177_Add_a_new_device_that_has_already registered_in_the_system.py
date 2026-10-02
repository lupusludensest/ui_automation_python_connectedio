from behave import *

@then("Add a new device that has already registered in the system")
def add_nw_dvc_alrd_rgstrd(context):
    """
    Add a new device that has already registered in the system
    """
    context.app.main_page.add_nw_dvc_alrd_rgstrd()


@then("The system should check if the device has already registered a prompt should appear Device already exists")
def systm_vrfctn_dvc_alrd_exsts(context):
    """
    The system should check if the device has already registered a prompt should appear Device already exists
    """
    context.app.main_page.systm_vrfctn_dvc_alrd_exsts()