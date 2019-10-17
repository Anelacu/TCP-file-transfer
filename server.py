# server.py file for NOSE assessed exercise 1
# Authors - Magdalena Latifa 2398248l and Ivan Nikitin 2292523n
# Lab group LB10
import sys
import socket
import os

# Create socket
srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Register socket with OS
srv_sock.bind(("",int(sys.argv[1])))
# Create queue for incoming requests
srv_sock.listen(5)

# on request prints string the client sent
while True:
    cli_sock,cli_addr = srv_sock.accept()
    request = cli_sock.recv(1024)
    print(str(cli_addr) + ": " + request.decode('utf-8'))
    cli_sock.close()
