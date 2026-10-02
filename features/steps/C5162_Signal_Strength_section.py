from behave import *

@step("Make sure {sgnl_strngt_txt_hr} is on the screen")
def sgnl_strngt_txt_hr(context, sgnl_strngt_txt_hr):
    """
    Make sure Signal Strength is on the screen
    """
    context.app.main_page.sgnl_strngt_txt_hr(sgnl_strngt_txt_hr)


@then("Mouse hover question mark in top right of the Signal Strength block and make sure tooltip appears")
def ms_hvr_qstn_mrk_sgnl_strngt(context):
    """
    Mouse hover question mark in top right of the Signal Strength block and make sure tooltip appears
    """
    context.app.main_page.ms_hvr_qstn_mrk_sgnl_strngt()


@then("The inscription {inscrptn_no_dt_avlbl_in_sgnl_strngt} is in the center of Signal Strength block")
def inscrptn_no_dt_avlbl_in_sgnl_strngt(context, inscrptn_no_dt_avlbl_in_sgnl_strngt):
    """
    The inscription No Data Available is in the center of Signal Strength block
    """
    context.app.main_page.inscrptn_no_dt_avlbl_in_sgnl_strngt(inscrptn_no_dt_avlbl_in_sgnl_strngt)