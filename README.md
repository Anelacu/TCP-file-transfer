TCP file transfer server/client implementation in Python3
----------------------------------------------------------

This repository demonstrates a file transfer server implementation in python 3 using the berkeley sockets API from the python standard library. <br>
This project was part of the assessment for a university course. 

Setup
------

Make a directory for the project to be cloned into and clone the repo:
```
$ mkdir ~/workdir
$ cd ~/workdir 
$ git clone git@github.com:Anelacu/TCP-file-transfer.git
```

Example use
------------

To start the server on a given port number: 
```
$ cd sever
$ python ../server.py [port number]
```
Now we can execute commands from a client terminal. <br>
The possible list of commands is: <br>
<ul>
    <li>list - lists all files in server dir</li>
    <li>put - upload a file to server dir</li>
    <li>get - download a file from server dir</li>
</ul>

To execute a list command: 
```
$ cd client
$ python ../client.py 127.0.0.1 [port number] list
```

To execute a get command:
```
$ cd client 
$ python ../client.py 127.0.0.1 [port number] get [file_name]
```

To execute a put command:
```
$ cd client 
$ python ../client.py 127.0.0.1 [port number] put [file_name]
```