# client.py file for NOSE assessed exercise 1
# Authors - Magdalena Latifa 2398248l and Ivan Nikitin 2292523n
# Lab group LB10
import socket
import sys

# create a socket
cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get hostname/IP address
hostname = ""
port_no = 0

# connect socket to server
# todo cli_socket.connect((hostname, port number))

"""
while sth
    # prepare req message

    # send request
    cli_socket.sendall (req message)

    # receive response, if any
    cli_socket.recv (res message max length)

    # process response
"""
cli_socket.close()
