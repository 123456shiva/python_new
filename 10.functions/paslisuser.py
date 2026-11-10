def display(numbers):
    for i in numbers:
        print(i)

my_list = []

n = int(input("Enter number of elements: "))

for i in range(n):
    num = int(input("Enter number: "))
    my_list.append(num)

display(my_list)