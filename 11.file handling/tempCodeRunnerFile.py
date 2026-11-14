file=open("open.txt","r")

data=file.read()
print(data)

print("The file is closed:",file.closed)