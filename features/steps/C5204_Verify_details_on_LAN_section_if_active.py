from behave import *

use_step_matcher("re")


@then("Pay attention to the LAN section. IP address, TX data from last reboot KB, RX data from last reboot KB, MAC address and Pie Chart")
def lan_ip_tx_rx_mac_pie_chrt(context):
    """
    Pay attention to the LAN section. IP address, TX data from last reboot KB, RX data from last reboot KB, MAC address and Pie Chart
    """
    context.app.main_page.lan_ip_tx_rx_mac_pie_chrt()