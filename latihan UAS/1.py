# class User:
#    def __init__(self, username, password):
#        self.__username = username
#        self.__password = password
#        self.__list_of_product = [] # 1 poin
#    def get_username(self):
#        return self.__username
#    def get_password(self):
#        return self.__password
#    def get_list_of_product(self):
#        return self.__list_of_product
#    def beli_product(self, product):
#        self.__list_of_product.append(product) # 1 poin
#    def print_list_of_product(self):
#        for items in self.__list_of_product: # 1 poin
#            print(f'{items} dengan jumlah <amount_product> mempunyai total harga ))(<price_product> * <amount_product>)') # 1 poin

# class Product:
#     def __init__(self, name, amount, price):
#         self.__name = name 
#         self.__amount = amount 
#         self.__price = price
#     def get_name(self): 
#         return self.__name
#     def get_amount(self): 
#         return self.__amount
#     def get_price(self): 
#         return self.__price
#     def __str__(self):
#         return self.__name + " dengan jumlah " + self.__amount + " mempunyai total harga " + (self.__amount * self.__price)

# dict = {"haha": 1}
# dict["haha"] += 1
# print(dict)

# lst = {2,4}
# print(sum(lst))

# tinggi = 5
# spasi = tinggi
# for i in range(1, tinggi+1):
#     bintang = i*2-1
#     print(' '*(spasi)+"*"*bintang)
#     spasi -=1

def f_rec(s):
    if not s:
        return s
    elif len(s) == 1:
        return s
    else:
        if s[0] == s[len(s)-1]:
            return s[0] + f_rec(s[1:-1]) + s[0]
        else:
            return f_rec(s[1:-1]) 
        
print(f_rec("abc"))
print(f_rec("abcd"))
print(f_rec("abba"))
print(f_rec("abcda"))

