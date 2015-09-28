#!/usr/bin/env python

#******************************************************************************
#
#  CS 6421 - Discovery Server
#  Execution:    python print.py portnum
#
#******************************************************************************



import socket
import sys
##TODO: import your module here


#******************************************************************************
#   Print Server
#******************************************************************************

class PrintServer(object):
    def __init__(self):
        self.welcome = "welcome to print server"


    #******************************************************************************
    #   Function to process requests
    #******************************************************************************
    def process(self, conn):
        # Read userInput from client
        userInput = conn.recv(BUFFER_SIZE)

        if userInput:
            res = userInput
        else:
            res = "data compromised"
        
        print res
        conn.send(res + '\n')
        # Close connection
        conn.close()


#******************************************************************************
#   Main code run when program is started
#******************************************************************************
if __name__ == "__main__":
    
    
    BUFFER_SIZE = 1024
    interface = ""

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
        print 'Ready to serve...'
        # Set up a new connection from the client
        conn, addr = s.accept()
        # If an exception occurs during the execution of try clause
        # the rest of the clause is skipped
        # If the exception type matches the word after except
        # the except clause is executed
        try:
            # Receives the request message from the client
            print 'Accepted connection from client', addr
            echo = PrintServer()
            # Process the connection
            echo.process(conn)
        except KeyboardInterrupt:
            conn.close()
        except IOError:
            # Close the client connection socket
            conn.close()

    # Close the Server connection socket
    s.close()
    
    #TODO: add your unregister code here 

    # Exit
    sys.exit(0)
