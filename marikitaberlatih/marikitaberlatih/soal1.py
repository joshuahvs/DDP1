
try:
    file = input("nama file: ")
    my_file = open(file, "r")
except FileNotFoundError:
    print("file tidak ditemukan")
    exit()

file_to_read = my_file.read().split()
counter = 0
for word in file_to_read:
    reversing = word[-1]
    if reversing != "a" and reversing != "i" and reversing != "u" and reversing != "e" and reversing != "o":
        counter += 1
print(f"Ada {counter} kata yang diakhiri huruf konsonan")