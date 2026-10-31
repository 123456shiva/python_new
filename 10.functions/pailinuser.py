def pailn(n):
    if n == n[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

n = input("Enter a number: ")
pailn(n)