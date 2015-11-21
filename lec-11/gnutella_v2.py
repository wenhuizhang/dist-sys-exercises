#!/usr/bin/env python

#******************************************************************************
#
#  CS 6421 - Gnutella
#  Execution:    python gnutella_v2.py leaf leaf_neighbors
#
#******************************************************************************

import sys
from random import randint






#******************************************************************************
#   Main code run when program is started
#******************************************************************************

if __name__ == "__main__":
    
    leaf = 1000
    leaf_neighbors = 3
    ultra = 256
    ultra_neighbors = 32

    # if input arguments are wrong, print out usage
    if len(sys.argv) != 5:
        print >> sys.stderr, "usage: python gnutella_v2.py leaf leaf_neighbors ultra ultra_neighbors\n".format(sys.argv[0])
    else:
        leaf = int(sys.argv[1])
        leaf_neighbors = int(sys.argv[2])
        ultra = int(sys.argv[3])
        ultra_neighbors = int(sys.argv[4])

    # init dict
    vert_list = dict()
    ultra_list = dict()

    for key in xrange(ultra):
        ultra_list[key+1] = set()
        for edge in xrange(ultra_neighbors):
            ultra_list[key+1].add(randint(1, leaf))


    for key in xrange(leaf):
        vert_list[key+1] = set()
        for edge in xrange(leaf_neighbors):
            vert_list[key+1].update(ultra_list[randint(1,ultra)])



    

    file = open("gnutella2.js", 'w')
    file.write("var adjacencyList = {")
    file.write("\n")
    for key in xrange(leaf):
        file.write( str(key + 1) + ": " + str(vert_list[key+1])[4:len(str(vert_list[key+1]))-1] + ",")
        file.write("\n")
    file.write( "};")
    file.close()





