def plain(n):
    tem=n
    rev=0

    while n>0:
        dig=n%10
        rev=rev*10+dig
        n=n//10

    if tem==rev:
        return True
    else:
        return False

print(plain(121))