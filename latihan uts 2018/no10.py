def bin2decimal(binStr):
    decimal = 0
    power = 0

    # Iterasi dari kanan ke kiri (LSB ke MSB) dalam string biner
    for digit in reversed(binStr):
        if digit == '1':
            decimal += 2 ** power
        elif digit != '0':
            raise ValueError("Input string is not a valid binary representation")

        power += 1

    return decimal

# Contoh penggunaan:
print(bin2decimal('0'))      # Output: 0
print(bin2decimal('101'))    # Output: 5
print(bin2decimal('11011'))  # Output: 27
print(bin2decimal('00111')) 


# def bin2decimalrec(binStr):
#     if not binStr:
#         return 0

#     last_digit = binStr[-1]

#     if last_digit == '1':
#         return bin2decimalrec(binStr[:-1]) * 2 + 1
#     elif last_digit == '0':
#         return bin2decimalrec(binStr[:-1]) * 2
#     else:
#         raise ValueError("Input string is not a valid binary representation")

# # Contoh penggunaan:
# print(bin2decimalrec('0'))      # Output: 0
# print(bin2decimalrec('101'))    # Output: 5
# print(bin2decimalrec('11011'))  # Output: 27
