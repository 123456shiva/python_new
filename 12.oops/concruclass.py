class student:
    def __init__(self, name, age, rollno):
        self.name = name
        self.age = age
        self.rollno = rollno

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.rollno)

S1 = student("Shiv Sharan", 20, 101)
S1.display()