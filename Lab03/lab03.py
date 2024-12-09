# Mencetak selamat datang dan meminta file input dan output yang diingingkan 
while True:
    try:
        print("Selamat datang! Masukkan dua nama file yang berisi daftar makanan yang kamu miliki.")
        file_input = input("Masukkan nama file input daftar makanan: ")
        file_output = input("Masukkan nama file output: ")
        test_file_input = open(file_input, "r")
        test_file_output = open(file_output, "r")
    except FileNotFoundError:
        print("Maaf, file input tidak ada")
        continue
    else:
        break
test_file_input.close()
test_file_output.close()

customer = True

while customer == True:
    print("Apa yang ingin kamu lakukan?")
    print("================================================")
    print("1. Tampilkan daftar makanan pertama")
    print("2. Tampilkan daftar makanan kedua")
    print("3. Tampilkan gabungan makanan dari dua daftar")
    print("4. Tampilkan makanan yang sama dari dua daftar")
    print("5. Keluar")
    action = int(input("Masukkan aksi yang ingin dilakukan: "))

    if action == 1:
        in_file = open(file_input, "r")
        out_file = open(file_output, "a")
        first_line = in_file.readline()
        print(first_line)
        print(first_line, file = out_file)
        in_file.close()
        out_file.close()

    elif action == 2:
        in_file = open(file_input,"r")
        out_file = open(file_output, "a")
        in_file.readline()
        second_line = in_file.readline()
        print(second_line)
        print(second_line, file = out_file)
        in_file.close()
        out_file.close() 

    elif action == 3:
        in_file = open(file_input,"r")
        out_file = open(file_output, "a")
        first_line = in_file.readline()
        second_line = in_file.readline()
        keterangan = "Gabungan makanan favorit dari kedua daftar: "
        food_first_line = first_line[18:]
        food_second_line = second_line[18:]

        index = 0
        combine_food = ""
        for i in food_first_line:
            if i == ",":
                combine = food_first_line.find(",", index)
                # print(food_first_line[index:combine])
                index += combine +1
                combine_food += food_first_line[index:combine]

        print(combine_food)

        # coma = first_line.find(",")
        # food_first_line = food_first_line[18:18+coma]
        # print(food_first_line)
        # print(coma)
        
        in_file.close()
        out_file.close()
    

    elif action == 5:
        customer = False