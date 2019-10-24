# Utility funcitons to be used by client.py and server.py
# Authors - Magdalena Latifa 2398248l and Ivan Nikitin 2292523n
# Lab group LB10
import socket
import sys


def send_file(socket, filename):
    pass


def recv_file(socket, filename):
    """
    Creates file with given name and stores data recieved from socket
    Args:
        param1: The socket.
        param2: The file.
    Raises:
        Errors to be implemented later --TODO--
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        print('Server up and running.')
        s.listen(5)
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024).decode('utf-8')
                print(str(addr) + ": " + data)
                myfile = open(data, "xb")
                if not data:
                    break
            print('Done recieving file')


def send_listing(socket):
    pass


def recv_listing(socket):
    pass
