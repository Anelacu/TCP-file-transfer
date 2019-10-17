# client.py file for NOSE assessed exercise 1
# Authors - Magdalena Latifa 2398248l and Ivan Nikitin 2292523n
# Lab group LB10
import socket
import sys

def exit():
    print('exit')
    sys.exit(1)

# create a socket
cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get hostname/IP address
if len(sys.argv) != 3:
    print('Invalid number of arguments')
    exit()
try:
    hostname = str(sys.argv[1])
    port_no = int(sys.argv[2])
except ValueError:
    print("Invalid arguments")
    exit()

print(type(hostname), hostname)
print(type(port_no), port_no)

# connect socket to server
cli_socket.connect((hostname, port_no))

"""
while sth
    # prepare req message

    # send request
    cli_socket.sendall (req message)

    # receive response, if any
    cli_socket.recv (res message max length)

    # process response
"""
#cli_socket.close()
