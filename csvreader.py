############################################################################################################
	# Team Id : PB#4097
	# Author List : Aditya Agrawal
	# Filename: csvreader.py
	# Theme: Planterbot
	# Functions: CSVInitialize(), CSVRead()
	# Global Variables: Filename, file_names, shapes, colors, csvlist
#############################################################################################################
import os #For file management
import csv #To read from CSV Files

Filename='' #To store filename of CSV file
file_names={} #To store filenames of flowers corresponding to Shape and Color combination
shapes=['Triangle','Circle','Square'] 
colors=['Red','Green','Blue']
csvlist=[] #To store CSV values read from File as I had problems iterating over object
def CSVInitialize():
	#Function Name: CSVInitialize
	#Input: None
	#Output: Stores Filename of CSV file
	#Logic: Iterates over files in the root direcory to find all CSV files and stores the first one in the list
	#Example Call: CSVInitialize()
	global Filename
	csvfiles = [os.path.join('.', f) for f in os.listdir('.') if f.endswith(".csv")]
	Filename=csvfiles[0]
def CSVRead():
	CSVInitialize()
	global shapes,colors,file_names
	with open(Filename, 'rb') as foo:
		
		read=csv.DictReader(foo)
		for row in read:
			csvlist.append(row)
	for color in colors:
		#print color
		for shape in shapes:
				row = csvlist[0]
				for row in (x for x in csvlist if x['Color']==color and x['Shape']==shape):
							
					keyname=row['Color']+row['Shape']
					file_names[keyname]=row['Seedling Image']
	return file_names			



	
