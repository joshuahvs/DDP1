# Menggunakan while loop agar program mengulang jika file yang di input tidak ditemukan 
while True:
    # menggunakan try dan except untuk mencoba dan bila file tidak ditemukan maka file akan mengulang 
    try:
        # Mencetak selamat datang dan juga meminta input file dan juga output file 
        print("Selamat datang! Masukkan dua nama file yang berisi daftar makanan yang kamu miliki.")
        file_input = input("Masukkan nama file input daftar makanan: ")
        file_output = input("Masukkan nama file output: ")
        test_file_input = open(file_input, "r") # membuka file 
        test_file_output = open(file_output, "r")
    # akan dijalankan bila file tidak ditemukan
    except FileNotFoundError:
        print("Maaf, file input tidak ada")
        continue
    # kalau file ditemukan maka program akan keluar dari loop dan menjalankan perintah selanjutnya 
    else:
        break
#menutup file yang dibuka tadi 
test_file_input.close()
test_file_output.close()

# Menggunakan while loop agar program terus berjalan bila user tidak memilih untuk keluar dari program 
customer = True
while customer == True:
    #Mencetak menu utama dan meminta input action yang akan dijalankan
    print("Apa yang ingin kamu lakukan?")
    print("================================================")
    print("1. Tampilkan daftar makanan pertama")
    print("2. Tampilkan daftar makanan kedua")
    print("3. Tampilkan gabungan makanan dari dua daftar")
    print("4. Tampilkan makanan yang sama dari dua daftar")
    print("5. Keluar")
    action = int(input("Masukkan aksi yang ingin dilakukan: "))

    # program yang akan dijalankan bila user memilih 1 
    if action == 1:
        in_file = open(file_input, "r") # "r" untuk membaca
        out_file = open(file_output, "a") # "a" untuk menambahkan text ke file output
        first_line = in_file.readline() # membaca line pertama di file
        print(first_line) # mencetak line pertama
        print(first_line, file = out_file) # memasukkan hasil cetak line pertama di file output
        in_file.close() #.close untuk menutup file 
        out_file.close()

    elif action == 2:
        in_file = open(file_input,"r")
        out_file = open(file_output, "a")
        in_file.readline() #mencetak line pertama 
        second_line = in_file.readline() #mencetak line kedua
        print(second_line)
        print(second_line, file = out_file)
        in_file.close()
        out_file.close() 

    elif action == 3:
        in_file = open(file_input,"r")
        out_file = open(file_output, "a")
        first_line = in_file.readline()
        second_line = in_file.readline()
    
        food_first_line = first_line[18:]
        food_second_line = second_line[18:]
        index = 0
        combine_food = ""
        for i in food_first_line:
            if i == ",":
                combine = food_first_line.find(",", index)
                food_checking = food_first_line[index:combine]
                print(food_checking)
                combine_food += food_checking + ","
                index = combine +1

        for j in food_second_line:
            if j == ",":
                combine = food_first_line.find(",", index)
                food_checking = food_first_line[index:combine]
                print(food_checking)
                combine_food += food_checking + ","
                index = combine +1

        print("Gabungan makanan favorit dari kedua daftar: ", combine_food)
    
        in_file.close()
        out_file.close()

    elif action == 4:
        in_file = open(file_input,"r")
        out_file = open(file_output, "a")
        first_line = in_file.readline()
        second_line = in_file.readline()
    
        food_first_line = first_line[18:]
        food_second_line = second_line[18:]
        index = 0
        combine_food = ""
        same_food = ""
        for i in first_line:
            if i == ",":
                combine = food_first_line.find(",", index)
                food_checking = food_first_line[index:combine]
                print(food_checking)
                combine_food += food_checking + ","
                index = combine +1
                if food_checking in combine_food:
                    same_food += food_checking
        for j in food_second_line:
            if j == ",":
                combine = food_first_line.find(",", index)
                food_checking = food_first_line[index:combine]
                print(food_checking)
                combine_food += food_checking + ","
                index = combine +1
        print("Makanan yang sama dari dua daftar: ")




    # menyetel customer = false, agar program berhenti 
    elif action == 5:
        customer = False


    # agar bila input yang dimasukkan customer tidak ada dalam pilihan menu, maka program akan meminta input lagi
    else:
        action = int(input("Masukkan aksi yang ingin dilakukan: "))