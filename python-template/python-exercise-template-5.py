#!/usr/bin/python

import csv
import sys

if len(sys.argv) != 2: #note the sys.argv[0] is the name of the python script itself, that's why we need to check a length of 2
    print "Error! Give exactly one command line argument."
    exit(1) #exit(1) is exit with errors and exit(0) is exit without errors

ifile = open(sys.argv[1], 'r')
reader = csv.reader(ifile)  

for row in reader: #row iterates over the rows of the file in order
    if row[0] == "Sno":
	header_row = row #header_row stores the header row 
	break	 


header_dict = {} #empty dictionary created
for i in range(len(header_row)):
    header_dict[i] = header_row[i] #adding key, value pair to the dictionary

for key in header_dict: #loop goes through the key values
    print key, header_dict[key] 
     	
ifile.close()

