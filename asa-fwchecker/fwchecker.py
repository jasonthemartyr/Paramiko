import getpass, os, sshfw
from contextfunction import cust
from shutil import copyfile


def checkpath(savepath):
    savedircheck = os.path.exists(savepath)

    if savedircheck == False:
        savedir = os.makedirs(savepath)



user_name = getpass.getuser()
fwpath = '/home/' + user_name + '/fwchecker/'
checkpath(fwpath)
print("#############################################")
print("\nThis script is designed to run a single command agaist a list of ASA contexts.")
print("i.e. 'sh run | i RDG' to check for RDG rules or 'sh run | i ssh' to check ssh\n")
print("Please select fwsm or context to run your command on \n")

selection = input("\033[1m" + "fwsm, ctxt01 or all: \n" + "\033[0m")

print("#############################################\n")

user_password = getpass.getpass()

# FWSM
fwsm_host_name = "10.110.69.99"
fwsm_save_path = '/home/' + user_name + '/fwchecker/fwsm'
fwsm_list = [
    "context1",
    "context2",
    "context3"
]
# CTXT01
ctxt01_host_name = "10.110.69.86"
ctxt01_save_path = '/home/' + user_name + '/fwchecker/ctxt01'
ctxt01_list = [
    "context1",
    "context2",
    "context3"
]


if selection == "fwsm":

    cmd = input('please enter a command:')
    checkpath(fwsm_save_path)
    cust(fwsm_host_name, user_name, user_password, fwsm_save_path, fwsm_list, cmd)
elif selection == "ctxt01":

    cmd = input('please enter a command:')
    checkpath(ctxt01_save_path)
    cust(ctxt01_host_name, user_name, user_password, ctxt01_save_path, ctxt01_list, cmd)

elif selection == "all":
    cmd = input('please enter a command:')
    checkpath(fwsm_save_path)
    cust(fwsm_host_name, user_name, user_password, fwsm_save_path, fwsm_list, cmd)
    checkpath(ctxt01_save_path)
    cust(ctxt01_host_name, user_name, user_password, ctxt01_save_path, ctxt01_list, cmd)

else:
    print("wrong")