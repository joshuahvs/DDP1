import matplotlib.pyplot as plt #Mengimport library matplotlib

# Fungsi yang akan mengembalikan tipe dari sebuah string (SUDAH DIDEFINISIKAN)
def get_type(a_str):
    try:
        int(a_str)
        return "int"
    except:
        try:
            float(a_str)
            return "float"
        except:
            return "str"

# Fungsi untuk membaca keseluruhan file, dan mereturn tuple berisi data, header, dan tipe kolom
def read_csv(file_name, delimiter = ','):
    data = []
    header = []
    data_types = []
    
    with open(file_name, "r") as file: 
        # Memasukkan data per row yang sudah di proses ke list ke dalam list data
        reading = file.readlines() 
        for i in reading:
            splitting = i.strip('\n').split(delimiter)
            data += [splitting]
        # Memisahkan header dari list data
        header += data[0]
        data.pop(0)
        # Mengecheck panjang tiap baris
        counter = 1
        for i in data:
            counter += 1
            if len(i) != len(header):
                raise Exception(f"Banyaknya kolom pada baris {counter} tidak konsisten.")
            
        # Mengecheck setiap tipe data dari keseluruhan data per kolum
        temp_data_types = []
        for i in range(len(data)):
            tipe_sementara = [] 
            for j in range(len(header)):
                tipe = get_type(data[i][j])
                tipe_sementara.append(tipe)
            temp_data_types.append(tipe_sementara)

        # Menentukan tipe data yang akan dimasukkan ke dalam data_types berdasarkan data per kolum yang sudah di check
        for i in range(len(header)):
            to_check = []
            for j in range(len(data)):
                to_check += [temp_data_types[j][i]]
            if 'str' in to_check:
               data_types.append('str')
            elif 'float' in to_check and 'int' not in to_check:
               data_types.append('float')
            elif 'int'in to_check and 'float'in to_check:
               data_types.append('float')
            elif 'int' in to_check and 'float' not in to_check:
               data_types.append('int')
        
        # Mengubah keseluruhan tipe data di list data berdasarkan data_types
        for i in range(len(data_types)):
            if data_types[i] == 'str': #tidak usah diubah
               pass
            elif data_types[i] == 'int': #ubah semua data ke int
               for j in range(len(data)):
                  data[j][i] = int(data[j][i])
            elif data_types[i] == 'float': #ubah semua data ke float
               for j in range(len(data)):
                  data[j][i] = float(data[j][i])       

    return (data, header, data_types)

# Mengembalikan data (SUDAH DIDEFINISIKAN)
def to_list(dataframe):
    return dataframe[0]
# Mengembalikan header atau nama kolom (SUDAH DIDEFINISIKAN)
def get_column_names(dataframe):
    return dataframe[1]
# Mengembalikan tipe data (SUDAH DIDEFINISIKAN)
def get_column_types(dataframe):
    return dataframe[2]

# Fungsi yang mengembalikan data berupa tabel (SUDAH DIDEFINISIKAN)
def head(dataframe, top_n = 10):
    cols = get_column_names(dataframe)
    out_str = ""
    out_str += "|".join([f"{col:>15}" for col in cols]) + "\n"
    out_str += ("-" * (15 * len(cols) + (len(cols) - 1))) + "\n"
    for row in to_list(dataframe)[:top_n]:
        out_str += "|".join([f"{col:>15}" for col in row]) + "\n"
    return out_str

# Fungsi ini mengembalikan nama kolom dan tipe datanya berupa representasi tabel dan total jumlah barisnya
def info(dataframe):
    # Informasi yang akan di return
    data = to_list(dataframe)
    total_rows = len(data)
    column_names = get_column_names(dataframe)
    types = get_column_types(dataframe)
    kolom = "Kolom"
    tipe = "Tipe"
    # Mereturn total baris, dan tabel yang sudah di format
    to_return = f"Total Baris = {total_rows} Baris\n\n"
    to_return += f"{kolom[:15]:<15} {tipe[:15]:<15}\n"
    to_return += "------------------------------\n"
    # Mengiterasi data dari column names/header dan mencetaknya serta tipe datanya
    for i in range(len(column_names)):
        to_return += f"{column_names[i][:15]:<15} {types[i][:15]:<15}\n"
    
    return to_return

# Fungsi yang akan mengembali hasil perbandingan dari value 1 dan value 2 (SUDAH DIDEFINISIKAN)
def satisfy_cond(value1, condition, value2):
    if condition == "<":
        return value1 < value2
    elif condition == "<=":
        return value1 <= value2
    elif condition == ">":
        return value1 > value2
    elif condition == ">=":
        return value1 >= value2
    elif condition == "!=":
        return value1 != value2
    elif condition == "==":
        return value1 == value2
    else:
        raise Exception(f"Operator {condition} tidak dikenal.")
    
# Fungsi yang mengembalikan dataframe baru yang memenuhi condition
def select_rows(dataframe, col_name, condition, value):
    new_data = [] # data baru yang akan di return
    header = get_column_names(dataframe)
    # Mengecek apakah ada kolom dengan nama yang diinginkan
    try:
        indexnya = header.index(col_name) 
    except ValueError:
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
    # Mengecek apakah condition sesuai
    if condition not in ["<", "<=", "==", ">", ">=", "!="]:
        raise Exception(f"Operator {condition} tidak dikenal.")
    types = get_column_types(dataframe)
    data = to_list(dataframe)
    # Mencari row-row yang memenuhi kondisi dan menambahkannya ke new_data
    for i in range(len(data)):
        to_scan = data[i][indexnya] #value 1 yang akan dibandingkan
        if satisfy_cond(to_scan, condition, value):
            to_append = data[i]
            new_data.append(to_append)
    return (new_data, header, types)

# Fungsi yang akan mengembalikan dataframe baru dengan kolom yang dipilih saja
def select_cols(dataframe, selected_cols):
    # Mengecek apakah parameter kosong
    if select_cols == [] or select_cols is None:
        raise Exception("Parameter selected_cols tidak boleh kosong.")
    new = []
    lst_index = []
    header = get_column_names(dataframe)
    col_in_header = False
    data = to_list(dataframe)
    # Mengecheck kolom yang diinginkan di header, jika ada, maka simpan indexnya
    for col in selected_cols:
        if col in header:
            col_in_header = True
            indexnya = header.index(col)
            lst_index.append(indexnya)
    # jika kolum tidak ada di header
    if col_in_header == False:
        raise Exception(f"Kolom {selected_cols} tidak ditemukan.")
    # Mengiterasi data, dan memasukkan data dari kolom yang dipilih ke new
    for i in range(len(data)):
        temporary = []
        for j in lst_index:
            to_append = data[i][j]
            temporary.append(to_append)
        new.append(temporary)
    types = get_column_types(dataframe)
    new_types = []
    # Memasukkan tipe data dari kolom yang dipilih 
    for j in lst_index:
        new_types.append(types[j])
    return (new, selected_cols, new_types)

# Fungsi yang akan mengembalikan dictionary berupa frequency count dari setiap nilai unik di suatu kolom
def count(dataframe, col_name):
    header = get_column_names(dataframe)
    types = get_column_types(dataframe)
    # Mengecek apakah ada kolom dengan nama yang diinginkan
    try:
        index = header.index(col_name)
    except ValueError:
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
    # Mengecek apakah tipe datanya sesuai
    if types[index] == "int" or types[index] == "float":
        raise Exception(f"Kolom {col_name} harus bertipe string.")
    dict = {}
    data = to_list(dataframe)
    # Mengiterasi isi data
    for i in data:
        key = i[index] # index berdasarkan kolom yang diminta 
        # Menghitung setiap nilai unik 
        if key in dict.keys():
            dict[key] += 1
        else:
            dict[key] = 1
    # Jika tabel kosong
    if dict == {}:
        raise Exception("Tabel kosong.")
    return dict

# Fungsi yang mengembalikan float berupa nilai rata-ratanya
def mean_col(dataframe, col_name):
    header = get_column_names(dataframe)
    types = get_column_types(dataframe)
    # Mengecek kolom yang diinginkan
    try:
        index = header.index(col_name)
    except ValueError:
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
    # Mengecek tipe data dari kolom yang diinginkan 
    if types[index] == "str":
        raise Exception(f"Kolom {col_name} bukan bertipe numerik.") 
    data = to_list(dataframe)  
    counter = 0
    total = 0
    # Mengiterasi keseluruhan data dan menambah nilai count dan total
    for i in range(len(data)):
        counter += 1
        total += (data[i][index])
    # Mencari nilai rata-ratanya
    mean = total/counter
    return mean

# Fungsi yang akan menampilkan scatter plot dari parameter x dan y (SUDAH DIDEFINISIKAN)
def show_scatter_plot(x, y, x_label, y_label):
    plt.scatter(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()

# Fungsi yang akan menyeleksi data dan menampilkan scatter plot
def scatter(dataframe, col_name_x, col_name_y):
    header = get_column_names(dataframe)
    data = to_list(dataframe)
    types = get_column_types(dataframe)
    x = []
    y = []
    # Mengecek apakah kolom x di header
    if col_name_x not in header:
        raise Exception(f"Kolom {col_name_x} tidak ditemukan.")
    # Mengecek apakah kolom y di header
    if col_name_y not in header:
        raise Exception(f"Kolom {col_name_y} tidak ditemukan.")
    index_x = header.index(col_name_x)
    index_y = header.index(col_name_y)
    # Mengecek tipe data dari kolom x
    if types[index_x] != 'float' and types[index_x] != 'int':
        raise Exception(f"Kolom {col_name_x} bukan bertipe numerik.")
    # Mengecek tipe data dari kolom y
    if types[index_y] != 'float' and types[index_y] != 'int':
        raise Exception(f"Kolom {col_name_y} bukan bertipe numerik.")
    # Mengiterasi datanya dan memasukkannya ke dalam list lalu memanggil fungsi untuk menampilkan scatter plotnya
    for i in range(len(data)):
        x.append(data[i][index_x])
        y.append(data[i][index_y])
    show_scatter_plot(x, y, col_name_x, col_name_y)
    return None
  
# FITUR BONUS
# Fungsi yang menambahkan keseluruhan angka di suatu kolom 
def total_col(dataframe, col_name):
    header = get_column_names(dataframe)
    types = get_column_types(dataframe)
    # Mengecek kolom yang diinginkan
    try:
        index = header.index(col_name)
    except ValueError:
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
    # Mengecek tipe data dari kolom yang diinginkan 
    if types[index] == "str":
        raise Exception(f"Kolom {col_name} bukan bertipe numerik.") 
    data = to_list(dataframe)  
    total = 0
    # Mengiterasi keseluruhan data dan menambah nilai count dan total
    for i in range(len(data)):
        total += (data[i][index])
    # Mencari nilai total suatu kolum
    return f"Total bilangan di kolom {col_name} adalah {total}"

# FITUR BONUS
# Mencari modus di suatu kolom
def mode_col(dataframe, col_name):
    dictionary = count(dataframe, col_name)

    for i in dictionary.keys():
        if dictionary[i] == max(dictionary.values()):
            return f"Modus dari kolom {col_name} andalah {i}"



if __name__ == "__main__":
    # Memuat dataframe dari tabel abalone.csv
    dataframe = read_csv("abalone.csv")

    # Mencetak 10 baris pertama
    print(head(dataframe, top_n = 10))

    # Cetak informasi dataframe
    print(info(dataframe))

    #  kembalikan dataframe baru, dengan  kolom Length > 0.49
    new_dataframe = select_rows(dataframe, "Length", ">", 0.49)
    print(head(new_dataframe, top_n = 5))

    # kembalikan dataframe baru, dimana Sex == "M" DAN Length > 0.49
    new_dataframe = select_rows(select_rows(dataframe, "Length",">", 0.49), "Sex", "==", "M")
    print(head(new_dataframe, top_n = 5))

    # kembalikan dataframe baru yang hanya terdiri dari kolom Sex, Length, Diameter, dan Rings
    new_dataframe = select_cols(dataframe, ["Sex", "Length","Diameter", "Rings"])
    print(head(new_dataframe, top_n = 5))

    # hitung mean pada kolom Length (pada dataframe original)
    print(mean_col(dataframe, "Length"))

    # melihat unique values pada kolom Sex, dan frekuensi kemunculannya (pada dataframe original)
    print(count(dataframe, "Sex"))

    # Menghitung total angka di suatu kolom
    print(total_col(dataframe, "Length"))

    # Mencari modus di suatu kolom
    print(mode_col(dataframe, "Sex"))

    # tampilkan scatter plot antara kolom "Height" dan "Diameter"
    scatter(dataframe, "Height", "Diameter")


