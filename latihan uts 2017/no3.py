def max_cap(s):
    slist = []
    unicodelist = []
    for i in s:
        if i == i.upper() and i != " ":
            slist += [i]
    if len(slist) == 0:
        return None
    
    for j in slist:
        unicode = ord(j)
        unicodelist.append(unicode)
    comparison = 0
    for a in unicodelist:
        if a > comparison:
            comparison = a
    # print(slist)
    # print(unicodelist)
    print(slist[unicodelist.index(comparison)])
    
    # return slist[unicode.index(comparison)]

max_cap("belAjaR PyThon DengaN geMBirA")
            
    

