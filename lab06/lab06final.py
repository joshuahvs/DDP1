user = True

file = open("Lab6.txt", "r")
database_name = []
database_ddp1 = []
database_kalkulus = []
database_matdis1 = []

def database_mahasiswa(nama, npm, matkul, isi):
    data_mahasiswa = {
            "nama":nama,
            "npm": npm,
            "matkul": matkul,
            "isi": isi
        }
    return data_mahasiswa

def persentase(kata1, kata2):
    jumlah_kata_unik = len(set(kata1))
    kata_sama = 0
    for word in kata1:
        if word in kata2:
            kata_sama += 1
    persen = (kata_sama/jumlah_kata_unik)*100 if jumlah_kata_unik!= 0 else 0
    return persen

for line in file:
    if "DDP-1" in line:
        new_line  = line.split(";")
        nama  = new_line[0]
        npm = new_line[1]
        matkul = new_line[2].strip('\n')
        pembatas = file.readline()
        isi = file.readline()
        data_to_append = database_mahasiswa(nama, npm, matkul, isi)
        database_ddp1.append(data_to_append)
    elif "Kalkulus" in line:
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
    if nama not in database_name:
        database_name.append(nama)
file.close()

while user == True:
    print("Selamat datang di program Plagiarism Checker!")
    print("=====================================================================")

    mata_kuliah = input("Masukkan nama mata kuliah yang ingin diperiksa: ")

    if mata_kuliah == "DDP-1" or mata_kuliah == "Kalkulus" or mata_kuliah == "Matdis-1":
        try:
            mahasiswa_pertama = input("Masukkan nama/NPM mahasiswa pertama: ")
            mahasiswa_kedua = input("Masukkan nama/NPM mahasiswa kedua: ")
        
        except IndexError:
            print("Informasi mahasiswa tidak ditemukan.")
            continue

        if mata_kuliah == "DDP-1":
            for i in range(len(database_ddp1)):
                if mahasiswa_pertama in database_ddp1[i].values():
                    index_mahasiswa1 = i
            for i in range(len(database_ddp1)):
                if mahasiswa_kedua in database_ddp1[i].values():
                    index_mahasiswa2 = i

            kata1 = database_ddp1[index_mahasiswa1]['isi'].split()
            kata2 = database_ddp1[index_mahasiswa2]['isi']
            persenan = persentase(kata1, kata2)

        elif mata_kuliah == "Kalkulus":
            for i in range(len(database_kalkulus)):
                if mahasiswa_pertama in database_kalkulus[i].values():
                    index_mahasiswa1 = i
            for i in range(len(database_kalkulus)):
                if mahasiswa_kedua in database_kalkulus[i].values():
                    index_mahasiswa2 = i

            kata1 = database_kalkulus[index_mahasiswa1]['isi'].split()
            kata2 = database_kalkulus[index_mahasiswa2]['isi']
            persenan = persentase(kata1, kata2)

        elif mata_kuliah == "Matdis-1":
            for i in range(len(database_matdis1)):
                if mahasiswa_pertama in database_matdis1[i].values():
                    index_mahasiswa1 = i
            for i in range(len(database_matdis1)):
                if mahasiswa_kedua in database_matdis1[i].values():
                    index_mahasiswa2 = i

            kata1 = database_matdis1[index_mahasiswa1]['isi'].split()
            kata2 = database_matdis1[index_mahasiswa2]['isi']
            persenan = persentase(kata1, kata2)
        
        if persenan < 31:
            indikasi = "tidak terindikasi plagiarisme"
        elif persenan >= 31 and persenan<= 70:
            indikasi = "terindikasi plagiarisme ringan"
        elif persenan>70:
            indikasi = "terindikasi plagiarisme"

        print("============================= Hasil =================================")
        print(f'Tingkat kemiripan tugas {mata_kuliah} {mahasiswa_pertama} dan {mahasiswa_kedua} adalah {persenan:.2f}%')
        print(f'{mahasiswa_pertama} dan {mahasiswa_kedua} {indikasi}')
        print()

    elif mata_kuliah.casefold() == "exit":
        print("Terima kasih telah menggunakan program Plagiarism Checker!")
        user = False
    else:
        print(f'{mata_kuliah} tidak ditemukan.')