from behave import *

@then("IMEI {imei_is_here} is here")
def imei_is_here(context, imei_is_here):
    """
    IMEI 356961071557824 is here
    """
    context.app.main_page.imei_is_here(imei_is_here)


@then("Model {mdl_is_here} is here")
def mdl_is_here(context, mdl_is_here):
    """
    Model ER2000T-NA-CAT1 is here
    """
    context.app.main_page.mdl_is_here(mdl_is_here)


@step("Firmware version {frmwr_is_here} is here")
def frmwr_is_here(context, frmwr_is_here):
    """
    Firmware version VR2 4.0 is here
    """
    context.app.main_page.frmwr_is_here(frmwr_is_here)


@step("Modem firmware {mdm_frmwr_is_here} is here")
def mdm_frmwr_is_here(context, mdm_frmwr_is_here):
    """
    Modem firmware 20.00.524 is here
    """
    context.app.main_page.mdm_frmwr_is_here(mdm_frmwr_is_here)


@then("Words {lst_hrd_is_here} is here")
def lst_hrd_is_here(context, lst_hrd_is_here):
    """
    Words Last heard is here
    """
    context.app.main_page.lst_hrd_is_here(lst_hrd_is_here)


@step("Section {uptm_is_here} is here")
def uptm_is_here(context, uptm_is_here):
    """
    Section Uptime is here
    """
    context.app.main_page.uptm_is_here(uptm_is_here)