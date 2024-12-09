#Membuka file untuk dibaca
file = open("Lab6.txt", "r")
#database untuk setiap matkul
database_ddp1 = []
database_kalkulus = []
database_matdis1 = []

#fungsi untuk membuat dictionary yang akan di append ke database
def database_mahasiswa(nama, npm, matkul, isi):
    data_mahasiswa = {
            "nama":nama,
            "npm": npm,
            "matkul": matkul,
            "isi": isi
        }
    return data_mahasiswa

#fungsi untuk menghitung persentase kemiripan
def persentase(kata1, kata2):
    jumlah_kata_unik = len(set(kata1))
    set1 = set(kata1)
    set2 = set(kata2)
    jumlah_kata_sama = len(set1.intersection(set2))
    persen = (jumlah_kata_sama/jumlah_kata_unik)*100 if jumlah_kata_unik!= 0 else 0
    return persen
#Membaca file line per line, dan memasukkan setiap informasi yang dibutuhkan ke dalam dictionary
for line in file:
    if "DDP-1" in line:
        new_line  = line.split(";")
        nama  = new_line[0]
        npm = new_line[1]
        matkul = new_line[2].strip('\n')
        pembatas = file.readline()
        isi = file.readline().strip('\n')
        data_to_append = database_mahasiswa(nama, npm, matkul, isi) #menggunakan fungsi untuk menghasilkan dictionary
        database_ddp1.append(data_to_append) # menambahkan dictionary ke dalam database mahasiswa
    elif "Kalkulus-1" in line:
        new_line  = line.split(";")
        nama  = new_line[0]
        npm = new_line[1]
        matkul = new_line[2].strip('\n')
        pembatas = file.readline()
        isi = file.readline().strip('\n')
        data_to_append = database_mahasiswa(nama, npm, matkul, isi) 
        database_kalkulus.append(data_to_append)
    elif "Matdis-1" in line:
        new_line  = line.split(";")
        nama  = new_line[0]
        npm = new_line[1]
        matkul = new_line[2].strip('\n')
        pembatas = file.readline()
        isi = file.readline().strip('\n')
        data_to_append = database_mahasiswa(nama, npm, matkul, isi)
        database_matdis1.append(data_to_append)
file.close()

#fungsi untuk menemukan index data mahasiswa
def get_index(user_input, database):
    index = None
    for i in range(len(database)):
        for j in database[i].values():
            if user_input in j:
                index = i
    return index

#main programnya
user = True
while user == True:
    #program akan terus berjalan selama user tidak memilih untuk exit
    print("Selamat datang di program Plagiarism Checker!")
    print("=====================================================================")
    mata_kuliah = input("Masukkan nama mata kuliah yang ingin diperiksa: ")
    #mengecheck apakah mata kuliah terdaftar
    if mata_kuliah == "DDP-1" or mata_kuliah == "Kalkulus-1" or mata_kuliah == "Matdis-1":
        if mata_kuliah == "DDP-1": #ketika mata kuliah yang dipilih adalah DDP-1
            mahasiswa_pertama = input("Masukkan nama/NPM mahasiswa pertama: ")
            index_mahasiswa1 = get_index(mahasiswa_pertama, database_ddp1) #menggunakan fungsi untuk mencari index
            if  index_mahasiswa1 == None: #jika tidak menemukan index mahasiswa 1
                print("Informasi mahasiswa tidak ditemukan.")
                print()
                continue
            mahasiswa_kedua = input("Masukkan nama/NPM mahasiswa kedua: ")
            index_mahasiswa2 = get_index(mahasiswa_kedua, database_ddp1)
            if index_mahasiswa2 == None: #jika tidak menemukan index mahasiswa 2
                print("Informasi mahasiswa tidak ditemukan.")
                print()
                continue
            kata1 = database_ddp1[index_mahasiswa1]['isi'].split() #melihat isi yang akan di check plagiarismenya
            kata2 = database_ddp1[index_mahasiswa2]['isi'].split()
            nama_mahasiswa1 = database_ddp1[index_mahasiswa1]['nama'] #melihat nama dari mahasiswa(jika yang dimasukkan adalah npm)
            nama_mahasiswa2 = database_ddp1[index_mahasiswa2]['nama']
            persenan = persentase(kata1, kata2) #menghitung presentase plagiarisme
       
        # Ketika matkul yang ingin di check adalah kalkulus
        elif mata_kuliah == "Kalkulus-1": 
            mahasiswa_pertama = input("Masukkan nama/NPM mahasiswa pertama: ")
            index_mahasiswa1 = get_index(mahasiswa_pertama, database_kalkulus)
            if  index_mahasiswa1 == None:
                print("Informasi mahasiswa tidak ditemukan.")
                print()
                continue
            mahasiswa_kedua = input("Masukkan nama/NPM mahasiswa kedua: ")
            index_mahasiswa2 = get_index(mahasiswa_kedua, database_kalkulus)
            if index_mahasiswa2 == None:
                print("Informasi mahasiswa tidak ditemukan.")
                print()
                continue
            kata1 = database_kalkulus[index_mahasiswa1]['isi'].split()
            kata2 = database_kalkulus[index_mahasiswa2]['isi'].split()
            nama_mahasiswa1 = database_kalkulus[index_mahasiswa1]['nama']
            nama_mahasiswa2 = database_kalkulus[index_mahasiswa2]['nama']
            persenan = persentase(kata1, kata2)
        #ketika matkul yang ingin di check adalah matdis
        elif mata_kuliah == "Matdis-1":
            mahasiswa_pertama = input("Masukkan nama/NPM mahasiswa pertama: ")
            index_mahasiswa1 = get_index(mahasiswa_pertama, database_matdis1)
            if  index_mahasiswa1 == None:
                print("Informasi mahasiswa tidak ditemukan.")
                print()
                continue
            mahasiswa_kedua = input("Masukkan nama/NPM mahasiswa kedua: ")
            index_mahasiswa2 = get_index(mahasiswa_kedua, database_matdis1)
            if index_mahasiswa2 == None:
                print("Informasi mahasiswa tidak ditemukan.")
                print()
                continue
            kata1 = database_matdis1[index_mahasiswa1]['isi'].split()
            kata2 = database_matdis1[index_mahasiswa2]['isi'].split()
            nama_mahasiswa1 = database_kalkulus[index_mahasiswa1]['nama']
            nama_mahasiswa2 = database_kalkulus[index_mahasiswa2]['nama']
            persenan = persentase(kata1, kata2)
        
        # menghitung tingkat keparahan plagiarisme berdasarkan hitungan persenan
        if persenan < 31:
            indikasi = "tidak terindikasi plagiarisme"
        elif persenan >= 31 and persenan<= 70:
            indikasi = "terindikasi plagiarisme ringan"
        elif persenan>70:
            indikasi = "terindikasi plagiarisme"
        # Mencetak hasil dari test plagiarisme
        print("============================= Hasil =================================")
        print(f'Tingkat kemiripan tugas {mata_kuliah} {nama_mahasiswa1} dan {nama_mahasiswa2} adalah {persenan:.2f}%')
        print(f'{nama_mahasiswa1} dan {nama_mahasiswa2} {indikasi}.')
        print()
    # ketika user memilih untuk exit, maka program akan berhenti
    elif mata_kuliah == "EXIT":
        print("Terima kasih telah menggunakan program Plagiarism Checker!")
        user = False
    # jika input matkul dari user tidak valid
    else:
        print(f'{mata_kuliah} tidak ditemukan.')
        print()