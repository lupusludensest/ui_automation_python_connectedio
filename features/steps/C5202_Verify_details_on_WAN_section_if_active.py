from behave import *

@then("Verify that the following details displayed: IP address, TX data from last reboot KB, RX data from last reboot KB, MAC address and Pie Chart")
def ip_tx_rx_mac_pie_chrt(context):
    """
    Verify that the following details displayed: IP address, TX data from last reboot KB, RX data from last reboot KB, MAC address and Pie Chart
    """
    context.app.main_page.ip_tx_rx_mac_pie_chrt()