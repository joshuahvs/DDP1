name_dict = {}
while True:
    input_nama = input()
    if input_nama == "SELESAI":
        break
    lst_nama = input_nama.split()
    parent = lst_nama[0]
    child = lst_nama[1]
    if parent not in name_dict:
        name_dict[parent] = set()
    name_dict[parent].add(child)



print(name_dict)
print("haha")


