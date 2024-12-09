# Create a recursion function that accepts a list as the argument, and return the length of the list

def count_list(a):
    if a == []:
        return 0
    return 1 + count_list(a[1:])


print(count_list(['a','b', 'c','d']))