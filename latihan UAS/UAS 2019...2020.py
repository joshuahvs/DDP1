# y=10
# def f1(x):
#     global y
#     y = y**x
# def f2(l):
#     for i in range (len(l)):
#         l[i] = y**l[i]
# def f3(l):
#     for val in l:
#         val *= y
# x1 = 2
# f1(x1)
# print(y) #cetak __________________________
# l1 = [1,2,0]
# f2(l1)
# print(l1) #cetak __________________________
# l2 = [1,2,0]
# f3(l2)
# print(l2) 



# x = {i*j for i in range(2, 15) for j in range(2, 15)}
# y = {i for i in range(2, 15) if i not in x}
# print(y) #cetak


# harga = {"pisang": 10000, "apel": 20000, "jeruk": 15000}
# stok = {"pisang": 20, "apel": 10, "jeruk": 5}

# harga['mangga'] = 25000
# stok['mangga'] = 30

# for k, v in harga.items():
#     print(f'{k:10}{v:6} {stok[k]:10}')

# def totalPendapatan(harga_dict, stok_dict):
#     total = 0
#     for k in harga_dict:
#         total += (harga_dict[k]*stok_dict[k])
#         print(total)
#     return total

# print(totalPendapatan(harga, stok))


# class MyClass1:
#     pass
# class MyClass2:
#     pass
# obj = MyClass1()
# result = isinstance(obj,MyClass2)
# print(result)  # Output: True

# def sq(lst,val=0):
#     if len(lst)==0:
#         return val
#     else:
#         if isinstance(lst[-1],int): newVal = val + lst[-1]**2
#         else: newVal = val
#     return sq(lst[:-1], newVal)

# def sq_forloop(lst):
#     val = 0
#     for i in lst:
#         if isinstance(i, int):
#             val += i ** 2
#     return val

# print( sq([]) ) #cetak ____________________________
# print( sq([7,7.5,-5,"abc",1]) )

# print( sq_forloop([]) ) #cetak ____________________________
# print( sq_forloop([7,7.5,-5,"abc",1]) )

# def f(x,y):
#     cnt = 0
#     for s in y:
#         if set(x).issubset(set(s)):
#             cnt +=1
#     return cnt
# print(f("i", ["aing","aku","io","ich","kulo"])) #output should be 2
# print(f("uaaaas", ["pause","uasiap","pak","ikan"])) #output should be 3


# def f(*w,**z):
#     if len(w) == 0:
#         return None
#     return lambda x,y: x*y*max(w) + len(z)
# print(f(5,2,1,a=5,b=2)(3,4)) 
# print(f(2)(2,7))


# def gambarNSegitiga(M, N):
#     blank = M
#     for i in range(1, M+1):
#         str = "*" * (i) + " " *(blank)
#         print(str *N)
#         blank -= 1

# gambarNSegitiga(1,5)
# gambarNSegitiga(7,3)


# class A:
#     x = 0
#     def __init__(self, y = 0):
#         self.x = y
#         A.x += 1
#     def fun(self, a):
#         return a * self.x
# class B(A):
#     def fun(self, a):
#         return A.x * a
    
# test1 = A()
# test2 = A(5)
# print(test1.x)
# print(test2.x)
# print(test2.fun(2))
# test3 = B(5)
# print(test3.fun(2))
# print(A.x)



def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 3

# Contoh penggunaan
sequence_generator = infinite_sequence()
for i in range(10):
    print(next(sequence_generator))



