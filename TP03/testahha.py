lala = {'M': 1528, 'F': 1307, 'I': 13662}


def mode(lala):
    for i in lala.keys():
        if lala[i] == max(lala.values()):
            return i



print(mode(lala))