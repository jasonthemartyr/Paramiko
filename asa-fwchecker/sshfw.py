import paramiko, time, re, csv, sys, getpass, difflib, os
from os import listdir
from os.path import isfile, join

def sshfw(host_name, user_name, user_password, changeto, CUST, save_path, cmd):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # auto accept host keys
        client.connect(host_name, username=user_name, password=user_password)
    except IOError:
        print("Could not connect to %s" % CUST)
    else:
        print("#############################################")
        print(">>>>> connected to %s \n" % CUST)
        channel = client.invoke_shell()
        time.sleep(1)
        channel.send("en\n")
        channel.send(user_password + "\n")
        channel.send("terminal pager 0\n")
        channel.send(changeto + "\n")
        channel.send(cmd + "\n")
        channel.send("sh run | i domain\n")
        channel.send("exit\n")
        stdout = channel.makefile('r')
        name_of_file = CUST + '_FW_output.txt'
        completeName = os.path.join(save_path, name_of_file)
        fout = open(completeName, 'w')
        lines = stdout.readlines()
        for line in lines[13:]:
            if cmd not in line and 'exit' not in line and 'terminal pager 0' not in line and "Type help" not in line and "Password" not in line:
                print(line)
                fout.write(str(line))
        fout.close()
        time.sleep(5)
        channel.close()
        print("<<<<< disconnected from %s \n" % CUST)
if __name__ == "__main__":
    main()