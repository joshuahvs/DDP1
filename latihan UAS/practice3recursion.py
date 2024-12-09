# Create a recursion function that accepts a non-negative integer a as the argument, and return the sum of the digit. Example -> 45 = 4+5=9

def sum(number):
    if str(number) == "":
        return 0
    num = str(number)
    return int(num[0]) + sum(num[1:])

print(sum(45))