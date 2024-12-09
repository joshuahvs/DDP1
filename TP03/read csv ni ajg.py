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
    
def read_csv(file_name, delimiter=','):
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

        for list in data:
            counter += 1
            if len(list) != len(header):
                raise Exception(f"Banyaknya kolom pada baris {counter} tidak konsisten.")
            else:
               for items in list:
                  if get_type(items) == 'str':
                     try:
                        
    
