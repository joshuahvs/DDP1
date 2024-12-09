def mystery(lst):
    if lst != []:
        if lst[0]% 2 != 0:
            mystery(lst[1:])
            print (lst[0])
        else:
            mystery(lst[1:])

mystery(([1,2,3,4,5,6,7]))