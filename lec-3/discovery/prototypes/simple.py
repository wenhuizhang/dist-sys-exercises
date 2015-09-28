#!/usr/bin/env python

#******************************************************************************
#
#  CS 6421 - Discovery Server
#  Execution:    python simple.py portnum
#
#******************************************************************************

import socket
import sys
import string
##TODO: import your module here


#******************************************************************************
#   Simple Server Class
#******************************************************************************
class SimpleServer(object):
    def __init__(self):
        self.BUFFER_SIZE = 1024
        self.welcome = "Welcome to simple server. Please send the requests.\n"

    
    #******************************************************************************
    #   ADD function
    #******************************************************************************
    def add(self, userInputs):
        print('add...')
        res = 'set result'

        return res
    
    #******************************************************************************
    #   REMOVE function
    #******************************************************************************
    def remove(self, userInputs):
        print('remove...')
        res = 'remove...'
        
        return res
    
    #******************************************************************************
    #   LOOKUP function
    #******************************************************************************
    def lookup(self, userInputs):
        print('lookup...')
        res = 'get result'
        
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

        if userInputs[0].upper() == 'SET':
            res = self.add(userInputs)
        elif userInputs[0].upper() == 'GET':
            res = self.lookup(userInputs)
        else:
            res = 'only SET and GET action allowed\n'

        print "res to Client: " + res + '\n' 
        conn.send(res)
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
            action = SimpleServer()
            # Process the connection
            action.process(conn)
        except KeyboardInterrupt:
            conn.close()
        except IOError:
            # Close the client connection socket
            conn.close()

    # Close the Server connection socket
    s.close()    
    # Exit
    sys.exit(0)

