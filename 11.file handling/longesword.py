file=open("11.file handling/copy.txt","r")
data=file.read()
words=data.split()

longest=max(words,key=len)
print("The longest word is:",longest)

file.close()