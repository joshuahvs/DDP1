def replace_with_1(s,c):
    result = ''
    for i in s:
        if i ==c:
            result += '1'
        else:
            result += i
    return result

print(replace_with_1('apasaja', 'a'))
print(replace_with_1('fasilkom', 'i'))