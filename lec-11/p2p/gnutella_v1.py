#!/usr/bin/env python

#******************************************************************************
#
#  CS 6421 - Gnutella
#  Execution:    python gnutella_v1.py vertices neighbors
#
#******************************************************************************

import sys
from random import randint






#******************************************************************************
#   Main code run when program is started
#******************************************************************************

if __name__ == "__main__":
    
    vertices = 100
    neighbors = 5

    # if input arguments are wrong, print out usage
    if len(sys.argv) != 3:
        print >> sys.stderr, "usage: python gnutella_v1.py vertices neighbors\n".format(sys.argv[0])
    else:
        vertices = int(sys.argv[1])
        neighbors = int(sys.argv[2])

    # init dict
    vert_list = dict()

    for key in xrange(vertices):
        vert_list[key+1] = set()
        for edge in xrange(neighbors):
            vert_list[key+1].add(randint(1, vertices))

    file = open("gnutella1.js", 'w')
    file.write( "var adjacencyList = {")
    file.write("\n")
    for key in xrange(vertices):
        file.write( str(key + 1) + ": " + str(vert_list[key+1])[4:len(str(vert_list[key+1]))-1] + ",")
        file.write("\n")
    file.write( "};")
    file.close()





