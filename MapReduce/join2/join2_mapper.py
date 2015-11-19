#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This mapper code will input a <date word, value> input file, and move date into 
#  the value field for output
#  
#  Note, this program is written in a simple style and does not full advantage of Python 
#     data structures,but I believe it is more readable
#
#  Note, there is NO error checking of the input, it is assumed to be correct
#     meaning no extra spaces, missing inputs or counts,etc..
#
# See #  see https://docs.python.org/2/tutorial/index.html for details  and python  tutorials
#
# --------------------------------------------------------------------------


for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    key_value  = line.split(",")   #split line into key and value, returns a list
    if (key_value[1] == 'ABC' or key_value[1].isdigit()):   #if value is ABC or if value is a digit print it out
        print( '%s %s' % (key_value[0], key_value[1]) )   #print tv show, space, channel ABC or viewers

#Note that Hadoop expects a tab to separate key value
#but this program assumes the input file has a ',' separating key value
