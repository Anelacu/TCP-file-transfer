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
from utilities import recv_file, send_file, send_listing

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

call = {"put": recv_file, "get": send_file, "list": send_listing}

# Define socket of family IPv4 and type TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Try to create server, raise error and exit on fail
    try:
        s.bind((HOST, PORT))
        print('Server up and running.')
    except OSError as e:
        print('Can not establish server.' + str(e))
        exit()

    s.listen(5)
    while True:
        # Connect with client, if that doesn't work break from current request
        try:
            cli_socket, addr = s.accept()
            print("Derver accepted a connection." )
        except OSError as e:
            print('Can not connect to client.' + str(e))
            break

        # Recieved and process request from client
        while True:
            data = cli_socket.recv(1024).decode('utf-8')
            print(data)
            try:
                command, file_name = data.split(",")
            except:
                break
            print("command", command, "fname", file_name)
            print("Received data from client" + str(command))
            if len(data) == 0:
                print("Server got no data")
                break

            sent = call[command](cli_socket, file_name)
            print('Server sent: ', sent)
            if sent == 0:
                print("Server failed to send")
                break

        cli_socket.close()
        print("Server closed connection succesfully.")
    print('Done receiving request.')
