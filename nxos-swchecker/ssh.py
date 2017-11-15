from paramiko import client

class ssh:
    client = None

    def __init__(self, logindetails):
        self.__ip = logindetails['ip']
        self.__username = logindetails['username']
        self.__password = logindetails['password']
        self.client = client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        self.client.connect(self.__ip, username=self.__username, password=self.__password, look_for_keys=False)

    def run_command(self, command):
        if (self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
            while not stdout.channel.exit_status_ready():
                if stdout.channel.recv_ready():
                    alldata = stdout.channel.recv(9000)
                    prevdata = True
                    while prevdata:
                        prevdata = stdout.channel.recv(9000)
                        alldata += prevdata
                    return str(alldata, "utf8")
        else:
            print("Connection not opened.")
