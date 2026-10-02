from behave import *

@then("Click Dashboard menu icon and make sure {dsbrd_txt} page reloaded")
def clck_on_dsch_brd_mn_icn(context, dsbrd_txt):
    """
    Click Dashboard menu icon and make sure Dashboard page reloaded
    """
    context.app.main_page.clck_on_dsch_brd_mn_icn(dsbrd_txt)


@then("Make sure Data Usage Details block {dt_usg_blk} is present on the screen")
def mk_sr_dt_usg_dtls_blck_hr(context, dt_usg_blk):
    """
    Make sure Data Usage Details block DATA USAGE is present on the screen
    """
    context.app.main_page.mk_sr_dt_usg_dtls_blck_hr(dt_usg_blk)


@step("Hover over question mark in top right of the block and make sure tooltip {tl_tp_txt} appears")
def hvr_ovr_qstn_mrk_tl_tps_hr(context, tl_tp_txt):
    """
    Hover over question mark in top right of the block and make sure tooltip WAN/Cellular data usage classified periodically. appears
    """
    context.app.main_page.hvr_ovr_qstn_mrk_tl_tps_hr(tl_tp_txt)


@step("Change in drop-down changes the columns = click on Today option from drop-down menu")
def clck_on_tdy_optn_drp_mn(context):
    """
    Change in drop-down changes the columns = click on Today option from drop-down menu
    """
    context.app.main_page.clck_on_tdy_optn_drp_mn()


@then("The inscription No Data Available is in the center")
def no_dt_avlbl_hr(context):
    """
    The inscription No Data Available is in the center
    """
    context.app.main_page.no_dt_avlbl_hr()


@then("Verify GB inactive column highlighted grey {clr_gr} when hover over it and hold")
def gb_inctv_clmn_is_grey(context, clr_gr):
    """
    Verify GB inactive column highlighted grey 128, 128, 128, 1 when hover over it and hold
    """
    context.app.main_page.gb_inctv_clmn_is_grey(clr_gr)

