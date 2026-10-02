from behave import *

@step("Verify if the number of devices on the INVENTORY card should match the number of devices with online status on the Devices page")
def invntr_qntty_is_the_same(context):
    """
    Verify if the number of devices on the NVENTORY card should match the number of devices with online status on the Devices page
    """
    context.app.main_page.invntr_qntty_is_the_same()