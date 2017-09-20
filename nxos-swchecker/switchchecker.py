import time, re, csv, sys, getpass, os

from sshprint import sshprint

username = getpass.getuser()
password = getpass.getpass()
time.sleep(1)
cmd = input('please enter a command:')

swnamelst = [
"10gacc-sw01",
"10gacc-sw02",
"10gacc-B-sw01",
"10gacc-B-sw02",
"tgacc-sw01",
"tgacc-sw02",
"10gacc-b-sw01",
"10gacc-b-sw02",
"10gacc-c-sw01",
"10gacc-c-sw02",
"10gacc-d-sw01",
"10gacc-d-sw02",
"dist-mls01",
"dist-mls02"
]

swiplst = [
    "10.110.69.50",
    "10.110.69.51",
    "10.110.69.60",
    "10.110.69.61",
    "10.110.69.20",
    "10.110.69.21",
    "10.110.69.62",
    "10.110.69.63",
    "10.110.69.64",
    "10.110.69.65",
    "10.110.69.75",
    "10.110.69.76",
    "10.110.69.5",
    "10.110.69.6"
]

for ip,name in zip(swiplst,swnamelst):
    filename = ip + '_ssh_output.txt'

    try:
        os.remove(filename)
        print("DELETING OLD " + filename)
        ssh_host_print(ip, username, password, cmd, name)
    except OSError:
        ssh_host_print(ip, username, password, cmd, name)
        pass