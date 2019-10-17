# server.py file for NOSE assessed exercise 1
# Authors - Magdalena Latifa 2398248l and Ivan Nikitin 2292523n
# Lab group LB10
import sys
import socket
import os

# Define hostname and get port from user
HOST = '0.0.0.0'
if len(sys.argv) != 2:
    print('Expected two arguments - server file and port number')
try:
    PORT = int(sys.argv[1])
except ValueError:
    print("Invalid argument - int expected")

# test server
# Define socket, bind to specified port, on request ping back address
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by address', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
                print('No data recieved')
            conn.sendall(data)
