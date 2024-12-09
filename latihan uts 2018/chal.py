# def decimaltobiner(number):
#     biner1 = ""
#     # hasil_pembagian = 0
#     while number > 0:
#         if number%2 == 0:
#             biner1 = "0" + biner1
#         elif number%2 == "1":
#             biner1 = "1" + biner1
#         number = number//2
#     return biner1

# print(decimaltobiner(7))
    
# def decimal_to_binary(decimal):
#     if decimal == 0:
#         return '0'
    
#     binary = ''
#     while decimal > 0:
#         remainder = decimal % 2
#         binary = str(remainder) + binary
#         decimal = decimal // 2
    
#     return binary

# print(decimal_to_binary(7))



list1 = [[2,3,4],20,30,40]
list2 = list1
list3 = list2[:]
list1[1] = 7
list2[3] = 9
list3[2] = 0
list3[0][-1] = 8
print(list1)
print("list2:", list2)
print("list3:", list3)
#cetak list2: [[2, 3, 8], 7, 30, 9] #cetak list3: [[2, 3, 8], 20, 0, 40]