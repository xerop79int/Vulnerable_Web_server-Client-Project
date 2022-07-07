#!/usr/bin/env python3

import os
import socket		
import sys

just = sys.argv[1]
just = just.strip(".py")
just = __import__(just)

# Creating a socket that will handle the connection
number_of_clients = 4
HOSTNAME = "localhost"
PORT_NO = int(sys.argv[2])

address = (HOSTNAME, PORT_NO)

socket_object = socket.create_server(address, family=socket.AF_INET6,
                dualstack_ipv6=True, backlog=False)

socket_object.listen(number_of_clients)

# While loop for connections
while True:
    try:
        # handling the connection and sending request to server
        #pid = os.fork()
        client_object, client_address = socket_object.accept()
        #if pid > 0:
        init_response = client_object.recv(1024).decode()
        response = just.check_request(init_response)
        client_object.send(response.encode())
        client_object.close()
    except KeyboardInterrupt:
        if os.path.exists("./tmp/command.txt"):
            os.remove("./tmp/command.txt")
        exit(0)
    except:
        exit(0)
        