import subprocess
import os
from ssh import ssh
from ip_list_class import ListIP
from ip_list_class import *


def get_router_items(string):
    output = []

    for line in string.splitlines():
        # if 'IP address:' in line:
        #     output.append(line)
        output.append(line)
    return output


def router_login(login_details, command):
    router_class = ssh(login_details)

    try:
        router_command = router_class.run_command(command)
        #router_command = router_class.run_commands(command)
        for line in get_router_items(router_command):
            print(line)
    except:
        pass




def ping_ip(ip):
    res = subprocess.call(['ping', '-c', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res == 0:
        return 'up'
    else:
        return 'down'


#command = 'show diag chassis eeprom'
#command = 'show cdp nei detail'
#sw_command = 'show inventory'
#command = 'sh vlan'
#command = 'sh mac address-table | i 91cd'
#command = ['sh int desc', 'sh ver']
command = 'sh int desc'
username = 'rwb'
password = 'FireExtinguisher'




#command = 'show interfaces status'


# stpetersburg_ips = ListIP('172.16.224.0/27')
# dunn_ips = ListIP('172.16.235.0/27')
# richfield_ips = ListIP('172.16.228.0/27')
# millington_ips = ListIP('172.16.238.0/27')
# bethlehem_ips = ListIP('172.16.234.0/27')

# tampa_ips = ListIP('172.16.225.0/27')

# jacksonville_ips = ListIP('172.16.237.0/27')
# orlando_ips = ListIP('172.16.236.0/27')





# site_dict = {'St Petersbug, FL': stpetersburg_ips,'Dunn, NC' : dunn_ips,'Richfield, OH' : richfield_ips,'Millington, TN' : millington_ips,'Bethlehem, PA' : bethlehem_ips,'Tampa, FL' : tampa_ips,'Jacksonville, FL' : jacksonville_ips,'Orlando, FL' : orlando_ips}

site_dict = {
'OB-2-S': '10.16.255.1',
'NB-1-E': '10.16.255.11',
'NB-3-W': '10.16.255.12',
'NB-2-E': '10.16.255.13',
'NB-2-W': '10.16.255.14',
'NB-3-E': '10.16.255.15',
'NB-1-W': '10.16.255.16',
'NB-B-E': '10.16.255.17',
'NB-B-W': '10.16.255.18',
'OB-1-S': '10.16.255.2',
'OB-B-S': '10.16.255.3',
'OB-2-E': '10.16.255.4',
'OB-1-N': '10.16.255.5',
'OB-B-W': '10.16.255.7',
'OB-2-W': '10.16.255.9',
'OB-B-E': '172.30.250.3',
'TRAILER': '172.30.46.4',
'GUARD': '172.30.46.6',
'COMPUTER ROOM': '172.30.48.2',
'TRACTOR': '172.30.58.5',
'CONTRSUCTION': '172.30.58.6',
'NBS': '172.30.59.13',
'FIBERGLASS': '172.30.59.14',
'RECLAIM': '172.30.59.4',
'FLEETSALES': '172.30.62.3',
'MUSEUM': '172.30.62.6',
'AUD1': '172.30.63.5',
'AUD2': '172.30.63.6',
'our switch' : '10.16.255.7'
}


output = set()
#for city,router_ip in site_dict.items():

for city,rtr_ip in site_dict.items():
    print('>>>>> {} <<<<<'.format(city))



    rtr_ping = ping_ip(rtr_ip)

    if rtr_ping == 'up':
        print('ssh {}'.format(rtr_ip))
        login_info = {'ip': rtr_ip, 'username': username, 'password': password}
        router_login(login_info, command)

    else:
        print('cant ping {}'.format(rtr_ip))





    # for rtr_ip, sw_ip in zip(router_ip.router_ips(), router_ip.switch_ips()):
    #     rtr_ping = ping_ip(rtr_ip)
    #     sw_ping = ping_ip(sw_ip)

    # for rtr_ip in router_ip.router_ips:
    #     rtr_ping = ping_ip(rtr_ip)
    #
    #
    #     if rtr_ping == 'up':
    #
    #         print('# {}'.format(rtr_ip))
    #         login_info = {'ip': rtr_ip, 'username': username, 'password': password}
    #         router_login(login_info, command)
    #     else:
    #         print('cant ping {}'.format(rtr_ip))
    #
    #


