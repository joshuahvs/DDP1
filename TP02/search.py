import sys # Mengimport sys agar bisa membaca command prompt dan kita bisa memanfaatkan list dan indexnya dari command prompt
import os # Mengimport os untuk ngebuka folder dokumen satu per satu
import time # Mengimport time untuk digunakan sebagai timer

start_time = time.time() #Menggunakan time untuk mencatat waktu dan memulai timer 

#Validasi kesalahan input 
if len(sys.argv) == 1: #Supaya program tidak mengeluarkan output sebelum dimasukkan command prompt
    sys.exit(1) #Program akan berhenti 
if len(sys.argv) == 3: #program yang akan dijalankan bila panjang list dari command prompt adalah 3
    section = sys.argv[1] #menyetel variable berdasarkan command prompt
    start_section = "<"+section+">" #membuat start dan end seperti sesuai dengan file di dataset
    end_section = "</"+section+">"
    words_to_find = sys.argv[2]
elif len(sys.argv) == 5: #program yang akan dijalankan bila panjang list dari command prompt adalah 5
    section = sys.argv[1]
    start_section = "<"+section+">"
    end_section = "</"+section+">"
    words_to_find = sys.argv[2]
    command = sys.argv[3]
    words_to_find2 = sys.argv[4]
else: #apabila panjang list dari command prompt bukan 3 dan 5 maka argument tidak benar
    print("Argumen program tidak benar.") # Mencetak pesan argumen tidak benar
    sys.exit(1) # program akan keluar
    
folder_path = "/Users/joshuahansvito/Documents/DDP 1/TP02/dataset" #Menyetel path dari folder data set (diganti sesuai dengan path folder yang ingin dibuka)
documents_count = 0 

#Membuat fitur bonus yaitu progress bar
total_file = len(os.listdir(folder_path)) #total file yang ada di folder dataset
def progress_percentage(iteration): #iteration sebagai parameter yang akan diinput ketika memanggil fungsi 
    percent = float((iteration/total_file)*100) #melakukan kalkulasi percent
    bar = "="* int(percent) + " "* int((100-percent)) #membuat barnya
    print(f"\r|{bar}| {percent:.2f}%", end="\r") #mencetak bar

# Membuka dan mengiterasi semua file di folder dengan menggunakan os.listdir
for i, all_file in enumerate(os.listdir(folder_path)):
    file_full_path = os.path.join(folder_path, all_file) #Menambahkan folder path didepan setiap file agar dapat dibuka
    # Membuka file dengan with open
    with open(file_full_path, "r") as opened_file:
        file_to_read = opened_file.read().replace("\n", " ") # Membaca filenya lalu mengganti setiap enter dengan koma agar dapat dibaca 
        #Menggunakan metode find untuk mencari daerah yang harus di scan
        start_index = file_to_read.find(start_section)
        end_index = file_to_read.find(end_section)
        #Mencari provinsi di file tersebut
        provinsi_start_index = file_to_read.find("provinsi=")
        provinsi_end_index = file_to_read.find("status")
        #Mencari klasifikasi di file tersebut
        klasifikasi_start_index = file_to_read.find("klasifikasi=")
        klasifikasi_end_index = file_to_read.find("lama_hukuman")
        #Mencari sub klasifikasi di file tersebut
        sub_klasifikasi_start_index = file_to_read.find("sub_klasifikasi")
        sub_klasifikasi_end_index = file_to_read.find("url")
        #Mencari lembaga peradilan di file tersebut
        lembaga_peradilan_start_index = file_to_read.find("lembaga_peradilan")
        lembaga_peradilan_end_index = file_to_read.find("provinsi")

        if section == "all":
            file_to_scan = file_to_read #Jika user mengiput all maka program akan membaca keseluruhan file
        else:
            file_to_scan = file_to_read[start_index:end_index] #selain itu, program akan membaca di section yang ditentukan oleh user
        provinsi = file_to_read[provinsi_start_index +10 :provinsi_end_index-2] #Menggunakan metode slicing untuk mengambil nama provinsi
        klasifikasi = file_to_read[klasifikasi_start_index+13:klasifikasi_end_index-2] #Metode slicing untuk mengambil klasifikasi 
        sub_klasifikasi = file_to_read[sub_klasifikasi_start_index+17:sub_klasifikasi_end_index-2] #Metode slicing untuk mengambil sub klasifikasi
        lembaga_peradilan  = file_to_read[lembaga_peradilan_start_index+19:lembaga_peradilan_end_index-2] #Metode slicing untuk mengambil lembaga peradilan 

        if len(sys.argv) == 3: # Program akan dijalankan ketika panjang list adalah 3
            if words_to_find in file_to_scan: # Ketika kata yang dicari ada di dalam file...
                documents_count += 1 # menambah jumlah dokumen agar dapat dihitung berapa dokumen yang mengandung kata yang dicari 
                print(f"{all_file} {provinsi[:15]:>15} {klasifikasi[:15]:>15} {sub_klasifikasi[:30]:>30} {lembaga_peradilan[:20]:>20}")
        elif len(sys.argv) == 5: # program akan dijalankan ketika panjang list adalah 5
            if command.casefold() == "and": #jika user mengguknakan AND
                if words_to_find in file_to_scan and words_to_find2 in file_to_scan:
                    documents_count += 1
                    #Mengeprint nama file, provinsi, klasifikasi, sub klasifikasi, dan juga lembaga peradilannya, dan dilakukan format agar rapi.
                    print(f"{all_file} {provinsi[:15]:>15} {klasifikasi[:15]:>15} {sub_klasifikasi[:30]:>30} {lembaga_peradilan[:20]:>20}")
            elif command.casefold() == "or": #Jika user menggunakan OR
                if words_to_find in file_to_scan or words_to_find2 in file_to_scan:
                    documents_count += 1
                    print(f"{all_file} {provinsi[:15]:>15} {klasifikasi[:15]:>15} {sub_klasifikasi[:30]:>30} {lembaga_peradilan[:20]:>20}")
            elif command.casefold() == "andnot": #Jika user menggunakan kata ANDNOT
                if words_to_find in file_to_scan and words_to_find2 not in file_to_scan:
                    documents_count += 1
                    print(f"{all_file} {provinsi[:15]:>15} {klasifikasi[:15]:>15} {sub_klasifikasi[:30]:>30} {lembaga_peradilan[:20]:>20}")
            else: #selain AND, OR atau ANDNOT maka program akan menampilkan pesan ini dan keluar dari program
                print("Mode harus berupa AND, OR, atau ANDNOT.")
                sys.exit(1)
    progress_percentage(i+1) #Memanggil fungsi progress
    
end_time = time.time() #Mengakhiri timer 
total_time = end_time - start_time # Menghitung waktu yang dibutuhkan program untuk menjalankan program
spasi = " " * 70
print(f"Banyaknya dokumen yang ditemukan adalah {documents_count} {spasi}") # Mencetak banyaknya file yang ditemukan
print(f"Waktu yang dibutuhkan adalah {total_time} detik") #Mencetak banyaknya waktu yang dibutuhkan 