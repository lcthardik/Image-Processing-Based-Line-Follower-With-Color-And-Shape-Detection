import os
import csv

Filename = ''
file_names = {}
shapes = ['Triangle', 'Circle', 'Square']
colors = ['Red', 'Green', 'Blue']
csvlist = []

def CSVInitialize():
    global Filename
    csvfiles = [os.path.join('.', f) for f in os.listdir('.') if f.endswith(".csv")]
    Filename = csvfiles[0]

def CSVRead():
    CSVInitialize()
    global shapes, colors, file_names
    with open(Filename, 'rb') as foo:
        read = csv.DictReader(foo)
        for row in read:
            csvlist.append(row)
    
    for color in colors:
        for shape in shapes:
            row = csvlist[0]
            for row in (x for x in csvlist if x['Color'] == color and x['Shape'] == shape):
                keyname = row['Color'] + row['Shape']
                file_names[keyname] = row['Seedling Image']
    
    return file_names
