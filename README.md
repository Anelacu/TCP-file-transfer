# TCP file transfer server/client implementation in Python3

This repository demonstrates a file transfer server implementation in python 3 using the berkeley sockets API from the python standard library. <br>

## Setup

Make a directory for the project to be cloned into and clone the repo:
```shell
$ mkdir ~/workdir
$ cd ~/workdir 
$ git clone git@github.com:Anelacu/TCP-file-transfer.git
```

## Example use

To start the server on a given port number: 
```shell
$ cd server
$ python ../server.py [port number]
```
Now we can execute commands from a client terminal. <br>
The possible list of commands is:

- list - lists all files in server dir
- put - upload a file to server dir
- get - download a file from server dir

To execute a list command: 
```shell
$ cd client
$ python ../client.py 127.0.0.1 [port number] list
```

To execute a get command:
```shell
$ cd client 
$ python ../client.py 127.0.0.1 [port number] get [file_name]
```

To execute a put command:
```shell
$ cd client 
$ python ../client.py 127.0.0.1 [port number] put [file_name]
```