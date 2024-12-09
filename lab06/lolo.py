
# list_of_dicts = [
#     {"nama": "Alice", "age": 25},
#     {"nama": "Bob", "age": 30},
#     {"nama": "Charlie", "age": 27}
# ]

# yes = 0
# input = "Bob"


# for i in range(len(list_of_dicts)):
#     if input in list_of_dicts[i].values():
#         index = i

# print(index)



list1 = ['Variabel', 'Tipe', 'Data', 'Struktur', 'String', 'Integer', 'Float', 'Boolean', 'Pengulangan', 'Kondisi', 'Fungsi', 'Prosedur', 'Array', 'Pointer', 'Pemrograman', 'Berorientasi', 'Objek', 'Pengkodean', 'Logika', 'Kontrol', 'Versi', 'Algoritma', 'Class', 'Metode', 'Operasi', 'Input', 'Output', 'String', 'Integer', 'Float', 'Boolean']

list2 = ['OOP', 'Variabel', 'DataType', 'String', 'Integer', 'Float', 'List', 'Tuple', 'Dictionary', 'Rekursi', 'Kondisi', 'Fungsi', 'Modul', 'Class', 'Metode', 'Operasi', 'Input', 'Output', 'Logika', 'Komentar', 'File', 'Kode', 'Sintaks', 'Global', 'Local', 'Scope', 'Return', 'Rekursi', 'List', 'Tuple', 'Dictionary']

# Convert lists to sets for faster comparison
set1 = set(list1)
set2 = set(list2)

# Find the common words
common_words = set2.intersection(set1)
num_common_words = len(common_words)

print(f"The number of common words is: {num_common_words}")
print(f"The common words are: {common_words}")
