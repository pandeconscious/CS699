#!/usr/bin/python

import csv
import sys
import re

if len(sys.argv) != 3: #note the sys.argv[0] is the name of the python script itself, that's why we need to check a length of 3
	print "Error! Give exactly one command line argument."
	exit(1) #exit(1) is exit with errors and exit(0) is exit without errors

def add_up(row):
	total = 0
	for i in range(1, len(row)):
		if re.match(r"^[-0-9]", row[i]): #math for -ve sign as well as for digits
			total += float(row[i])
	return total
	
ifile = open(sys.argv[1], 'r') #input file as the first command line argument
reader = csv.reader(ifile) 

ofile = open(sys.argv[2], 'w') #output file as the second command line argument
writer = csv.writer(ofile, quoting=csv.QUOTE_NONNUMERIC) #QUOTE_NONUMERIC option for giving quotes around non-numeric values in the written file

list_rows = [] #this is how we declare an empty array

for row in reader: #row iterates over the rows of the file in order
	if row[0].isdigit(): #each row is a list with col values as its element
		total = add_up(row)
		row.append(total)
		list_rows = list_rows + [row] #list_rows is the final 2-D array w/0 header
	else:
		if re.match(r"^[AC]",row[0]): #matching the header files so that they are directly wriiten to the file
			row.append('')
		elif re.match(r"^S",row[0]):
			row.append("Total marks")
			 
		writer.writerow(row)

list_rows.sort(key = lambda row: row[7], reverse=True)

for row in list_rows:
	writer.writerow(row)

ifile.close()
ofile.close()

