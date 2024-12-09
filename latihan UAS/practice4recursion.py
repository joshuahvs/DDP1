# Create a recursion function that accepts a string argument, and return the result if the string is a palindrome or not (True/False)

# def check_palidrome(str):
#     if str == '':
#         return 1
#     elif str == '1'
#         return 0
#     if str

# print(check_palidrome('katak'))

def is_palindrome(s):
    s = s.lower()  # Convert to lowercase for case-insensitive comparison
    if len(s) <= 1:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

result = is_palindrome('katak')
print(result)
