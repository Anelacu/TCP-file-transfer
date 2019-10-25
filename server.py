# server.py file for NOSE assessed exercise 1
# Authors - Magdalena Latifa 2398248l and Ivan Nikitin 2292523n
# Lab group LB10
"""
Purpose of server.py:
    upload a file (request type and the filename -- exclusive binary mode)
        same as recv_file()
    download a file (open the file in binary mode)
        same as send_file()
    list 1st level directory contents
        i.e. send_listing()

print reoprt on the console after a request was processed
"""
import sys
import socket
import os
from utilities import *


# helper function to debug, can replace all with sys.exit(1) later
def exit():
    print('exit')
    sys.exit(1)

# Define hostname and get port from user
HOST = '0.0.0.0'
if len(sys.argv) != 2:
    print('Expected just a port number')
    exit()
try:
    PORT = int(sys.argv[1])
except ValueError:
    print("Invalid argument - int expected")
    exit()

# Define socket, bind to specified port, on request ping back address
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print('Server up and running.')
    s.listen(5)
    print("done listening")
    while True:
        print("server into first while loop" )
        cli_socket, addr = s.accept()  # = client socket and client address
        print("server accepted a connection" )
        while True:
            print("server into 2nd while loop" )
            data = cli_socket.recv(1024).decode('utf-8')
            print("server data from receiving" + str(data))
            if len(data) == 0:
                print("server got 0, break")
                break
            sent = send_listing(cli_socket)
            print('server sent: ', sent)
            if sent == 0:
                print("server sent 0, break")
                break
            #if not data:
                #break
        cli_socket.close()
        print("server close connection")
    print('Done recieving file')
    cli_socket.sendall(data)

'''

'''
