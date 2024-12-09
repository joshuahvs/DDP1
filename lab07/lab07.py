print("Masukkan data relasi:")

#memproses semua input dan memasukkanya ke dalam sebuah dictionary
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

# fungsi yang akan mengechek apakah seorang anak merupakan keturunan dari parent 
def cek_keturunan(parent, child):
    if parent not in name_dict: #base case
        return 0
    if child in name_dict[parent]: #base case
        return 1
    for i in name_dict[parent]: #mengecheck kemungkinan untuk cucunya
        if cek_keturunan(i, child):
            return 1
    return 0

# fungsi yang akan mencetak keturunan dari parent 
def cetak_keturunan(parent):
    if parent not in name_dict.keys(): #base case
        return ''
    keturunan = f'- {" ".join(list(name_dict[parent]))}\n' # formating untuk nanti ketika di return
    for i in name_dict[parent]: #mengecheck anak dari anaknya parent(cucunya)
        keturunan += cetak_keturunan(i)
    return keturunan
        
# fungsi yang menghitung dan mereturn jumlah jarak antara parent dan child 
def jarak_generasi(parent, child, distance = 0):
    if parent == child: #base case
        return distance
    if parent not in name_dict: #base case
        return -1
    for i in name_dict[parent]: # mengechek anak dari anaknya parent(cucunya)
        result = jarak_generasi(i, child, distance +1)
        if result != -1:
            return result
    return -1

# fungsi yang mencetak pesan terimakasih
def exit():
    print("Terima kasih telah menggunakan Relation Finder!")

# menggunakan while loop agar program terus berjalan 
user_active = True
while user_active == True:
    # mencetak menu pilihan 
    print()
    print("=====================================================================")
    print("Selamat Datang di Relation Finder! Pilihan yang tersedia:")
    print("1. CEK_KETURUNAN")
    print("2. CETAK_KETURUNAN")
    print("3. JARAK_GENERASI")
    print("4. EXIT")
    action = int(input("Masukkan pilihan: "))
    # ketika user memilih 1 
    if action == 1:
        parent = input("Masukkan nama parent: ")
        child = input("Masukkan nama child: ")
        truth  = cek_keturunan(parent, child)
        if truth == True:
            print(f"{child} benar merupakan keturunan dari {parent}")
        else:
            print(f"{child} bukan merupakan keturunan dari {parent}")
    # ketika user memilih 2
    elif action == 2:
        parent = input("Masukkan nama parent: ")
        print(cetak_keturunan(parent))
    # ketika user memilih 3
    elif action == 3:
        parent = input("Masukkan nama parent: ")
        child = input("Masukkan nama child: ")
        truth = jarak_generasi(parent, child)
        if truth != -1:
            print(f'{parent} memiliki hubungan dengan {child} sejauh {truth}')
        else:
            print(f'Tidak ada hubungan antara {parent} dengan {child}')
    # ketika user memilih 4
    elif action == 4:
        exit()
        user_active = False
    # ketika user memilih input selain deri nomer yang diberikan 
    else:
        print("input salah")
        continue

