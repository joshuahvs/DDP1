def mystery(param):
    i, j = 0, len(param) -1
    while (i!= j) and (param[i]==param[j]):
        i += 1
        j -= 1
    return i == j #return should be outside while loop??
    
print(mystery("katak"))