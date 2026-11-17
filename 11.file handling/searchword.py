file=open("11.file handling/copy.txt","r")
data=file.read()
words="line"

if words in data:
    print("The word is present in the file")

else:
    print("The word is not present in the file")

file.close()
