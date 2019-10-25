# Utility funcitons to be used by client.py and server.py
# Authors - Magdalena Latifa 2398248l and Ivan Nikitin 2292523n
# Lab group LB10
import socket
import sys
import os
from os import listdir
from os.path import curdir


''' DOC FOR REMOVING
    open the file and send it over the network via the socket --binary mode
    same as server's downloading of a file
    same as client's upload/put request (but also need to close!!)'''
def send_file(socket, filename):
    """
    Opens the file with the given file name and sends its data over networwk
    Args:
        param1(socket): The socket.
        param2 (str): The file name.
    Raises:
        Errors to be implemented later --TODO--
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        data = open(filename,'xb')
        s.connect((HOST, PORT))
        print('Established connection from ' + addr)
        l = data.read(1024)
        while(l):
            s.send(l)
        data.close()
        print('Done sending!')


''' DOC FOR REMOVING
    create the file and store in it data received from the socket --exclusive binary
    no overwriting of existing files
    same as server's uploading of a file
    same as client's download/get request (but also need to close!!)'''
def recv_file(socket, file_name):
    """
    Creates file with given name and stores data recieved from socket
    Args:
        param1(socket): The socket.
        param2(str): The file name.
    Raises:
        Errors to be implemented later --TODO--
    """

    data = ''
    temp = ''
    while True:
        temp = socket.recv(1024).decode('utf-8')
        data += temp
        print(str(addr) + ": " + data)
        myfile = open(data, "xb")
        if temp == '':
            break
    print('Done recieving file!')
    # TODO write the file here

''' DOC FOR REMOVING
    generate and send the directory listing from the server to the client
    same as server's listing: USE os.listdir() or sth'''
def send_listing(socket):
    """
    Generates and sends the directory listing from the server to the client
    Args:
        param1(socket): The socket.
    Raises:
        Errors to be implemented later --TODO--
    """
    data = ' '.join(listdir(os.path.curdir)) +'EOF'
    try:
        bytes = socket.sendall(data.encode('utf-8'))
        print('Done sending! Bytes: ', bytes)
    except socket.error as e:
        print('Cannot establish connection during sending' + str(e))
    return bytes


''' DOC FOR REMOVING
    receive the listing from the server and print it on the screen
    same as client's listing (request it, receive and print a file per line)
'''
def recv_listing(socket):
    '''docs go here'''
    data = []
    temp = ' '

    while len(temp) > 0 and "EOF" not in temp:
        print('in while loop')
        try:
            temp = socket.recv(1024).decode('utf-8')
            data.append(temp)
        except socket.error as e:
            print('Cannot establish connection during receiving' + str(e))

    data = ' '.join(data)[:-3]
    # Remove the 'EOF' which marks the end of the message
    print('Listing received from the server')
    print(data)
    return len(data)
