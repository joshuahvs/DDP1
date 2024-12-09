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
            print(data_types[i])
            if data_types[i] == 'str': #Ubah semua data ke string
               pass
            elif data_types[i] == 'int': #ubah semua data ke int
               for j in range(len(data)):
                  data[j][i] = int(data[j][i])
            elif data_types[i] == 'float': #ubah semua data ke float
               for j in range(len(data)):
                  data[j][i] = float(data[j][i])       

    return (data, header, data_types)




lala = read_csv("test1 copy.csv")
print(lala[0])
print(lala[1])
print(lala[2])
