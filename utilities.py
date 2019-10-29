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
def send_file(socket, file_name):
    """
    Opens the file with the given file name and sends its data over networwk
    Args:
        param1(socket): The socket.
        param2 (str): The file name.
    Raises:
        Errors to be implemented later --TODO--
    """
    """try:
        with open(file_name,'rb') as f:
            print('opened file to read')
            data = f.read()
        data += "EOF".encode()
        bytes = socket.sendall(data)
        print('Done sending! Bytes: ', bytes)
    except OSError as e:
        print('Cannot establish connection during sending' + str(e))
    except FileNotFoundError as e:
        print('Cannot find the right file' + str(e))"""

    print("Sending:", file_name)
    with open(file_name, 'rb') as f:
        raw = f.read()
    # Send actual length ahead of data, with fixed byteorder and size
    socket.sendall(len(raw).to_bytes(8, 'big'))
    # You have the whole thing in memory anyway; don't bother chunking
    socket.sendall(raw)


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
    """data = []
    temp = ''
    while len(temp) > 0:
        print("in the file rec loop")
        temp = socket.recv(1024)
        print("got this temp", temp)
        data.append(temp)
        #print(str(addr) + ": " + data)
    print('Done recieving file!')
    data = ''.join(data)[:-3]
    data = data.encode()
    with open(file_name,'xb') as f:
        f.write(data)"""
    # Get the expected length (eight bytes long, always)
    expected_size = b""
    while len(expected_size) < 8:
        more_size = socket.recv(8 - len(expected_size))
        expected_size += more_size

    # Convert to int, the expected file length
    expected_size = int.from_bytes(expected_size, 'big')

    # Until we've received the expected amount of data, keep receiving
    packet = b""  # Use bytes, not str, to accumulate
    while len(packet) < expected_size:
        buffer = socket.recv(expected_size - len(packet))
        if not buffer:
            raise Exception("Incomplete file received")
        packet += buffer
    with open(file_name, 'wb') as f:
        f.write(packet)

    #return len(data)

''' DOC FOR REMOVING
    generate and send the directory listing from the server to the client
    same as server's listing: USE os.listdir() or sth'''
def send_listing(socket, file_name):
    """
    Generates and sends the directory listing from the server to the client
    Args:
        param1(socket): The socket.
    Raises:
        Errors to be implemented later --TODO--
    """
    data = '\n'.join(listdir(os.path.curdir)) +'EOF'
    try:
        bytes = socket.sendall(str.encode(data))
        print('Done sending! Bytes: ', bytes)
    except OSError as e:
        print('Cannot establish connection during sending' + str(e))
    return bytes


''' DOC FOR REMOVING
    receive the listing from the server and print it on the screen
    same as client's listing (request it, receive and print a file per line)
'''
def recv_listing(socket, file_name):
    '''docs go here'''
    data = []
    temp = ' '

    while len(temp) > 0 and "EOF" not in temp:
        print('in while loop')
        try:
            temp = socket.recv(1024).decode()
            data.append(temp)
        except OSError as e:
            print('Cannot establish connection during receiving' + str(e))

    data = ''.join(data)[:-3]
    # Remove the 'EOF' which marks the end of the message
    print('Listing received from the server \n')
    print(data + '\n')
    return len(data)
