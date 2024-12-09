kecepatan_lari = float(input("masukkan kecepatan lari mile per jam: "))
jarak_lari = 26.2

waktu = float(jarak_lari/kecepatan_lari)
jam = int(waktu)
menit = (waktu-jam)*60

print(f"waktu untuk menyelesaikan maraton {jam} jam {menit} menti")