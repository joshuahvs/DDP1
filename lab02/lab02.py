# Harga dari buku-buku
x_man = 7000
doraemoh = 5500
nartoh = 4000

# Menggunakan while loop agar program terus berjalan selama pelanggan belum memilih untuk keluar 
while True:
    # Mencetak ucapan selamat datang 
    print("Selamat Datang di Toko Buku Place Anak Chill",
        "\n============================================")
    # Mencetak pilihan menu awal (pinjam buku atau keluar)
    print("1. Pinjam buku",
        "\n2. Keluar",
        "\n============================================")
    # Meminta input apa yang ingin dilakukan pelanggan 
    yang_ingin_dilakukan = int(input("Apa yang ingin anda lakukan: "))

    # Program yang akan dijalankan jika user memilih opsi 1 
    if yang_ingin_dilakukan == 1:
        # Meminta input nama, saldo, dan juga status membership 
        nama = input("Masukkan nama anda: ")
        saldo = int(input("Masukkan saldo anda (Rp): "))
        member = input("Apakah anda member? [Y/N]: ")
        # Program yang akan dijalankan ketika user adalah member
        if member == "Y":
            id = input("Masukkan ID anda: ")
            jumlah_digit = sum(int(ids) for ids in id) # Menggunakan for loop untuk mengiterasi dan menghitung jumlah digit dari ID
            # Program yang akan dijalankan jumlah digit dari ID user tidak berjumlah 23
            if jumlah_digit != 23:
                print("ID anda salah!")
                counter = 0
                # Menggunakan while loop dan counter supaya meminta program meminta ID user total sebanyak 3 kali
                while counter < 2:
                    id = input("Masukkan ID anda: ")
                    jumlah_digit = sum(int(ids) for ids in id) # Menggunakan for loop untuk mengiterasi dan menghitung jumlah digit dari ID
                    # Program yang akan dijalankan ketika ID yang dimasukkan sudah berjumlah 23
                    if jumlah_digit == 23:
                        break # Menghentikan while loop
                    else:
                        print("ID anda salah!")
                        counter += 1 # counter supaya while loop berjalan 2 kali
                # While loop ini akan otomomatis berhenti dan kembali ke menu utama jika counter >= 2, while loop akan bernilai false
                else:
                    print("Program akan kembali ke menu utama", "\n")
            
            # Program yang akan dijalankan ketika jumlah digit ID berjumlah 23
            if jumlah_digit == 23:
                print("Login member berhasil!")
                # Menggunakan while loop supaya program terus berjalan selama pelanggan belum memilih untuk exit 
                while True:
                    print("============================================",
                        "\nKatalog Buku Place Anak Chill",
                        "\n============================================",
                        "\nX-Man (Rp 7.000/hari)",
                        "\nDoraemoh (Rp 5.500/hari)",
                        "\nNartoh (Rp 4.000/hari)",
                        "\n============================================",
                        "\nExit",
                        "\n============================================")
                    # Meminta input buku
                    buku_pilihan = input("Buku yang dipilih: ")
                    if buku_pilihan.casefold() == "exit":
                        break
                    lama_peminjaman = int(input("Ingin melakukan peminjaman untuk berapa hari: "))
                    # Memberikan harga buku berdasarkan buku yang dipilih
                    if buku_pilihan.casefold() == "x-man": # Menggunakan casefold karena supaya input bersifat case insensitive
                        harga = x_man * lama_peminjaman * 0.8
                    elif buku_pilihan.casefold() == "doraemoh":
                        harga = doraemoh * lama_peminjaman * 0.8
                    elif buku_pilihan.casefold() == "nartoh":
                        harga = nartoh * lama_peminjaman * 0.8
                    # Jika buku yang dipilih tidak ada di katalog, maka program akan berjalan
                    else:
                        print("Komik tidak ditemukan. Masukkan kembali judul komik yang sesuai katalog!", "\n")
                        continue # Menggunakan continue untuk melanjutkan ke iterasi selanjutnya dan tidak menjalankan perintah selanjutnya
                    
                    # Jika saldo kurang, maka program akan mencetak tidak berhasil
                    if saldo < harga: 
                        print("Tidak berhasil meminjam! Saldo anda kurang", str(harga - saldo), "\n")
                    # Jika saldo lebih besar dari harga, maka program akan berjalan 
                    elif saldo >= harga:
                        saldo -= harga
                        # Mencetak rangkuman 
                        print("Berhasil meminjam buku", buku_pilihan, "selama", str(lama_peminjaman), "hari",
                            "\nSaldo anda saat ini Rp" + str(saldo), "\n")

        # Perintah yang akan dijalankan ketika user tidak mempunyai membership
        elif member == "N":
            while True:
                print("============================================",
                    "\nKatalog Buku Place Anak Chill",
                    "\n============================================",
                    "\nX-Man (Rp 7.000/hari)",
                    "\nDoraemoh (Rp 5.500/hari)",
                    "\nNartoh (Rp 4.000/hari)",
                    "\n============================================",
                    "\nExit",
                    "\n============================================")
                buku_pilihan = input("Buku yang dipilih: ")
                if buku_pilihan.casefold() == "exit":
                    break
                lama_peminjaman = int(input("Ingin melakukan peminjaman untuk berapa hari: "))
                if buku_pilihan.casefold() == "x-man":
                    harga = x_man * lama_peminjaman 
                elif buku_pilihan.casefold() == "doraemoh":
                    harga = doraemoh * lama_peminjaman 
                elif buku_pilihan.casefold() == "nartoh":
                    harga = nartoh * lama_peminjaman
                else:
                    print("Komik tidak ditemukan. Masukan kembali judul komik sesuai katalog!" + "\n")
                    continue

                if saldo < harga: 
                    print("Tidak berhasil meminjam! Saldo anda kurang", str(harga - saldo), "\n")
                elif saldo > harga:
                    saldo -= harga
                    print("Berhasil meminjam buku", buku_pilihan, "selama", str(lama_peminjaman), "hari",
                        "\nSaldo anda saat ini Rp" + str(saldo), "\n")
                
            
    # Program yang akan dijalankan jika user memilih opsi 2
    elif yang_ingin_dilakukan == 2:
        print("Terima kasih telah mengunjungi Toko Buku Place Anak Chill!")
        break # Menghentikna while loop dan program akan berhenti 
    
    # Jika user memilih bukan opsi 1 maupun 2, maka program akan berjalan
    else:
        print("Perintah tidak diketahui!")
        # Program akan otomatis kembali meminta yang ingin dilakukan karena masih dalam while loop
        