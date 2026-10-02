from behave import *

@step("Make sure {dvc_lctns_txt_hr} words are on the screen")
def dvc_lctns_txt_hr(context, dvc_lctns_txt_hr):
    """
    Make sure Device Locations words are on the screen
    """
    context.app.main_page.dvc_lctns_txt_hr(dvc_lctns_txt_hr)


@step("Mouse hover question mark in top right of the block and make sure tooltip appears")
def qstn_crcl_dvc_lctn_sctn(context):
    """
    Mouse hover question mark in top right of the block and make sure tooltip appears
    """
    context.app.main_page.qstn_crcl_dvc_lctn_sctn()


@then("Make sure that click on Device Locations drop-down list is working")
def dvc_lctns_drp_dwn_mn(context):
    """
    Make sure that click on Device Locations drop-down list is working
    """
    context.app.main_page.dvc_lctns_drp_dwn_mn()