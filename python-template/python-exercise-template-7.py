#!/usr/bin/python

import csv
import sys
import re

if len(sys.argv) != 2: #note the sys.argv[0] is the name of the python script itself, that's why we need to check a length of 3
	print "Error! Give exactly one command line argument."
	exit(1) #exit(1) is exit with errors and exit(0) is exit without errors

def add_up(row):
	total = 0
	for i in range(1, len(row)):
		if re.match(r"^[-0-9]", row[i]): #math for -ve sign aswell as for digits
			total += float(row[i])
	return total
	

ifile = open(sys.argv[1], 'r') #input file as the first command line argument
reader = csv.reader(ifile) 

list_rows = [] #this is how we declare an empty array

for row in reader: #row iterates over the rows of the file in order
	if row[0].isdigit(): #each row is a list with col values as its element
		total = add_up(row)
		row.append(total)
		list_rows = list_rows + [row] #list_rows is the final 2-D array w/0 header

list_rows.sort(key = lambda row: row[7], reverse=True)

OverallM = list_rows

top_20 = int(0.2*len(list_rows))
bot_40 = len(list_rows) - top_20

top20pM = list_rows[0:top_20]
bot40pM = list_rows[-bot_40:]

print bot40pM
print top20pM

ifile.close()

