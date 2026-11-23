student = {
    "name": "Shiv",
    "age": 22,
    "course": "BCA"
}

key = input("Enter key to update: ")
value = input("Enter new value: ")

if key in student:
    student[key] = value
    print("Dictionary updated successfully")
else:
    print("Key not found")

print(student)