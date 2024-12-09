def k_sum_pairs(lst, a):
    pairs = []
    for i in lst:
        for j in lst:
            if i + j == a:
                pairs += [(i,j)]
    print(pairs)

k_sum_pairs([-4,5,-2,7], 3)
k_sum_pairs([-4,5,-2,7], 2)