import sys # Mengimport sys agar kita bisa melakukan command prompt

# Fungsi print headers yang akan memunculkan header
def print_headers():
    print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format("No", "Smartphone", "Price", "Screensize", "RAM")) # Mengeprint header dan menggunakan format agar code terprint dengan rapi
    print("================================================================")

# Fungsi yang akan memunculkan tabel list hp secara keseluruhan
def print_table(filename): #filename adalah parameternya
    with open(filename, "r") as opened_file: #Membuka file berdasarkan parameter yang diinput 
        print_headers() #memanggil fungsi print_headers yang akan memunculkan headers
        file_to_read = opened_file.readlines() #Membuka dengan metode readlines yang akan langsung membaca perbaris dan jadi list
        counter = 0 
        # Mengiterasi tiap line di file_to_read
        for line in file_to_read: 
            line_seperate = line.split("\t") # Memisahkan konten di list di saat ada tab("\t")
            smartphone = line_seperate[0] # Index smartphone di list adalah 0 
            price = line_seperate[1] # Index price di list adalah 1
            screensize = line_seperate[2] #Index screensize di list adalah 2
            ram = line_seperate[3].strip("\n") #Menggunakan strip untuk menghilankan spasi di index 3 yaitu ram 
            counter += 1 # Menambah counter
            # Mencetak list dengan menggunakan format agar rapi
            print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(counter, smartphone, price, screensize, ram))

# Fungsi untuk mencari hp berdasarkan parameter file dan keyword nama hp
def search_phone(filename, keyword):
    with open(filename, "r") as opened_file:
        print("\n")
        print_headers()
        file_to_read = opened_file.readlines()
        counter = 0
        for line in file_to_read:
            line_to_scan = line.casefold() #Menggunakan casefold agar semua huruf dijadikan huruf kecil, agar bersifat case insensitive
            keyword_to_search = keyword.casefold()
            if keyword_to_search in line_to_scan:
                line_seperate = line.split("\t")
                smartphone = line_seperate[0]
                price = line_seperate[1]
                screensize = line_seperate[2]
                ram = line_seperate[3].strip("\n")
                counter += 1
                print("| {: <2} | {: <25} | {: <8} | {: <10} | {: <3} |".format(counter, smartphone, price, screensize, ram))
        print(f"Ukuran data dari hasil pencarian: {counter}x4") # Mencetak jumlah data di file yang ditemukan mengandung keyword yang dicari

# Fungsi untuk mencari nilai min, nilai max, dan rata rata
def desc_stat(filename, column):
    with open(filename, "r") as opened_file:
        file_to_read = opened_file.readlines()
        finding_list = [] #List dibuat kosong dulu
        counter = 0
        for line in file_to_read:
            line_separate = line.split("\t")
            list_index = line_separate[column].strip("\n") #Menggunakan index agar yang diambil hanyalah yang diingikan oleh user
            finding_list.append(float(list_index)) #Untuk setiap iterasi, dimasukkan ke dalam list berupa float agar dapat dihitung
            counter += 1 
        min_value = min(finding_list) # Min untuk mencari nilai minimum di list
        max_value = max(finding_list) # Max untuk mencari nilai maximum di list
        total = sum(finding_list) # Sum untuk mencari nilai total dari seluruh angka di list
        mean = total/counter # Menghitung rata-ratanya
        print(f"Min data: {min_value:.2f}") #.2f adalah formating agar muncul 2 angka dibelakang koma
        print(f"Max data: {max_value:.2f}")
        print(f"Rata - rata: {mean:.2f}")

if __name__ == '__main__':
    if len(sys.argv) != 4: #program yang akan dijalankan jika jumlah prompt yang diinput di command prompt tidak 4
        print("Usage: python script_name.py <file_path> <search_keyword> <column_num>")
        sys.exit(1)
    # Mendefinisikan variabel berdasarkan command prompt
    file_path = sys.argv[1]
    key = sys.argv[2]
    column_num = int(sys.argv[3])

    # Memanggil fungsi fungsi yang sudah dibuat diatas
    try:
        print_table(file_path)
        search_phone(file_path, key)
        desc_stat(file_path, column_num)
    except FileNotFoundError: # Menggunakan try dan except yang dapat memunculkan pesan jika file yang ingin dibuka tidak ditemukan
        print("Maaf, file input tidak ada")
    except IndexError:
        print("Maaf, kolom yang diinput tidak valid")

# program selesai