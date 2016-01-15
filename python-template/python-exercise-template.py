#!/usr/bin/env python

import csv
import sys
import re

def countcandidates(reader): #all the parameters in python as passed by reference
	#function to count candidates by counting vaid rows in the file
	count_candidates = 0
	for row in reader: #row iterates over the rows of the file in order
		if row[0].isdigit(): #each row is a list with col values as its elements
			count_candidates += 1	
	return count_candidates

def storearray(list_rows, reader):
	#function to store the rows of the file in a 2-D list
	for row in reader: #row iterates over the rows of the file in order
		if row[0].isdigit(): #each row is a list with col values as its element
			list_rows.append(row) #at this step the dimensionality of the array goes to two, and this way by using append function we work on the list_rows that was passed(but if we do list_rows = list_rows + [row], then we have created a local copy of list_rows in the function which will be destroyed after function returns)

def select(x): return int(x[6]) #function returns the 7 element as an int value

def sum(x, y): return x+y

def select2(x): return x[6] == '1'

def header_dict_create_print(reader, header_dict):
	#function to create and print dictionary of header column names
	for row in reader: #row iterates over the rows of the file in order
    		if row[0] == 'Sno':
			header_row = row #header_row stores the header row
			break	 
	
	for i in range(len(header_row)):
    		header_dict[i] = header_row[i] #adding key, value pair to the dictionary
	
	for key in header_dict: #loop goes through the key values
    		print key, header_dict[key]

def add_up(row):
	#this function adds up the marks along a row
	total = 0
	for i in range(1, len(row)):
		if re.match(r"^[-0-9]", row[i]): #math for -ve sign as well as for digits
			total += float(row[i])
	return total
				 
def append_total_marks(reader, writer, list_rows):
	for row in reader: #row iterates over the rows of the file in order
		if row[0].isdigit(): #each row is a list with col values as its element
			total = add_up(row)
			row.append(total)
			list_rows.append(row) #list_rows is the final 2-D array w/0 header
		else:
			if re.match(r"^[AC]",row[0]): #matching the header files so that they are directly wriiten to the file
				row.append('')
			elif re.match(r"^S",row[0]):
				row.append("Total marks")
				 
			writer.writerow(row)

	list_rows.sort(key = lambda row: row[7], reverse=True)

	for row in list_rows:
		writer.writerow(row)

def main():
	if len(sys.argv) != 2: #note the sys.argv[0] is the name of the python script itself
	    print "Error! Give exactly one command line argument."
	    exit(1) #exit(1) is exit with errors and exit(0) is exit without errors

	ifile = open(sys.argv[1], 'r')
	reader = csv.reader(ifile)  
	print "The number of candidates  =", countcandidates(reader) #calling countcandidates function
	
	list_rows= [] #empty list created
	ifile.seek(0)#go back to the beginning of the file
	storearray(list_rows, reader)
	print "The nummber of candidates =", len(list_rows)
	ifile.seek(0)
		
	list_selection = map(select, list_rows) #this is just the list of selection column
	count_selected_candidates = reduce(sum, list_selection) 
	print "The number of selected candidates= ", count_selected_candidates
	
	list_selection2 = filter(select2, list_rows) #list of the rows of the selected candidates
	count_selected_candidates2 = len(list_selection2) 
	print "The number of selected candidates= ", count_selected_candidates

	header_dict = {} #empty dictionary created
	header_dict_create_print(reader, header_dict)
	ifile.seek(0)

	list_rows = [] #make it empty to start over	
	ofile = open('marks_total.csv', 'w') #output file as the second command line argument
	writer = csv.writer(ofile, quoting=csv.QUOTE_NONNUMERIC) #QUOTE_NONUMERIC option for giving quotes around non-numeric values in the written file
	append_total_marks(reader, writer, list_rows)

	OverallM = list_rows
	top_20 = int(0.2*len(list_rows))
	bot_40 = len(list_rows) - top_20

	top20pM = list_rows[0:top_20]
	bot40pM = list_rows[-bot_40:]
	
	print "Complete array", OverallM
	print "Bottom 40%", bot40pM
	print "Top 20%", top20pM	

	ifile.close()
	ofile.close()
#main ends here

if __name__ == "__main__": #the boilerplate code for running main
	main()

