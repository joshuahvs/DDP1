def count_positive_even(lst):
    result = []
    for i in lst:
        count= 0
        for j in i:
            if j>0 and j%2 == 0:
                count += 1
        result.append(count)
    return result

print(count_positive_even([[2,-1,0], [4,3,4]]))