from behave import *

@step('Go to the Devices page {dvcs_url}')
def go_to_dvcs_pg(context, dvcs_url):
    """
    Go to the Devices page https://devcloud.connectedio.com/devices
    """
    context.app.main_page.go_to_dvcs_pg(dvcs_url)


@then("Click Add new device button on the right up corner")
def clck_add_nw_dvc(context):
    """
    Click Add new device button on the right up corner
    """
    context.app.main_page.clck_add_nw_dvc()


@then("Fill required Device IMEI field {emei}")
def fill_emei_fld(context, emei):
    """
    Fill required Device IMEI field 356961071557824
    """
    context.app.main_page.fill_emei_fld(emei)


@step("Fill Device Name field if any {dvc_nm}")
def fill_dvc_nm_fld(context, dvc_nm):
    """
    Fill required Device IMEI field 356961071557824
    """
    context.app.main_page.fill_dvc_nm_fld(dvc_nm)


@then("Fill required Serial Number field {srl_nmbr}")
def fill_srl_nmbr_fld(context, srl_nmbr):
    """
    Fill required Device IMEI field 356961071557824
    """
    context.app.main_page.fill_srl_nmbr_fld(srl_nmbr)


@step("Click Save and refresh the page")
def clck_sv_btn(context):
    """
    Click Save and refresh the page
    """
    context.app.main_page.clck_sv_btn()


@then("Success is here - device is on the page")
def dvc_is_on_the_pg(context):
    """
    Success is here - device is on the page
    """
    context.app.main_page.dvc_is_on_the_pg()


@then("Delete device")
def delt_dvc(context):
    """
    Delete device
    """
    context.app.main_page.delt_dvc()