# def func(satu, dua):
#     dua.symmetric_difference_update(satu)
#     satu = {1}
#     return satu.issubset (dua)
# satu, dua = {1,4,3,2,4,1}, {12, 4, 3, 2, 4}
# c = func (satu, dua)
# print(satu)
# #jawaban__1_
# print (dua)
# #jawaban
# 2
# print (c)


#ANJINGGGGG BOOKMARK DULU LAH YANG INI GOBLOEUG
# def abracadabra(lst, n):
#     if not(len(lst)):
#         return False
#     if len(lst) == 1:
#         return lst[0] == n
#     index_of_some_el = len(lst)//2
#     some_el = lst[index_of_some_el]
#     if some_el > n:
#         return abracadabra(lst[:index_of_some_el], n)
#     elif some_el < n:
#         return abracadabra(lst[index_of_some_el:], n)
#     else:
#         return True 
    
# print(abracadabra([1, 2, 3, 4, 5], 3)) # Akan menampilkan output True
# print(abracadabra(['ab', 'ac', 'ad'], 'ad'))


# def alien_lang(some_str):
#     vocal = ['a', 'i', 'u', 'e', 'o']
#     if len(some_str) == 1:
#         return f'{some_str}g{some_str}' if some_str in vocal else some_str
#     else:
#         return alien_lang(some_str[:len(some_str)//2]) + alien_lang(some_str[len(some_str)//2:])
    
# print(alien_lang('Nama saya Budi')) # Nagamaga sagayaga Bugudigi
# # print(alien_lang('Halo')) # Hagalogo
# # print(alien_lang('crwt')) # crwt
# # haha= 'nama saya budi'
# # print(haha[:len(haha)//2])


# bag_of_words = "apple orange banana banana orange pineapple apricot"
# def puzzle(bag_of_words):
#     bag_of_words = bag_of_words.split()
#     dict_ = dict()
#     for item in bag_of_words: 
#         dict_[item] = dict_.get(item, 0) + 1
#     select = max(dict_.values())
#     a_list = [k for k, v in dict_.items() if v == select]
#     return sorted(a_list)[0]
# print (puzzle(bag_of_words))

def per_kata(word):
    if len(word) == 1 or len(word) == 0:
        return True
    else:
        if word[0] == word[-1]:
            return per_kata(word[1:-1])
        else:
            return False

def kata_palindrom(lst):
    if lst == []:
        return 0
    else:
        if per_kata(lst[0]):
            return 1 + kata_palindrom(lst[1:])
        else:
            return kata_palindrom(lst[1:])
        


lst = ['malam', 'apa', 'mengapa', 'apa']
jumlah = kata_palindrom(lst)
print(jumlah)