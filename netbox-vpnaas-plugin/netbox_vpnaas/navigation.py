from netbox.plugins import PluginMenuItem, PluginMenu

menu_items = (
    PluginMenuItem(
        link='plugins:netbox_vpnaas:remoteaccesstunnel_list',
        link_text='Remote Access Tunnels'
    ),
    PluginMenuItem(
        link='plugins:netbox_vpnaas:dns_list',
        link_text='DNS Servers'
    ),
    PluginMenuItem(
        link='plugins:netbox_vpnaas:ipv4routes_list',
        link_text='IPv4 Routes'
    ),
    PluginMenuItem(
        link='plugins:netbox_vpnaas:ipv6routes_list',
        link_text='IPv6 Routes'
    ),
    PluginMenuItem(
        link='plugins:netbox_vpnaas:ipsecprofile_list',
        link_text='IPSec Profiles'
    ),
    PluginMenuItem(
        link='plugins:netbox_vpnaas:tlsprofile_list',
        link_text='TLS Profiles'
    ),
    PluginMenuItem(
        link='plugins:netbox_vpnaas:termination_list',
        link_text='Terminations'
    ),
)

menu = PluginMenu(
    label='VPN as a Service',
    groups=(
        ('VPN', menu_items),
    ),
    icon_class='mdi mdi-vpn'
)