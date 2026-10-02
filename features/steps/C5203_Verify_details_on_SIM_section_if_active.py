from behave import *

@then("Verify that the following details displayed: SIM IP address, SIM TX data from last reboot KB, SIM RX data from last reboot KB, SIM ICC number, SIM APN and SIM Pie Chart")
def sim_ip_tx_rx_mac_pie_chrt(context):
    """
    Verify that the following details displayed: SIM IP address, SIM TX data from last reboot KB, SIM RX data from last reboot KB, SIM ICC number, SIM APN and SIM Pie Chart
    """
    context.app.main_page.sim_ip_tx_rx_mac_pie_chrt()