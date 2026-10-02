from behave import *

@then('Check if all elements are present. 6.1. Cards: "DEVICE ONLINE", 6.2. "DEVICE OFFLINE",  6.3. "INVENTORY", 6.4. "ALERT/NOTIFICATION", 6.5. "DATA USAGE"')
def ll_lmnts_r_prsnt(context):
    """
    Check if all elements are present. 6.1. Cards: "DEVICE ONLINE", 6.2. "DEVICE OFFLINE",  6.3. "INVENTORY", 6.4. "ALERT/NOTIFICATION", 6.5. "DATA USAGE"
    """
    context.app.main_page.ll_lmnts_r_prsnt()


@then('Check if sections are present. 7.1 "Data Usage Details", 7.2. "Notifications/Alerts", 7.3. "Groups", 7.4. "Signal Strength", 7.5. "Device Location".')
def ll_sctns_r_prsnt(context):
    """
    Check if sections are present. 7.1 "Data Usage Details", 7.2. "Notifications/Alerts", 7.3. "Groups", 7.4. "Signal Strength", 7.5. "Device Location".
    """
    context.app.main_page.ll_sctns_r_prsnt()