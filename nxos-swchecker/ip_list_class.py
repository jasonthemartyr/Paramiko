import ipaddress


class ListIP:



    def __init__(self, subnet):
        self.subnet = ipaddress.ip_network(subnet, strict=False)

    def ip_subnet_mask(self):
        """
        A method that converts the cidr notation to a subnet mask.
        :return:
        """
        iprange = ipaddress.ip_network(self.subnet)
        ipsubnet = iprange.netmask
        return ipsubnet

    def format_ip(self):
        """
        A method that removes the cidr notation.
        :return:
        """
        ip = format(str(self.subnet).split('/', 1)[0])

        return ip

    def list_ips(self):
        """
        A method that places IP's in a list.
        :return:
        """

        output = []
        for ip in self.subnet:
            output.append(str(ip))
        return output[1:]

