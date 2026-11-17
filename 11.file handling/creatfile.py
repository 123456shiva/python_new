import csv

file=open("11.file handling/data.csv","w",newline="")
data=csv.writer(file)

data.writerow(["Name","Age","Gender"])
data.writerow(["Shiv", 22, "MCA"])
data.writerow(["Rahul", 23, "BCA"])
data.writerow(["Amit", 21, "MBA"])

file.close()

print("Data written successfully to the CSV file.")