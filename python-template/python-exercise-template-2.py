#!/usr/bin/python

import csv
import sys

if len(sys.argv) != 2: #note the sys.argv[0] is the name of the python script itself, that's why we need to check a length of 2
    print "Error! Give exactly one command line argument."
    exit(1) #exit(1) is exit with errors and exit(0) is exit without errors

ifile = open(sys.argv[1], 'r')
reader = csv.reader(ifile)  

count_candidates = 0

list_rows = [] #this is how we declare an empty array

for row in reader: #row iterates over the rows of the file in order
    if row[0].isdigit(): #each row is a list with col values as its element
	list_rows = list_rows + [row] #at this step the dimensionality of the array goes to two

count_candidates = len(list_rows)

print "The number of candidates= ", count_candidates

ifile.close()

