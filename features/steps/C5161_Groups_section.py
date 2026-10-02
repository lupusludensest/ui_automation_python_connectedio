from behave import *


@step("Make sure {grps_blck_is_on_scrn} block is on the screen")
def grps_blck_is_on_scrn(context, grps_blck_is_on_scrn):
    """
    Make sure Groups block is on the screen
    """
    context.app.main_page.grps_blck_is_on_scrn(grps_blck_is_on_scrn)


@then("Mouse hover question mark in top right of the Groups block and make sure tooltip appears")
def ms_hvr_qstn_mrk_tp_rgt(context):
    """
    Make sure Groups block is on the screen
    """
    context.app.main_page.ms_hvr_qstn_mrk_tp_rgt()


@step("The inscription {inscrptn_no_dt_avlbl_in_cntr_grps} is in the center of Groups block")
def inscrptn_no_dt_avlbl_in_cntr_grps(context, inscrptn_no_dt_avlbl_in_cntr_grps):
    """
    The inscription No Data Available is in the center of Groups block
    """
    context.app.main_page.inscrptn_no_dt_avlbl_in_cntr_grps(inscrptn_no_dt_avlbl_in_cntr_grps)


@then("Make sure that click on Groups drop-down list is working")
def drp_dwn_grps_hr(context):
    """
    Make sure that click on Groups drop-down list is working
    """
    context.app.main_page.drp_dwn_grps_hr()


@then("Tooltip appears when mouse hover question mark in top right of the Groups block")
def tl_tip_grps_hr(context):
    """
    Tooltip appears when mouse hover question mark in top right of the Groups block
    """
    context.app.main_page.tl_tip_grps_hr()