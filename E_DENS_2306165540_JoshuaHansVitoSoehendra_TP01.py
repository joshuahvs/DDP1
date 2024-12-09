from turtle import * # Untuk mengimport fungsi turtle

# untuk mengatur speed turtle dan menyembunyikan turtlenya
speed(0)
hideturtle()

# Meminta input spesifikasi tower yang ingin dibuat
jumlah_tower = int(numinput("Jumlah tower", "Masukkan jumlah tower yang ingin dibangun", minval=1)) # minval adalah value minimal yang bisa diimput
# If loop akan dijalankan jika pengguna ingin untuk membuat lebih dari 1 tower
if jumlah_tower > 1: 
    jarak_tower = int(numinput("Jarak antara tower", "Masukkan jarak antara tower", minval=2, maxval=5)) # maxval adalah value maksimal yang bisa diinput
    perbedaan_jumlah_lapisan = int(numinput("Perbedaan lapisan tower", "Masukkan perbedaan lapisan antar tower", minval=2, maxval=5))
else: 
    jarak_tower = 0
    perbedaan_jumlah_lapisan = 0
lebar_batubata = int(numinput("Lebar batu bata", "Masukkan lebar batu bata", minval=1, maxval=35))
tinggi_batubata = int(numinput("Tinggi batu bata", "Masukkan tinggi batu bata", minval=1, maxval=25))
tinggi_tower_pertama = int(numinput("Lapisan tower pertama", "Masukkan jumlah lapisan tower pertama", minval=1, maxval=25))
lebar_badan_tower = int(numinput("Lebar badan tower", "Masukkan lebar badan tower", minval=1, maxval=10))

# Menghitung total lebar, dan menggunakannya untuk titik mulai, sehingga hasil dari turtle berada di tengah
total_lebar = jumlah_tower*(lebar_badan_tower*lebar_batubata)+(jarak_tower*lebar_batubata*(jumlah_tower-1))
titik_mulai = total_lebar/2

# Menggunakan penup supaya tidak terbentuk garis, lalu menyetel titik mulai supaya di tengah, dan pendown supaya garis yang digambar terlihat lagi
penup()
setposition(-titik_mulai,0)
pendown()

# Menyetel total batu bata mula-mula
total_batu_bata = 0

# Menggunakan for loop untuk mengiterasi jumlah tower yang ingin dibuat
for a in range(1, jumlah_tower+1):  # 1 supaya program mulai dari 1 bukan 0, dan jumlah tower + 1 supaya totalnya sama seperti jika mulai dari 0
        # Menggunakan for loop untuk mengiterasi tinggi tower sehingga program mengulang terus sampai tinggi tower yang diminta
        for b in range(tinggi_tower_pertama):  
            # Menggunakan for loop untuk mengiterasi lebar dari tower, program akan mengulang sebanyak lebar badan tower yang diminta
            for c in range(lebar_badan_tower):
                color("black", "#CA7F65") # untuk mengatur warna garis dan isiannya
                begin_fill() #untuk memulai pengisian
                # Serangkaian perintah untuk membuat 1 buat bata 
                forward(lebar_batubata)
                left(90)
                forward(tinggi_batubata) #forward untuk maju
                left(90) # left untuk belok ke kiri
                forward(lebar_batubata)
                left(90)
                forward(tinggi_batubata)
                left(90)
                forward(lebar_batubata)
                end_fill() # untuk menghentikan pengisian
                total_batu_bata += 1 # menambah total batu bata di setiap iterasi 
            # Serangkaian perintah yang membuat program kembali ke titik awal pembuatan lalu naik sebesar tinggi batu bata sehingga dapat melanjutkan iterasi lebar badan tower selanjutnya 
            left(180)
            forward(lebar_batubata*lebar_badan_tower)
            right(90)
            forward(tinggi_batubata)
            right(90)
        # Mengatur turtle untuk membuat kepala tower pertama 
        right(180)
        color("black", "#693424")
        begin_fill()
        forward(lebar_batubata*0.5)
        right(90)
        forward(tinggi_batubata)
        right(90)
        forward(lebar_batubata)
        right(90)
        forward(tinggi_batubata)
        left(90)
        end_fill()
        total_batu_bata += 1 
        # Mengunnakan for loop untuk membuat sisa dari kepala tower pertama
        for c in range(lebar_badan_tower):
                color("black", "#693424")
                begin_fill()
                forward(lebar_batubata)
                left(90)
                forward(tinggi_batubata)
                left(90)
                forward(lebar_batubata)
                left(90)
                forward(tinggi_batubata)
                left(90)
                forward(lebar_batubata)
                end_fill()
                total_batu_bata += 1
        # Membuat jamur super mario
        penup()
        right(180)
        forward(((lebar_badan_tower+1)*lebar_batubata)/2)
        right(90)
        forward(tinggi_batubata)
        left(90)
        forward(lebar_batubata/2)
        right(90)
        pendown()
        color("#ffd3a5", "#ffd3a5")
        begin_fill()
        forward(tinggi_batubata+2)
        right(90)
        forward(lebar_batubata+2)
        right(90)
        forward(tinggi_batubata+2)
        end_fill()
        penup()
        right(90)
        forward(lebar_batubata+2)
        right(180)
        forward(lebar_batubata+2)
        left(90)
        forward(tinggi_batubata+2)
        right(90)
        pendown()
        color("red", "red")
        begin_fill()
        forward(1/3*(lebar_batubata+2))
        left(90)
        radius = 5/6*(lebar_batubata+2)
        circle(radius, 180)
        left(90)
        forward(4/3*(lebar_batubata+2))
        end_fill()
        penup()
        right(90)
        forward(1/4*(tinggi_batubata+1))
        right(90)
        forward(1/4*(lebar_batubata+1))
        pendown()
        color("white", "white")
        begin_fill()
        circle(radius=1/10*(lebar_batubata))
        penup()
        forward(1/2*(lebar_batubata+1))
        pendown()
        circle(radius=1/10*(lebar_batubata+1))
        right(180)
        end_fill()

        # Mengatur ulang posisi turtle ke awal, dan melanjutkan sepanjang lebar tower ditambah jarak tower
        penup()
        setposition(-titik_mulai,0)
        tower_selanjutnya = (lebar_badan_tower*lebar_batubata + jarak_tower*lebar_batubata)*a 
        forward(tower_selanjutnya)
        pendown()
        tinggi_tower_pertama += perbedaan_jumlah_lapisan

penup()
setposition(0,-45) 
pendown()
# Untuk menulis jumlah tower, dan total batu bata yang digunakan untuk membangunnya
color("black")
write(str(jumlah_tower)+ " Super Mario Towers have been built with a total of " + str(total_batu_bata) + " bricks", align="center", font=("Arial", 15, "bold"))


# agar tab turtle tidak tertutup secara otomatis
exitonclick()