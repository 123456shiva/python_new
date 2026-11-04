def greet(name="Shiv"):
    print("Hello", name)

name = input("Enter your name: ")

if name == "":
    greet()
else:
    greet(name)