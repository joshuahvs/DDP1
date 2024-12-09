# Meminta input pesan hexadecimal dan angka yang akan diterjemahkan menjadi pesan dan password
pesan_kelompok_zog = input('Pesan Kelompok Zog: ')
angka_1 = int(input('Angka 1: '))
angka_2 = int(input('Angka 2: '))

# Merubah pesan hexadecimal menjadi menjadi byte string, lalu mengubah byte string menjadi string 
pesan_bytes_string = bytes.fromhex(pesan_kelompok_zog)
pesan_ascii = pesan_bytes_string.decode('ASCII')
 
# Mengubah angka menjadi password dengan cara mengalikan kedua angka dengan 13 lalu mengubahnya menjadi sebuah string biner
password = str(bin(angka_1 * angka_2 * 13))

# Mencetak hasil terjemahan, password, dan kesimpulannya
print('Hasil terjemahan pesan: ' + pesan_ascii \
      + '\nPassword: ' + password \
      + "\n" \
      + '\nPesan "'+ pesan_ascii + '" telah diterima dengan password "' + password + '".')

