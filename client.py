# client.py file for NOSE assessed exercise 1
# Authors - Magdalena Latifa 2398248l and Ivan Nikitin 2292523n
# Lab group LB10
"""
@args address of the server, server's port number, put/get/list, filename(for put and get)
purpose of client.py:
    upload(put) open the local file, read data and close the connection --binary mode
        same as send_file()
    download(get) create local file, read what server sent, stre it in the file, close the connection --exclusive binary mode
        same as recv_file()
    listing(list) send a request message, receive data, print it
        i.e. recv_listing()

    close the connection after all of them
"""
import socket
import sys
from utilities import send_file, recv_file, recv_listing
import os

# helper function to debug, can replace all with sys.exit(1) later
def exit():
    print('Client closed')
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

    if command == "put":
        file_name = str(sys.argv[4])
        if not os.path.exists(file_name):
            print('Wrong file name')
            sys.exit(1)

    elif command == "get":
        file_name = str(sys.argv[4])

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

call = {"put": send_file, "get": recv_file, "list": recv_listing}

# create a socket and connect it
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        con = s.connect((hostname, port_no))
    except IOError:
        print('Client cant establish connection')
    print("Client connected")


    msg = command + ',' + file_name ## there is something wrong with sys args
    print('cli',  msg)
    sent = s.sendall((msg).encode())
    if command == "get":
        status = s.recv(1024).decode()
        if status == "Good file name":
            received = call[command](s, file_name)
        else:
            print("Check file name")
            sys.exit(1)
    else:
        received = call[command](s, file_name)
    exit()
