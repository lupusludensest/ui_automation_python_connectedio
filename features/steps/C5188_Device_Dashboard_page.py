from behave import *

@then("Choose any device with IMEI number which is highlighted in blue active IMEI number and click on an active IMEI number")
def bl_hlghtd_emei_choosen(context):
    """
    Choose any device with IMEI number which is highlighted in blue active IMEI number and click on an active IMEI number
    """
    context.app.main_page.bl_hlghtd_emei_choosen()

@then('Verify the {dvc_dshbrd_opened} has opened')
def dvc_dshbrd_opened(context, dvc_dshbrd_opened):
    """
    Verify the Device Dashboard page has opened
    """
    context.app.main_page.dvc_dshbrd_opened(dvc_dshbrd_opened)