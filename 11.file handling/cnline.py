file=open("11.file handling/open.txt","r")
data=file.readlines()
print("Total number of lines in the file:",len(data))
file.close()