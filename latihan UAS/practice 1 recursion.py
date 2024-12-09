# Create a recursive function that accepts two integer argument a and b, and return the result of a power b

def square(a,b):
    if b == 0:
        return 1
    return a * square(a,b-1)

print(square(2,3))