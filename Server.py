import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def get_server_ip(selfself):
        return self.server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        response - os.system("ping -n 1 -W5 " + self.server_ip + " > /dev/null 2>&1")
            if response == 0:
                return (self.server_ip + "is up and running")
            else:
                return (self.server_ip + "is down.")