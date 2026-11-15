file=open("11.file handling/open.txt","a")

file.write("\nThis is an appended line.")

file.close()

print("The file is closed:",file.closed)