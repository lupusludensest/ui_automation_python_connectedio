from behave import *


@then("Make sure {alrts_blk_txt} block is present on the screen")
def alrts_blk_prsnt(context, alrts_blk_txt):
    """
    Make sure Notifications / Alerts block is present on the screen
    """
    context.app.main_page.alrts_blk_prsnt(alrts_blk_txt)


@step("Hover over question mark in top right of the block and make sure tooltip appears")
def hvr_ovr_qstn_mrk(context):
    """
    Hover over question mark in top right of the block and make sure tooltip appears
    """
    context.app.main_page.hvr_ovr_qstn_mrk()


@then("Make sure that click on column header Groups makes it active by moving underscore sign = {undr_scr} to it")
def undrscr_hr(context, undr_scr):
    """
    Make sure that click on column header Groups makes it active by moving underscore sign = 0px none to it
    """
    context.app.main_page.undrscr_hr(undr_scr)


@then("Verify Device inactive column highlighted grey {gry_clr_inctv_clmn_hr} when hover over it and hold")
def gry_clr_inctv_clmn_hr(context, gry_clr_inctv_clmn_hr):
    """
    Verify Device inactive column highlighted grey 128, 128, 128, 1 when hover over it and hold
    """
    context.app.main_page.gry_clr_inctv_clmn_hr(gry_clr_inctv_clmn_hr)


@step("The inscription {} is in the center and does not shift when switching columns")
def no_dt_vlbl_on_ntfctn_alrt(context, no_dt_vlbl_on_ntfctn_alrt):
    """
    The inscription No Data Available is in the center and does not shift when switching columns
    """
    context.app.main_page.no_dt_vlbl_on_ntfctn_alrt(no_dt_vlbl_on_ntfctn_alrt)


@then("Click on Device and verify text {clck_on_dvc_no_dt_avlb} is here")
def clck_on_dvc_no_dt_avlb(context, clck_on_dvc_no_dt_avlb):
    """
    Click on Device and verify text No Data Available is here
    """
    context.app.main_page.clck_on_dvc_no_dt_avlb(clck_on_dvc_no_dt_avlb)


@then("Locations of the No Data Available if Groups is active=undescored 0px none")
def lctns_no_dt_avlbl_grps(context):
    """
    Locations of the No Data Available if Groups is active=undescored 0px none
    """
    context.app.main_page.lctns_no_dt_avlbl_grps()


@then("Locations of the No Data Available if Device is active=undescored 0px none")
def lctns_no_dt_avlbl_dvc(context):
    """
    Locations of the No Data Available if Device is active=undescored 0px none
    """
    context.app.main_page.lctns_no_dt_avlbl_dvc()


@then("Verify the inscription No Data Available is in the center and does not shift when switching columns")
def vrf_if_lctn_and_sz_of_n_dt_avlbl(context):
    """
    Verify the inscription No Data Available is in the center and does not shift when switching columns
    """
    context.app.main_page.vrf_if_lctn_and_sz_of_n_dt_avlbl()