def plain(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False

print(plain(121))