# This is the template code for the CNE335 Final Project
# Justin Ellis
# CNE 335 Fall
import os
from Server import Server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Teddy")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    server_instance = Server('35.92.45.28')
    # TODO - Call Ping method and print the results
    result = server_instance.ping()
    print("Ping Results:", result)
    result= server_instance.update()
