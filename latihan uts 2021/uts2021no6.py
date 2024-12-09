INT_MODE = 1
FLOAT_MODE = 2
STR_MODE = 3

def convert_list (a_list, convert_mode):
    new_list = []
    for i in a_list:
        try:
            if convert_mode == 1:
                a = int(i)
            elif convert_mode == 2:
                a = float(i)
            elif convert_mode == 3:
                a = str(i)
        except ValueError:
            a = "Conversion Error"
        new_list.append(a)
    return new_list


my_list = ["1", "2.5", "3.14", "hello"]
converted_list = convert_list(my_list, INT_MODE)
print(converted_list)


# alist= [1, "2", 3.0, "2.1", "X"]
# a_list = convert_list(alist, INT_MODE)
# print(alist) # [1, 2, 3, "Conversion Error"]

# def convert_list(a_list, convert_mode):
#     newList = []
#     for i in a_list:
#         try:
#             if convert_mode == 1:
#                 a = int(i)
#             elif convert_mode == 2:
#                 a = float(i)
#             elif convert_mode == 3:
#                 a = str(i)
#         except ValueError:
#             a = 'Conversion Error'
#         newList.append(a)
#     return newList

# alist_2 = [1,"2", 3.0, "y" "2.1"]
# a_list_2 = convert_list(alist_2, FLOAT_MODE)
# print(alist_2) # [1.0, 2.0, 3.0, "Conversion Error", 2.1]

# alist_3= [1, "2", 3.0, "y", "2.1"]
# a_list_3 = convert_list(alist_3, STR_MODE)
# print(alist_3) # ['1', '2', '3.0', 'y', '2.1']