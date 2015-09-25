#!/usr/bin/env python

#******************************************************************************
#
#  CS 6421 - Discovery Server
#  Execution:    python ConvServer.py portnum
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
        self.reg_ip = clientsocket.getsockname()[0]
        # Discov Server
        self.discov_ip = "127.0.0.1"
        self.discov_portnum = 8888
    #******************************************************************************
    #   Register Request at Discov Server
    #******************************************************************************
    def register(self):
        reg_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        reg_socket.connect((self.discov_ip, self.discov_portnum))
        msg = "Logon\t" + self.reg_ip + ":" + str(portnum)
        print msg
        reg_socket.send(msg)
        reg_socket.close()
    
    #******************************************************************************
    #   Unregister Request at Discov Server
    #******************************************************************************
    def unregister(self):
        unreg_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        unreg_socket.connect((self.discov_ip, self.discov_portnum))
        msg = "Logoff\t" + self.reg_ip + ":" + str(portnum)
        print msg
        unreg_socket.send(msg)
        unreg_socket.close()




#******************************************************************************
#   Convert Server
#******************************************************************************

class ConvServer(object):
    def __init__(self):
        # Conv Server
            self.unit1 = "b"
	    self.unit2 = "g"
	    self.index = 0.442

    #******************************************************************************
    #   Convertion function
    #******************************************************************************
    def conv_func(self, userInputs):
        inputNum = userInputs[2].strip('\r\n')
        if userInputs[0] == self.unit1 and userInputs[1] == self.unit2:
            res = str(self.index * float(inputNum))
        elif userInputs[0] == self.unit2 and userInputs[1] == self.unit1:
            res = str(float(inputNum) / self.index)
        else:
            res = "Not Supported Convertion Type"
        return res

    #******************************************************************************
    #   Function to process requests
    #******************************************************************************
    def process(self, conn):
        # Read userInput from client
        userInput = conn.recv(BUFFER_SIZE)
        userInputs = userInput.split(' ')

        if len(userInputs) != 3:
            res = "Use [" + self.unit1 + " " + self.unit2 + " num] or [" + self.unit1 + " " + self.unit2 + " num]"  
        elif (not userInputs[2].strip('\r\n').replace(".", "", 1).isdigit()) :
            res = "Use [" + self.unit1 + " " + self.unit2 + " num] or [" + self.unit1 + " " + self.unit2 + " num]"  
        else:
            print "Conversion Amount: " + userInputs[2]
            res = self.conv_func(userInputs)

        print "res: " + res
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

    #TODO: add your register code here

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
            conv = ConvServer()
            # Process the connection
            conv.process(conn)
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
