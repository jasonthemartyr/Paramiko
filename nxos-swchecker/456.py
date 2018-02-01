

from ssh import ssh
from ip_list_class import ListIP
from ip_list_class import *
import getpass, time, os, subprocess


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


#username = getpass.getuser()
username = input('Please type your username: \n')
password = getpass.getpass()
time.sleep(1)
command = input('Please type a command: \n')
site_local = input('Please type the site lcoation: \n')
ip_range = input("Please type a range of IP's (172.16.109.0/27, etc): \n")



#joliet_ips = ListIP('172.16.109.0/27')

site_ips = ListIP(ip_range)



site_dict = {site_local : site_ips}

output = set()
for city,router_ip in site_dict.items():
     for rtr_ip in router_ip.list_ips():
         rtr_ping = ping_ip(rtr_ip)
  
         if rtr_ping == 'up':
    
             print('# {}'.format(rtr_ip))
             login_info = {'ip': rtr_ip, 'username': username, 'password': password}
             router_login(login_info, command)
         else:
             print('cant ping {}'.format(rtr_ip))
    
    

