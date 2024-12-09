# def find_modus(lst):
#     b_list = []
#     freq = []
#     for i in lst:
#         try:
#             freq += [b_list.index(i)] += 1
#         except:
#             b_list

def find_modus(a_list):
    b_list = []
    b_freq_list = []
    for x in a_list:
        try:
            b_freq_list[b_list.index(x)] += 1
        except ValueError:
            b_list.append(x)
            b_freq_list.append(1)
    max_freq = max(b_freq_list)
    return b_list[b_freq_list.index(max_freq)]


print(find_modus([5,3,4,5,3,1,-1,5,-2]))