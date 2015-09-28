#!/usr/bin/env python

#******************************************************************************
#
#  CS 6421 - Discovery Server
#  Execution:    python proxy.py portnum
#
#******************************************************************************

import socket
import sys
##TODO: import your module here



##TODO: implement your register class here
#******************************************************************************
#   Register Class
#******************************************************************************
class Register(object):
    def __init__(self):
        # Discov Server
        self.discov_ip = "127.0.0.1"
        self.discov_portnum = 8888
        self.unit1 = "b"
        self.unit2 = "g"
    
    #******************************************************************************
    #   Register Request at Discov Server
    #******************************************************************************
    def register(self):
        # send discov msg when turned on
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.discov_ip, self.discov_portnum))
            self.msg = self.unit1 + ' ' + self.unit2 + ' ' + sock.getsockname()[0] + ' ' + sys.argv[1]
            sock.send(self.msg)
            print "registed"
            sock.close()
        except KeyboardInterrupt:
            sock.close()
            sys.exit(1)
        except IOError:
            # Close the client connection socket
            sock.close()
            sys.exit(1)
    
    #******************************************************************************
    #   Unregister Request at Discov Server
    #******************************************************************************
    def unregister(self):
        # send discov msg when turned off
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.discov_ip, self.discov_portnum))
            sock.send(self.msg)
            self.msg = self.unit1 + ' ' + self.unit2 + ' ' + sock.getsockname()[0] + ' ' + sys.argv[1]
            print "unregisted"
            sock.close()
        except KeyboardInterrupt:
            sock.close()
            sys.exit(1)
        except IOError:
            # Close the client connection socket
            sock.close()
            sys.exit(1)




##TODO: implement your get convertion server list  class here
#******************************************************************************
#   GetList Class: get convertion service list from discovery server
#******************************************************************************
class GetList(object):
    def __init__(self, filename):
        self.reg_ip = clientsocket.getsockname()[0]
        self.BUFFER_SIZE = 1024
        self.filename = filename
        # Discov Server
        self.discov_ip = "127.0.0.1"
        self.discov_portnum = 8888
    #******************************************************************************
    #   getlist: get convertion server list
    #******************************************************************************
    def getlist(self):
       	return
    
    #******************************************************************************
    #   cachelist: cache convertion server list locally
    #******************************************************************************
    def cachelist(self):
        return

#******************************************************************************
#   Proxy Server Class
#******************************************************************************
class ProxyServer(object):
    def __init__(self):
        self.BUFFER_SIZE = 1024
        self.welcome = "Welcome to conversion proxy. Please send the requests.\n"

    
    #******************************************************************************
    #   Convertion function
    #******************************************************************************
    def conver(self, host, port, from_unit, to_unit, amount):
        print('Connecting...', host, port)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        msg = from_unit + ' ' + to_unit + ' ' + amount
        sock.send(msg)
        res = sock.recv(self.BUFFER_SIZE)
        sock.close()

        return res

    #******************************************************************************
    #   Function to process requests
    #******************************************************************************
    def process(self, conn):
        conn.send(self.welcome)
        # read userInput from client
        userInput = conn.recv(self.BUFFER_SIZE)
        print "Conversion Request from user: " + userInput.strip('\n')

        if not userInput:
	        print "Error reading message\n" 
                res = "Error reading message\n"
	        conn.send(res)
	        conn.close()
                return

        userInputs = userInput[:-1].split(' ')

        if len(userInputs) != 3:
            res = "Invalid Data\n"
            conn.send(res)
            conn.close()
            return
        else:
            print ("Request Conversion Amount: " + userInputs[2])
            unit1 = userInputs[0]
            unit2 = userInputs[1]

        if (unit1 + ':' + unit2) in serverTable:
            host, port = serverTable[unit1 + ':' + unit2]
            res = self.conver(host, port, unit1, unit2, userInputs[2])
        else:
            res = 'No method to convert from ' + unit1 + ' to ' + unit2 + '\n'

        print "res to Client: " + res.strip('\n')

        conn.send(res)

        conn.close()




#******************************************************************************
#   Main code run when program is started
#******************************************************************************
if __name__ == "__main__":
    
    interface = ""
    filename = 'path.txt'
    host = "127.0.0.1"
    port = 8888
   
    # if input arguments are wrong, print out usage
    if len(sys.argv) != 2:
        print >> sys.stderr, "usage: python {0} portnum\n".format(sys.argv[0])
        sys.exit(1)
    else:
        portnum = int(sys.argv[1])




    #TODO: implement your updating convertion server list here, write into 'path.txt', for temp test only
    
    #TODO: one more step, implement serverTable without saving file locally      
	
    # iterate through the server list, update server table
    f = open(filename, 'r')
    serverTable = dict()
    for line in f:
        es = line[0:-1].split(' ')
        if len(es) == 4:
            unit1 = es[0]
            unit2 = es[1]
            ip = es[2]
            pt = int(es[3])
            serverTable[unit1 + ':' + unit2] = (ip, pt)
            serverTable[unit2 + ':' + unit1] = (ip, pt)
    print list(serverTable)    
    f.close()

    # create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((interface, portnum))
    s.listen(5)

    # register
    reg = Register()
    reg.register()

    # Server should be up and running and listening to the incoming connections
    while True:
        print('Proxy is running. Port:' + str(portnum))
        # Set up a new connection from the client
        conn, addr = s.accept()
        # If an exception occurs during the execution of try clause
        # the rest of the clause is skipped
        # If the exception type matches the word after except
        # the except clause is executed
        try:
            # Receives the request message from the client
            print 'Accepted connection from client', addr
            conv = ProxyServer()
            # Process the connection
            conv.process(conn)
        except KeyboardInterrupt:
            conn.close()
        except IOError:
            # Close the client connection socket
            conn.close()

    reg.unregister()
    # Close the Server connection socket
    s.close()
    
    # Exit
    sys.exit(0)

