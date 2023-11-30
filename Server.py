import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def get_server_ip(self):
        return self.server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        response = os.system("ping -n 1 -w 5 " + self.server_ip)
        if response == 0:
            return (self.server_ip + "is up and running")
        else:
            return (self.server_ip + "is down.")