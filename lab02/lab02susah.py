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

    if yang_ingin_dilakukan == 1:
        nama = input("Masukkan nama anda: ")
        saldo = int(input("Masukkan saldo anda (Rp): "))
        member = input("Apakah anda member? [Y/N]: ")
        if member == "Y":
            id = input("Masukkan ID anda: ")
            jumlah_digit = sum(int(ids) for ids in id)
            # Menggunakan for loop untuk menghitung jumlah digit dari ID
            if jumlah_digit != 23:
                counter = 0
                while counter < 2:
                    print("ID anda salah!")
                    id = input("Masukkan ID anda: ")
                    jumlah_digit = sum(int(ids) for ids in id)
                    counter += 1
                else:
                    print("ID anda salah!")
                    print("Program akan kembali ke menu utama")
                    break

            elif jumlah_digit == 23:
                print("Login member berhasil!")
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
                        harga = x_man * lama_peminjaman * 0.8
                    elif buku_pilihan.casefold() == "doraemoh":
                        harga = doraemoh * lama_peminjaman * 0.8
                    elif buku_pilihan.casefold() == "nartoh":
                        harga = nartoh * lama_peminjaman * 0.8
                    saldo -= harga
                    print("Berhasil meminjam buku", buku_pilihan, "selama", str(lama_peminjaman), "hari",
                        "\nSaldo anda saat ini Rp" + str(saldo))

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
                    print("Komik tidak ditemukan. Masukan kembali judul komik sesuai katalog!")
                    continue

                if saldo <= harga: 
                    print("Tidak berhasil meminjam! Saldo anda kurang", str(harga - saldo))
                    continue
                elif saldo >= harga:
                    saldo -= harga
                print("Berhasil meminjam buku", buku_pilihan, "selama", str(lama_peminjaman), "hari",
                    "\nSaldo anda saat ini Rp" + str(saldo))
                
            

    elif yang_ingin_dilakukan == 2:
        print("Terima kasih telah mengunjungi Toko Buku Place Anak Chill!")
        break
    
    else:
        print("Perintah tidak diketahui!")
        