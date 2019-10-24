# Utility funcitons to be used by client.py and server.py
# Authors - Magdalena Latifa 2398248l and Ivan Nikitin 2292523n
# Lab group LB10
import socket
import sys
from os import listdir
from os.path import curdir

''' open the file and send it over the network via the socket --binary mode
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
        s.connect((HOST,PORT))
        print('Established connection from ' + addr)
        l = data.read(1024)
        while(l):
            s.send(l)
        data.close()
        print('Done sending!')


''' create the file and store in it data received from the socket --exclusive binary
    same as server's uploading of a file (but no overwriting!!!)
    same as client's download/get request (but also need to close!!)'''
def recv_file(socket, filename):
    """
    Creates file with given name and stores data recieved from socket
    Args:
        param1(socket): The socket.
        param2(str): The file name.
    Raises:
        Errors to be implemented later --TODO--
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        print('Server up and running.')
        s.listen(5)
        conn, addr = s.accept()
        print('Established connection from ' + addr)
        print('Recieving file...')
        with conn:
            while True:
                data = conn.recv(1024).decode('utf-8')
                print(str(addr) + ": " + data)
                myfile = open(data, "xb")
                if not data:
                    break
            print('Done recieving file!')

''' generate and send the directory listing from the server to the client
    same as server's listing: USE os.listdir() or sth'''
def send_listing(socket):
    """
    Generates and sends the directory listing from the server to the client
    Args:
        param1(socket): The socket.
    Raises:
        Errors to be implemented later --TODO--
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        data = listdir(os.path.curdir)
        s.connect((HOST,PORT))
        print('Established connection from ' + addr)
        s.send(data)
        print('Done sending!')


''' receive the listing from the server and print it on the screen
    same as client's listing (request it, receive and print a file per line)
    close afterwards but mabe in the client.py??'''
def recv_listing(socket):
    pass
