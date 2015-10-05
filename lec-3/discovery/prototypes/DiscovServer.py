#!/usr/bin/env python

#******************************************************************************
#
#  CS 6421 - Discovery Server
#  Execution:    python DiscovServer.py portnum
#
#******************************************************************************

import socket
import sys
import string
##TODO: import your module here



#******************************************************************************
#   Store Server Class
#******************************************************************************
class StoreServer(object):
    def __init__(self):
        self.BUFFER_SIZE = 1024
        self.welcome = "Welcome to store server. Please send the requests.\n"


    #******************************************************************************
    #   IdVerify function
    #******************************************************************************
    def IdVerify(self, userInputIP, addr):
        if (userInputIP == addr):
            return "Valid"
        else:
            return "Invalid"

    #******************************************************************************
    #   ADD function
    #******************************************************************************
    def add(self, userInputs, addr):
        
        userInputIP = userInputs[2]
        if self.IdVerify(userInputIP, addr) == "Invalid":
            print "FAILURE:Not Allowed"
            res = "FAILURE:Not Allowed"
            return res
        
        print('add...')
        print len(userInputs)
        if len(userInputs) != 4:
            print "FAILURE:SET UNIT1 UNIT2 IP PORT\n"
            res = "FAILURE:SET UNIT1 UNIT2 IP PORT\n"
            return res
        key = userInputs[0].strip('\r') + ":" + userInputs[1].strip('\r')
        value = userInputs[2].strip('\r') + ":" + userInputs[3].strip('\r')
        server_list.update({key:value})
        print server_list
        res = "SUCCESS\n"

        return res
    
    #******************************************************************************
    #   REMOVE function
    #******************************************************************************
    def remove(self, key, addr):
        userInputIP = key[0]
        if self.IdVerify(userInputIP, addr) == "Invalid":
            print "FAILURE:Not Allowed\n"
            res = "FAILURE:Not Allowed\n"
            return res
        
        print('remove...')
        if (server_list.get(key) != None):
            del server_list[key]
            res = "SUCCESS\n"
        else:
            res = "FAILURE\n"

        return res
    
    #******************************************************************************
    #   LOOKUP function
    #******************************************************************************
    def lookup(self, userInputs):
        if len(userInputs) > 3:
            print "FAILURE:LOOKUP UNIT1 UNIT2\n"
            res = "FAILURE:LOOKUP UNIT1 UNIT2\n"
            return res
        key = userInputs[0].strip('\r') + ":" + userInputs[1].strip('\r')
        print key
        print('lookup...')
        if (server_list.get(key) != None):
            res = server_list[key]
        else:
            res = "FAILURE:None\n"
        return res
    
    #******************************************************************************
    #   Function to process requests
    #******************************************************************************
    def process(self, conn, addr):
        conn.send(self.welcome)
        # read userInput from client
        userInput = conn.recv(self.BUFFER_SIZE)
        print "Conversion Request from user: " + userInput.strip('\n')

        if not userInput:
	        print "FAILURE:Error reading message\n"
                res = "FAILURE:Error reading message\n"
                conn.send(res)
                conn.close()
                return

        userInputs = userInput[:-1].split(' ')

        if userInputs[0].upper() == 'ADD':
            res = self.add(userInputs[1:], addr)
        elif userInputs[0].upper() == 'LOOKUP':
            res = self.lookup(userInputs[1:])
        elif userInputs[0].upper() == 'REMOVE':
            res = self.remove(userInputs[1:], addr)
        else:
            res = 'FAILURE:only ADD, LOOKUP and REMOVE action allowed\n'

        print "res to Client: " + res + '\n' 
        conn.send(res + '\n')
        conn.close()




#******************************************************************************
#   Main code run when program is started
#******************************************************************************
if __name__ == "__main__":
    
    interface = ""
    filename = 'path.txt'
   
    # if input arguments are wrong, print out usage
    if len(sys.argv) != 2:
        print >> sys.stderr, "usage: python {0} portnum\n".format(sys.argv[0])
        sys.exit(1)
    else:
        portnum = int(sys.argv[1])

    server_list = dict()
    # create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((interface, portnum))
    s.listen(5)

    # Server should be up and running and listening to the incoming connections
    while True:
        print('Server is running. Port:' + str(portnum))
        # Set up a new connection from the client
        conn, addr = s.accept()
        # If an exception occurs during the execution of try clause
        # the rest of the clause is skipped
        # If the exception type matches the word after except
        # the except clause is executed
        try:
            # Receives the request message from the client
            print 'Accepted connection from client', addr
            action = StoreServer()
            # Process the connection
            action.process(conn, addr[0])
        except KeyboardInterrupt:
            conn.close()
        except IOError:
            # Close the client connection socket
            conn.close()

    # Close the Server connection socket
    s.close()    
    # Exit
    sys.exit(0)

