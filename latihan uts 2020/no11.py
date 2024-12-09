def m(x):
    z = []
    for y in x:
        if (y and True) or False:
            z.append (y)
    return len(z)
 
print(m([True, False, True]))