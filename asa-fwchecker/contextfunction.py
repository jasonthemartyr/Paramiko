import time, re, csv, sys, getpass, os, imp


def cust(host_name, user_name, user_password, save_path, FW_LIST, cmd):
    my_module = imp.load_source("ssh_host", "/usr/local/scripts/fw_checker/sshfw.py")

    for CUST in FW_LIST:

        filename = CUST + '_ssh_output.txt'
        changeto = "changeto context " + CUST

        try:
            os.remove(filename)
            print("DELETING OLD " + filename)
            my_module.sshfw(host_name, user_name, user_password, changeto, CUST, save_path, cmd)
        except OSError:
            my_module.sshfw(host_name, user_name, user_password, changeto, CUST, save_path, cmd)
            pass


if __name__ == "__main__":
    main()