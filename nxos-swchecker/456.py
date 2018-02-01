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


command = 'sh int desc'
username = 'jmarter'
password = 'asdasdasdas'




#command = 'show interfaces status'


# stpetersburg_ips = ListIP('172.16.224.0/27')
# dunn_ips = ListIP('172.16.235.0/27')
# richfield_ips = ListIP('172.16.228.0/27')
# millington_ips = ListIP('172.16.238.0/27')
# bethlehem_ips = ListIP('172.16.234.0/27')

# tampa_ips = ListIP('172.16.225.0/27')

# jacksonville_ips = ListIP('172.16.237.0/27')
# orlando_ips = ListIP('172.16.236.0/27')

joliet_ips = ListIP('172.16.109.0/27')



# site_dict = {'St Petersbug, FL': stpetersburg_ips,'Dunn, NC' : dunn_ips,'Richfield, OH' : richfield_ips,'Millington, TN' : millington_ips,'Bethlehem, PA' : bethlehem_ips,'Tampa, FL' : tampa_ips,'Jacksonville, FL' : jacksonville_ips,'Orlando, FL' : orlando_ips}

site_dict = {'joliet, IL': joliet_ips}

output = set()
for city,router_ip in site_dict.items():

#for city,rtr_ip in site_dict.items():


     print(site_dict.items())

     #for rtr_ip, sw_ip in zip(router_ip.router_ips(), router_ip.switch_ips()):
     for rtr_ip in router_ip.list_ips():
         rtr_ping = ping_ip(rtr_ip)

    
         if rtr_ping == 'up':
    
             print('# {}'.format(rtr_ip))
             login_info = {'ip': rtr_ip, 'username': username, 'password': password}
             router_login(login_info, command)
         else:
             print('cant ping {}'.format(rtr_ip))
    
    

