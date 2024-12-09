# class mystery_a:
#     def __init__(self):
#         self.a='string'
#         self.x=3
# class mystery_b(mystery_a):
#     def __init__(self):
#         mystery_a.__init__(self)
#         self.x = 1
# class mystery_c(mystery_b):
#     def __init__(self):
#         self.y=2
# def main():
#     b = mystery_c()
#     print(b.a,b.y)
# main()


# a_set = {2022}
# b_set={'2022'}
# print(a_set.difference(b_set))

# a_set = {'DDP 1', tuple('UAS'),2022}
# b_set={'2022','DDP 1','UAS'}
# print(a_set.difference(b_set))


# dict1 = {"name": "Mike", "salary": 8000}
# temp = dict1.pop("name")
# print(dict1["name"])

# dict_x={'name':'Jhons',
# 'age':21,
# 'hobby': ['football','PUBG'],
# 'faculty':'Computer Science'
# }
# dict_x['faculty'][1] = 'System'
# print(dict_x)


# def foo(i, j):
#     if i == 0 :
#         return j
#     else :
#         return foo(i - 1, i * j)
# print(foo(4,3))


# class A():
#     def __init__(self,count=101):
#         self.count=100
# obj1=A()
# obj2=A(102)
# print(obj1.count, end=' ')
# print(obj2.count)

# class A:
#     def __init__(self,x=5):
#         self.calcI(30,x)
#         print("i from A is", self.i *self.helper)
#     def calcI(self, i,x):
#         self.i,self.x = 3 * i,self.helper;
#     def helper(self,x):
#         self.x = 2
# class B(A):
#     def __init__(self):
#         super().__init__()
#     def calcI(self, i,x):
#         self.i,self.j = 4 * i, 5;
# B()

# class mystery_a:
#     def __init__(self):
#         self.x=0
#         self.y=2
# class mystery_b(mystery_a):
#     def __init__(self):
#         self.y = 1
# class mystery_c(mystery_b):
#     def __init__(self):
#         super().__init__()
#         self.x=3
# def main():
#     b = mystery_c()
#     print(b.x,b.y)
# main()


# def foo(i, j):
#     if i == 0 :
#         return j
#     else :
#         return foo(i - 1, i + j)
    
# print(foo(8,6))