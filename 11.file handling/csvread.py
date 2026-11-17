import csv

file=open("11.file handling/data.csv","r")
data=csv.reader(file)

for row in data:
    print(row)

file.close()