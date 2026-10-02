from behave import *

@then("Verify that model of device is {vrf_mdl_of_dvc}")
def vrf_mdl_of_dvc(context, vrf_mdl_of_dvc):
    """
    Verify that model of device is ER2000T-NA-CAT1
    """
    context.app.main_page.vrf_mdl_of_dvc(vrf_mdl_of_dvc)


@step("Device image should be present with the correct layout at the top left corner of page")
def dvc_rgth_lctn(context):
    """
    Device image should be present with the correct layout at the top left corner of page
    """
    context.app.main_page.dvc_rgth_lctn()


@step("The image of the device should correspond to the model in the description {dvc_nm_crrlts_pic}")
def dvc_nm_crrlts_pic(context, dvc_nm_crrlts_pic):
    """
    The image of the device should correspond to the model in the description ER2000T1
    """
    context.app.main_page.dvc_nm_crrlts_pic(dvc_nm_crrlts_pic)