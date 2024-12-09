# def biner2desimal(binstr):
#     # Periksa apakah bilangan biner adalah negatif (2's complement representation)
#     is_negative = binstr[0] == '1'

#     # Jika negatif, lakukan operasi negasi 2's complement
#     if is_negative:
#         inverted = ''.join('1' if bit == '0' else '0' for bit in binstr)
#         decimal = -(int(inverted, 2) + 1)
#     else:
#         decimal = int(binstr, 2)

#     return decimal

# #Contoh penggunaan:
# print(biner2desimal('11100111'))  # Output: -25
# print(biner2desimal('00011001'))  # Output: 25
# print(biner2desimal('11001'))    # Output: -7
# print(biner2desimal('00111'))    # Output: 7
# print(biner2desimal('111111111111111111'))  # Output: -1
# print(biner2desimal('011111111111111111'))  # Output: 131071
# print(biner2desimal('10000000000'))  # Output: -1024

# print()
# print(biner2desimal('0'))      # Output: 0
# print(biner2desimal('0101'))    # Output: 5
# print(biner2desimal('11011'))  # Output: 27

# def biner2desimal(binstr):
#     twos = int(binstr)
#     if binstr[0] == '1':
#         ones = twos - 1
#         ones_string = str(ones)
#         bcd_list = []
#         for i in ones_string:
#             if i == '0':
#                 bcd_list.append('1')
#             else:
#                 bcd_list.append('0')
#         bcd=''.join(bcd_list)
#         dec_pos = int(bcd,2)
#         dec = dec_pos
#         dec = 0 - dec
#         return dec
#     else:
#         return int(str(twos),2)
# print(biner2desimal('11001'))

# print(biner2desimal('11100111'))  # Output: -25
# print(biner2desimal('00011001'))  # Output: 25
# print(biner2desimal('11001'))    # Output: -7
# print(biner2desimal('00111'))    # Output: 7
# print(biner2desimal('111111111111111111'))  # Output: -1
# print(biner2desimal('011111111111111111'))  # Output: 131071
# print(biner2desimal('10000000000'))  # Output: -1024

# print()
# print(biner2desimal('0'))      # Output: 0
# print(biner2desimal('101'))    # Output: 5
# print(biner2desimal('11011'))  # Output: 27

list = ['a', 'b', 'c']
print(list +['d'])