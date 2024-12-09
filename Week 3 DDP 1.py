while True:
    id = input("Masukkan ID anda: ")
    jumlah_digit = sum(int(ids) for ids in id)

    if jumlah_digit == 23:
        print("Login member berhasil!")

        while True:
            print("============================================",
                "\nKatalog Buku Place Anak Chill",
                "\n============================================",
                "\nX-Man (Rp 7.000/hari)",
                "\nDoraemon (Rp 5.500/hari)",
                "\nNaruto (Rp 4.000/hari)",
                "\n============================================",
                "\nExit",
                "\n============================================")
            break
            # Your book catalog and menu logic here

    else:
        print("ID anda salah!")
        counter = 0
        while counter < 2:
            id = input("Masukkan ID anda: ")
            jumlah_digit = sum(int(ids) for ids in id)
            if jumlah_digit == 23:
                break
            else:
                print("ID anda salah!")
                counter += 1
        else:
            print("Anda telah salah memasukkan ID sebanyak 3 kali.")
            break

