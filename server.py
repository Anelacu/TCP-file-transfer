# Authors - Magdalena Latifa and Ivan Nikitin
import sys
import socket
import os
from utilities import recv_file, send_file, send_listing

# Define hostname and get port from user
HOST = '0.0.0.0'
if len(sys.argv) != 2:
    print('Expected one argument: a port number')
    sys.exit(1)
try:
    PORT = int(sys.argv[1])
except ValueError:
    print("Invalid argument - int expected")
    sys.exit(1)

call = {"put": recv_file, "get": send_file, "list": send_listing}

# Define socket of family IPv4 and type TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Try to create server, raise error and exit on fail
    try:
        s.bind((HOST, PORT))
        print('Server up and running.')
    except OSError as e:
        print('Cannot establish server.' + str(e))
        sys.exit(1)

    s.listen(5)
    while True:
        # Connect with client, if that doesn't work break from current request
        try:
            cli_socket, addr = s.accept()
            print("Server accepted a connection.")
        except OSError as e:
            print('Cannot connect to client.' + str(e))
            break

        # Received and process request from client
        while True:
            try:
                data = cli_socket.recv(1024).decode()
                command , file_name = data.split(",")
            except OSError as e:
                print('Error establishing connection ' + str(e))
                break
            except:
                break

            # To handle file not existing server side on client request
            if command == 'get':
                if not os.path.exists(file_name):
                    cli_socket.sendall(b"Bad file name")
                    break
                else:
                    cli_socket.sendall(b"Good file name")

            if len(data) == 0:
                print("Server got no data")
                break

            # Use dictionary to process request calls
            sent = call[command](cli_socket, file_name)

            if sent == 0:
                print("Server failed to send")
                break

        cli_socket.close()
        print("Server closed connection successfully." + "\n")
    print('Done receiving request.')
