# def cetak_plus(a):
#     if a %2 == 0 :
#         print("Input harus bilangan ganjil")
#     else:
#         b = a//2
#         for i in range(b):
#             print(""*b, "*")
#         print("*"*a)
#         for i in range(b):
#             print(""*b, "*")

def cetak_plus(a):
    if a %2 == 0 :
        print("Input harus bilangan ganjil")
    else:
        for i in range(a):
            if i == a//2:
                print('*'*a)
            else:
                b = a//2
                print(" "*b + "*")

cetak_plus(5)