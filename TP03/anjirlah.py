import matplotlib.pyplot as plt

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
        for i in file: # Mengiterasi keseluruhan data
            counter += 1 # Untuk mengetahui pada baris ke berapa data tidak konsisten (jika tidak konsisten)
            data_split = i.strip('\n').split(delimiter) # split data menjadi sebuah list berdasarkan delimiter 
            if len(data_split) != len(header): # Mengecheck kekonsistenan panjang data
                raise Exception(f"Banyaknya kolom pada baris {counter} tidak konsisten.")
            else:
                data_types = ["str"] * len(header) # tipe data sebelum diubah
                # Mengiterasi data yang sudah di split untuk diubah tipe datanya (jika bisa)
                for index, cell in enumerate(data_split):
                    if data_types[index] == "str": 
                        try:
                            data_split[index] = int(cell)
                            data_types[index] = "int"
                        except ValueError: # Jika tidak berhasil mengubah ke interger
                            try:
                                data_split[index] = float(cell)
                                data_types[index] = "float"
                                has_float = True
                            except ValueError: # Jika tidak berhasil mengubah ke float
                                pass
                data.append(data_split)
        # Jika ada float di suatu kolom, maka mengubah semua data di kolom tersebut menjadi float
        if has_float == True:
                for i in range(len(data)):
                    data[i][index] = float(data[i][index])
                data_types[index] = "float"

    return (data, header, data_types)


def to_list(dataframe):
  return dataframe[0]

def get_column_names(dataframe):
  return dataframe[1]
  
def get_column_types(dataframe):
  return dataframe[2]

def head(dataframe, top_n = 10):
  """
  
    -- DIBUKA KE PESERTA --
  
    top_n baris pertama pada tabel!
  
    Mengembalikan string yang merupakan representasi tabel
    (top_n baris pertama) dengan format:
    
     kolom_1|     kolom_2|     kolom_3|     ...
    ------------------------------------------- 
    value_11|    value_12|    value_13|     ...
    value_21|    value_22|    value_23|     ...
    ...         ...         ...
    
    Space setiap kolom dibatasi hanya 15 karakter dan right-justified.
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    top_n (int): n, untuk penampilan top-n baris saja
    
    return (string): representasi string dari penampilan tabel.
    
    Jangan pakai print()! tetapi return string!
  """
  cols = get_column_names(dataframe)
  out_str = ""
  out_str += "|".join([f"{col:>15}" for col in cols]) + "\n"
  out_str += ("-" * (15 * len(cols) + (len(cols) - 1))) + "\n"
  for row in to_list(dataframe)[:top_n]:
    out_str += "|".join([f"{col:>15}" for col in row]) + "\n"
  return out_str
  
def info(dataframe):
  """
    Mengembalikan string yang merupakan representasi informasi
    dataframe dalam format:
    
    Total Baris = xxxxx baris
    
    Kolom          Tipe
    ------------------------------
    kolom_1        tipe_1
    kolom_2        tipe_2
    ...
    
    Space untuk kolom dan tipe adalah 15 karakter, left-justified
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    
    return (string): representasi string dari info dataframe    
  """
  # TODO: Implement
  pass

def satisfy_cond(value1, condition, value2):
  """
    -- DIBUKA KE PESERTA --
    
    parameter:
    value1 (tipe apapun yang comparable): nilai pertama
    condition (string): salah satu dari ["<", "<=", "==", ">", ">=", "!="]
    value2 (tipe apapun yang comparable): nilai kedua
    
    return (boolean): hasil perbandingan value1 dan value2
    
  """
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

def select_rows(dataframe, col_name, condition, value):
  """
  Mengembalikan dataframe baru dimana baris-baris sudah
  dipilih hanya yang nilai col_name memenuhi 'condition'
  terkait 'value' tertentu.
  
  Gunakan/Call fungsi satisfy_cond(value1, condition, value2) yang
  sudah didefinisikan sebelumnya!
  
  contoh:
    select_rows(dataframe, "umur", "<=", 50) akan mengembalikan
    dataframe baru dengan setiap baris memenuhi syarat merupakan
    item dengan kolom umur <= 50 tahun.
    
  Exceptions:
    1. jika col_name tidak ditemukan,
    
        raise Exception(f"Kolom {col_name} tidak ditemukan.")
        
    2. jika condition bukan salah satu dari ["<", "<=", "==", ">", ">=", "!="]
    
        raise Exception(f"Operator {condition} tidak dikenal.")
  
  parameter:
  dataframe (list, list, list): sebuah dataframe
  col_name (string): nama kolom sebagai basis untuk selection
  condition (string): salah satu dari ["<", "<=", "==", ">", ">=", "!="]
  value (tipe apapun): nilai untuk basis perbandingan pada col_name
  
  return (list, list, list): dataframe baru hasil selection atau filtering
  
  """
  # TODO: Implement
  pass
  
def select_cols(dataframe, selected_cols):
  """
    Mengembalikan dataframe baru dimana kolom-kolom sudah
    dipilih hanya yang terdapat pada 'selected_cols' saja.
    
    contoh:
    select_cols(dataframe, ["umur", "nama"]) akan mengembalikan
    dataframe baru yang hanya terdiri dari kolom "umur" dan "nama".
    
    Exceptions:
      1. jika ada nama kolom pada selected_cols yang tidak
         ditemukan, 
         
           raise Exception(f"Kolom {selected_col} tidak ditemukan.")
           
      2. jika select_cols adalah list kosong [],
      
           raise Exception("Parameter selected_cols tidak boleh kosong.")
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    selected_cols (list): list of strings, atau list yang berisi
                          daftar nama kolom
                          
    return (list, list, list): dataframe baru hasil selection pada
                               kolom, yaitu hanya mengandung kolom-
                               kolom pada selected_cols saja.
    
  """
  # TODO: Implement
  pass

def count(dataframe, col_name):
  """
    mengembalikan dictionary yang berisi frequency count dari
    setiap nilai unik pada kolom col_name.
    
    Tipe nilai pada col_name harus string !
    
    Exceptions:
      1. jika col_name tidak ditemukan,
      
           raise Exception(f"Kolom {col_name} tidak ditemukan.")
      
      2. jika tipe data col_name adalah numerik (int atau float),
      
           raise Exception(f"Kolom {col_name} harus bertipe string.")      
      
      3. jika tabel kosong, alias banyaknya baris = 0,
           
           raise Exception("Tabel kosong.")

    Peserta bisa menggunakan Set untuk mengerjakan fungsi ini.
           
    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name (string): nama kolom yang ingin dihitung rataannya
    
    return (dict): dictionary yang berisi informasi frequency count
                   dari setiap nilai unik.
  """
  # TODO: Implement
  pass

def mean_col(dataframe, col_name):
  """
    Mengembalikan nilai rata-rata nilai pada kolom 'col_name'
    di dataframe.
    
    Exceptions:
      1. jika col_name tidak ditemukan,
      
           raise Exception(f"Kolom {col_name} tidak ditemukan.")
      
      2. jika tipe data col_name adalah string,
      
           raise Exception(f"Kolom {col_name} bukan bertipe numerik.")      
      
      3. jika tabel kosong, alias banyaknya baris = 0,
           
           raise Exception("Tabel kosong.")
           
    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name (string): nama kolom yang ingin dihitung rataannya
    
    return (float): nilai rataan
  """
  # TODO: Implement
  pass
  
def show_scatter_plot(x, y, x_label, y_label):
  """
    -- DIBUKA KE PESERTA --
    
    parameter:
    x (list): list of numerical values, tidak boleh string
    y (list): list of numerical values, tidak boleh string
    x_label (string): label pada sumbu x
    y_label (string): label pada sumbu y
    
    return None, namun fungsi ini akan menampilkan scatter
    plot dari nilai pada x dan y.
    
    Apa itu scatter plot?
    https://chartio.com/learn/charts/what-is-a-scatter-plot/
  """
  plt.scatter(x, y)
  plt.xlabel(x_label)
  plt.ylabel(y_label)
  plt.show()
  
def scatter(dataframe, col_name_x, col_name_y):
  """
    fungsi ini akan menampilkan scatter plot antara kolom col_name_x
    dan col_name_y pada dataframe.
    
    pastikan nilai-nilai pada col_name_x dan col_name_y adalah angka!
    
    Exceptions:
      1. jika col_name_x tidak ditemukan,
      
           raise Exception(f"Kolom {col_name_x} tidak ditemukan.")
           
      2. jika col_name_y tidak ditemukan,
      
           raise Exception(f"Kolom {col_name_y} tidak ditemukan.")
           
      3. jika col_name_x BUKAN numerical,
      
           raise Exception(f"Kolom {col_name_x} bukan bertipe numerik.")
           
      4. jika col_name_y BUKAN numerical,
      
           raise Exception(f"Kolom {col_name_y} bukan bertipe numerik.")
    
    parameter:
    dataframe (list, list, list): sebuah dataframe
    col_name_x (string): nama kolom yang nilai-nilainya diplot pada axis x
    col_name_y (string): nama kolom yang nilai-nilainya diplot pada axis y
    
    Call fungsi show_scatter_plot(x, y) ketika mendefinisikan fungsi
    ini!
    
    return None
  """
  # TODO: Implement
  pass

if __name__ == "__main__":
  # TODO: Buat program yang memanfaatkan fungsi-fungsi di atas
  pass
  