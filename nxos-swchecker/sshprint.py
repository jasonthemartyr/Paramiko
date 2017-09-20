import paramiko, time, os, re


def sshprint(ip, username, password, cmd, swname):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # auto accept host keys
        client.connect(ip, username=username, password=password)
    except IOError:
        print("Could not connect to {1} ({0})".format(ip, swname))

    else:
        print("#############################################")
        print(">>>>> connected to {1} ({0}): \n".format(ip, swname))

        channel = client.invoke_shell()
        time.sleep(1)
        channel.send("terminal length 0\n")
        channel.send(cmd + "\n")
        time.sleep(1)
        channel.send("exit\n")
        stdout = channel.makefile('r')
        filename = swname + '.txt'
        savedircheck = os.path.exists('swchecker')
        if savedircheck == False:
            savedir = os.makedirs('swchecker')
        savepath = '/home/' + username + '/swchecker'
        fullpath = os.path.join(savepath, filename)
        fout = open(fullpath, 'w')
        # print(fout)
        lines = stdout.readlines()

    for line in lines[13:]:
        # print(line)
        # fout.write(str(line))
        if cmd not in line and 'exit' not in line and 'terminal length 0' not in line and 'Lesser General' not in line and 'A copy of each' not in line and 'http://' not in line:
            print(line)

            fout.write(str(line))
    fout.close()
    channel.close()

    print("<<<<< disconnected from {1} ({0})\n".format(ip, swname))


if __name__ == "__main__":
    main()