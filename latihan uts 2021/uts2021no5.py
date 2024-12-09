# def biner2desimal(binstr):
#     if binstr[0]== "0":
#         desimal = int(binstr,2)
#         return desimal
#     else:
#         to_desimal = ''
#         for i in binstr:
#             if i == "0":
#                 to_desimal += '1'
#             elif i == '1':
#                 to_desimal += '0'
#         to_desimal += '1'
#         desimal = int(to_desimal,2)
#         return -desimal

def biner2desimal(binstr):
    if binstr[0] == "0":
        # If the first digit is '0', treat it as a positive binary number
        desimal = int(binstr, 2)
        return desimal
    else:
        # If the first digit is '1', treat it as a negative binary number
        to_desimal = ''
        for i in binstr:
            if i == "0":
                to_desimal += '0'
            elif i == '1':
                to_desimal += '0'
        to_desimal += '1'
        desimal = int(to_desimal, 2)
        return -desimal
 on hold
    
print(biner2desimal('00111'))
print(biner2desimal('11001'))