#!/usr/bin/env python

#******************************************************************************
#
#  CS 6421 - Gnutella
#  Execution:    python chord.py vertices entries
#
#******************************************************************************

import sys
import math
from random import randint






#******************************************************************************
#   Main code run when program is started
#******************************************************************************

if __name__ == "__main__":
    
    vertices = 64
    entries = 6

    # if input arguments are wrong, print out usage
    if len(sys.argv) != 3:
        print >> sys.stderr, "usage: python chord.py vertices entries \n".format(sys.argv[0])
    else:
        vertices = int(sys.argv[1])
        entries = int(sys.argv[2])

    if entries > int(math.log(vertices, 2)):
        entries = int(math.log(vertices, 2))

    # init dict
    vert_list = dict()

    for key in xrange(vertices):
        vert_list[key+1] = set()
        for edge in xrange(entries):
            vert_list[key+1].add((key + pow(2,edge))%vertices + 1)

    file = open("chord.js", 'w')
    file.write( "var adjacencyList = {")
    file.write("\n")
    for key in xrange(vertices):
        file.write( str(key + 1) + ": " + str(vert_list[key+1])[4:len(str(vert_list[key+1]))-1] + ",")
        file.write("\n")
    file.write( "};")
    file.close()





