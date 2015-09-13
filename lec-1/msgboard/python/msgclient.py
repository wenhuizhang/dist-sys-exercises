# CS 6421 - Simple Message Board Client in Python
# T. Wood
# Run with:     python msgclient.py

import socket
import getopt, sys

host = "52.21.64.113";
portnum = "5555";
name = "wenhui"
msg = "hello"

# your code here!

options, remainder = getopt.gnu_getopt(sys.argv[1:], 'h:p:n:m:', ['host=',
                                                                 'port number=',
                                                                 'name=',
                                                                 'msg='
                                                             ])

# Get Options from CLI
for opt, arg in options:
    if opt == '-h':
        host = arg
    elif opt == '-p':
        portnum = arg
    elif opt == '-n':
        name = arg
    elif opt == '-m':
        msg = arg
    else:
    	print "OPTIONS:"
    	print "-h : host ip address"
    	print "-p : port number"
	print "-n : your name"
	print "-m : your message"
    	
#create socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect socket
clientsocket.connect((host, int(portnum)))
#send msg
clientsocket.send(name + '\n')
clientsocket.send(msg)

#when sucessfully finishing sending sockets, tell client that messgae is sent
print("Sent message to server!")
