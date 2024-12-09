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
    data = []
    header = []
    data_types = []

    with open(file_name, "r") as file:
        reading = file.readlines()
        for i in reading:
            splitting = i.strip('\n').split(delimiter)
            data += [splitting]
        header += data[0]
        data.pop(0)
        counter = 1
        for i in data:
            counter += 1
            if len(i) != len(header):
                raise Exception(f"Banyaknya kolom pada baris {counter} tidak konsisten.")
    
        temp_data_types = []
        for i in range(len(data)):
            tipe_sementara = [] 
            for j in range(len(header)):
                tipe = get_type(data[i][j])
                tipe_sementara.append(tipe)
            temp_data_types.append(tipe_sementara)  

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
        
        for i in range(len(data_types)):
            if data_types[i] == 'str': #Ubah semua data ke string
               pass
            elif data_types[i] == 'int': #ubah semua data ke int
               for j in range(len(data)):
                  data[j][i] = int(data[j][i])
            elif data_types[i] == 'float': #ubah semua data ke float
               for j in range(len(data)):
                  data[j][i] = float(data[j][i])       

    return (data, header, data_types)


def to_list(dataframe):
  return dataframe[0]

def get_column_names(dataframe):
  return dataframe[1]
  
def get_column_types(dataframe):
  return dataframe[2]



def head(dataframe, top_n = 10):
  cols = get_column_names(dataframe)
  out_str = ""
  out_str += "|".join([f"{col:>15}" for col in cols]) + "\n"
  out_str += ("-" * (15 * len(cols) + (len(cols) - 1))) + "\n"
  for row in to_list(dataframe)[:top_n]:
    out_str += "|".join([f"{col:>15}" for col in row]) + "\n"
  return out_str

  
def info(dataframe):
  data = to_list(dataframe)
  total_rows = len(data)
  
  column_names = get_column_names(dataframe)
  types = get_column_types(dataframe)
  kolom = "Kolom"
  tipe = "Tipe"
  to_return = f"Total Baris = {total_rows} Baris\n\n"
  to_return += f"{kolom[:15]:<15} {tipe[:15]:<15}\n"
  to_return += "------------------------------\n"
  for i in range(len(column_names)):
    to_return += f"{column_names[i][:15]:<15} {types[i][:15]:<15}\n"
  
  return to_return

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
  
def select_rows(dataframe, col_name, condition, value):
  new = []
  header = get_column_names(dataframe)
  types = get_column_types(dataframe)
  try:
    indexnya = header.index(col_name) 
  except ValueError:
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  if condition not in ["<", "<=", "==", ">", ">=", "!="]:
    raise Exception(f"Operator {condition} tidak dikenal.")
  data = to_list(dataframe)
  for i in range(len(data)):
     to_scan = data[i][indexnya]
     if satisfy_cond(to_scan, condition, value):
        to_append = data[i]
        new.append(to_append)
  return (new, header, types)


def select_cols(dataframe, selected_cols):
  if select_cols == []:
    raise Exception("Parameter selected_cols tidak boleh kosong.")
  new = []
  lst_index = []
  header = get_column_names(dataframe)
  types = get_column_types(dataframe)
  new_types = []
  col_in_header = False
  data = to_list(dataframe)
  for col in selected_cols:
    if col in header:
      col_in_header = True
      indexnya = header.index(col)
      lst_index.append(indexnya)
  if col_in_header == False:
      raise Exception(f"Kolom {selected_cols} tidak ditemukan.")
  for i in range(len(data)):
      temporary = []
      for j in lst_index:
        to_append = data[i][j]
        temporary.append(to_append)
      new.append(temporary)  
  for j in lst_index:
      new_types.append(types[j])
  return (new, selected_cols, new_types)


def count(dataframe, col_name):
  header = get_column_names(dataframe)
  dict = {}
  types = get_column_types(dataframe)
  try:
    index = header.index(col_name)
  except ValueError:
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  if types[index] == "int" or types[index] == "float":
    raise Exception(f"Kolom {col_name} harus bertipe string.")   
  data = to_list(dataframe)
  for i in data:
    var = i[index]
    if var in dict.keys():
      dict[var] += 1
    else:
      dict[var] = 1
  if dict == {}:
    raise Exception("Tabel kosong.")
  return dict

def mean_col(dataframe, col_name):
  header = get_column_names(dataframe)
  print(header)
  types = get_column_types(dataframe)
  try:
    index = header.index(col_name)
  except ValueError:
    raise Exception(f"Kolom {col_name} tidak ditemukan.")
  if types[index] == "str":
    raise Exception(f"Kolom {col_name} bukan bertipe numerik.")   
  data = to_list(dataframe)
  counter = 0
  total = 0
  for i in range(len(data)):
    counter += 1
    total += (data[i][index])
  mean = total/counter
  return mean


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
  header = get_column_names(dataframe)
  data = to_list(dataframe)
  types = get_column_types(dataframe)
  x = []
  y = []
  if col_name_x not in header:
    raise Exception(f"Kolom {col_name_x} tidak ditemukan.")
  if col_name_y not in header:
    raise Exception(f"Kolom {col_name_y} tidak ditemukan.")
  index_x = header.index(col_name_x)
  index_y = header.index(col_name_y)
  if types[index_x] != 'float' and types[index_x] != 'int':
    raise Exception(f"Kolom {col_name_x} bukan bertipe numerik.")
  if types[index_y] != 'float' and types[index_y] != 'int':
    raise Exception(f"Kolom {col_name_y} bukan bertipe numerik.")
  for i in range(len(data)):
     x.append(data[i][index_x])
     y.append(data[i][index_y])
  show_scatter_plot(x, y, col_name_x, col_name_y)
  return None
  



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
  dataframe = read_csv("abalone.csv")
  # print(head(dataframe))
  # print(info(dataframe))
  new_dataframe = select_cols(dataframe, ["Length", "Diameter", "Rings"])
  # print(new_dataframe[0])
  # print(new_dataframe[1])
  # print(new_dataframe[2])
  # print(info(select_cols(dataframe, ["Length", "Diameter", "Rings"])))
  # print(head(select_cols(dataframe, ["Length", "Diameter", "Rings"]), top_n=5))
  scatter(dataframe, "Length", "Diameter")
  # print(count(dataframe, 'Sex'))



# count(dataframe, "Sex")
# print(mean_col(dataframe,'Diameter'))
