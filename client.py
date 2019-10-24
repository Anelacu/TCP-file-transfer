# client.py file for NOSE assessed exercise 1
# Authors - Magdalena Latifa 2398248l and Ivan Nikitin 2292523n
# Lab group LB10
"""
@args address of the server, server's port number, put/get/list, filename(for put and get)
purpose of client.py:
    upload(put) open the local file, read data and close the connection --binary mode
        same as send_fie()
    download(get) create local file, read what server sent, stre it in the file, close the connection --exclusive binary mode
        same as recv_file()
    listing(list) send a request message, receive data, print it
        i.e. recv_listing()

    close the connection after all of them
"""
import socket
import sys
from utilities import send_file, recv_file, recv_listing

def exit():
    print('exit')
    sys.exit(1)

class NumberError(Exception):
    pass

# create a socket
cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get hostname/IP address
try:
    if len(sys.argv) > 5: # too many arguments given
        raise NumberError
    hostname = str(sys.argv[1])
    port_no = int(sys.argv[2])
    command = str(sys.argv[3])
    if command == "put" or command == "get":
        file_name = sys.argv[4]
    elif command == "list": # no argument expected afterwards
        if len(sys.argv) == 5: # there is an
            raise NumberError
    else: # incorrect command inputed
        raise ValueError
except (IndexError, NumberError) as e:
    print('Invalid number of arguments')
    exit()
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
cli_socket.close()
