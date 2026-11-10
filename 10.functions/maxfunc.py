def maximum(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


result = maximum(10, 20, 15)
print("The maximum value is:", result)