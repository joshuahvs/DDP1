def read_csv(file_name, delimiter = ','):
    #list data, header, dan tipe datanya
    data = []
    header = []
    data_types = []
    # Membuka file dan membacanya
    with open(file_name, "r") as file:
        read_first_line = file.readline()
        header += read_first_line.strip('\n').split(delimiter) # Membaca bagian header
        counter = 1
        has_float = False
        # has_str = False
        for i in file: # Mengiterasi keseluruhan data
            counter += 1 # Untuk mengetahui pada baris ke berapa data tidak konsisten (jika tidak konsisten)
            data_split = i.strip('\n').split(delimiter) # split data menjadi sebuah list berdasarkan delimiter 
            if len(data_split) != len(header): # Mengecheck kekonsistenan panjang data
                raise Exception(f"Banyaknya kolom pada baris {counter} tidak konsisten.")
            else:
                data_types = ["str"] * len(header) # tipe data sebelum diubah
                # Mengiterasi data yang sudah di split untuk diubah tipe datanya (jika bisa)
                temp_list = [] # temporary list to store converted values
                for index, cell in enumerate(data_split):
                    if data_types[index] == "str": 
                        try:
                            temp_list.append(int(cell)) # append int value to temp list
                        except ValueError: # Jika tidak berhasil mengubah ke interger
                            try:
                                temp_list.append(float(cell)) # append float value to temp list
                                has_float = True
                            except ValueError: # Jika tidak berhasil mengubah ke float
                                # has_str = False
                                temp_list.append(cell) # append string value to temp list
                    else:
                        temp_list.append(cell) # append value without conversion
                data.append(temp_list) # append temp list to data list

                # data.append(data_split)
            # Jika ada float di suatu kolom, maka mengubah semua data di kolom tersebut menjadi float
                if has_float == True:
                    try:
                        for i in range(len(data)):
                            data[i][index] = float(data[i][index])
                        data_types[index] = "float"
                    except ValueError:
                        for i in range(len(data)):
                            data[i][index] = str(data[i][index])
                        data_types[index] = "str"

    return (data, header, data_types)

lala = read_csv("test2.csv")
print(lala[0])
print(lala[1])
print(lala[2])
