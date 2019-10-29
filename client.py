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
import inspect
import os
"""currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)"""
from utilities import *

# helper function to debug, can replace all with sys.exit(1) later
def exit():
    print('exit')
    sys.exit(1)

class NumberError(Exception):
    pass

# get hostname/IP address
try:
    if len(sys.argv) > 5: # too many arguments given
        raise NumberError
    hostname = str(sys.argv[1])
    port_no = int(sys.argv[2])
    command = str(sys.argv[3])
    file_name = ''
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

call = {"put": send_file, "get": recv_file, "list": recv_listing}

# create a socket and connect it
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    con = s.connect((hostname, port_no))
    print("client connected")

    print('into the while loop')
    sent = s.sendall((command+','+file_name).encode('utf-8'))
    print("clent sent=",sent)
    print("sent", sent)
    if sent == 0:
        print('client sent 0, break conn')
    received = call[command](s, file_name)
    print("client recv= " + str(received))
    if received == 0:
        print('client recieved 0, break connection')
    exit()

"""
while sth
    # prepare req message

    # send request
    cli_socket.sendall (req message)

    # receive response, if any
    cli_socket.recv (res message max length)

    # process response
"""
