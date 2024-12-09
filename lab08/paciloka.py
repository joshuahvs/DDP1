#class hotel
class Hotel:
    #untuk inisiasi
    def __init__(self, name, available_room, room_price, profit=0, guest=[]):
        self.name = name
        self.available_room = available_room
        self.room_price = room_price
        self.profit = profit
        self.guest = guest
    #fungsi yang dipanggil saat user melakukan booking 
    def booking(self, user, jumlah_kamar):
        if jumlah_kamar > 0 and self.available_room >= jumlah_kamar:
            total_cost = jumlah_kamar * self.room_price
            if user.money >= total_cost:
                self.guest += [user.name]
                self.available_room -= jumlah_kamar
                self.profit += total_cost
                user.money -= total_cost
                user.hotel_list += [self.name]
                return True
        return False
    #return string nama dari hotel
    def __str__(self):
        return self.name
#Class user
class User:
    #inisiasi
    def __init__(self, name, money, hotel_list=[]):
        self.name = name
        self.money = money
        self.hotel_list = hotel_list
    #ketika user melakukan top up
    def top_up(self, jumlah_top_up):
        self.money += jumlah_top_up
    #return string
    def __str__(self):
        return self.name
#main programnya
if __name__ == '__main__':
    #meminta input user
    banyak_hotel = int(input("Masukkan banyak hotel: "))
    banyak_user = int(input("Masukkan banyak user: "))
    print()
    hotels = []
    users = []
    #mengiterasi nama hotel dan user berdasarkan jumlah hotel dan user
    for i in range(banyak_hotel):
        nama_hotel = input(f"Masukkan nama hotel ke-{i+1}: ")
        banyak_kamar = int(input(f"Masukkan banyak kamar hotel ke-{i+1}: "))
        harga_kamar = int(input(f"Masukkan harga satu kamar hotel ke-{i+1}: "))
        hotel = Hotel(nama_hotel, banyak_kamar, harga_kamar)
        hotels.append(hotel)

    print()
    for j in range(banyak_user):
        nama_user = input(f"Masukkan nama user ke-{j+1}: ")
        saldo = int(input(f"Masukkan saldo user ke-{j+1}: "))
        user = User(nama_user, saldo)
        users.append(user)

    active = True
    while active:
        print()
        print('=============Welcome to Paciloka!=============')
        print()
        action = int(input("Masukkan perintah: "))
        #action yang menampilkan semua daftar hotel dan user
        if action == 1:
            print("Daftar Hotel")
            for number, hotel in enumerate(hotels):
                print(f'{number+1}. {hotel.name}')
            print()
            print("Daftar User")
            for number, user in enumerate(users):
                print(f'{number+1}. {user.name}')
        #action untuk mencetak profit hotel
        elif action == 2:
            hotel_to_check = input("Masukkan nama hotel : ")
            found = False
            for hotel in hotels:
                if hotel_to_check == hotel.name:
                    print(f"Hotel dengan nama {hotel.name} mempunyai profit sebesar {hotel.profit}")
                    found = True
            if found == False:
                print("Nama hotel tidak ditemukan di sistem!")

        #action untuk mengecheck saldo user
        elif action == 3:
            user_to_check = input("Masukkan nama user : ")
            found = False
            for user in users:
                if user_to_check == user.name:
                    print(f"User dengan nama {user.name} mempunyai saldo sebesar {user.money}")
                    found = True
            if found == False:
                print("Nama user tidak ditemukan di sistem!")
        #action untuk menambah saldo user
        elif action == 4:
            user_to_check = input("Masukkan nama user : ")
            found = False
            for user in users:
                if user_to_check == user.name:
                    found = True
                    saldo_to_add = int(input("Masukkan jumlah uang yang akan ditambahkan ke user : "))
                    if saldo_to_add > 0:
                        user.top_up(saldo_to_add)
                        print(f"Berhasil menambahkan {saldo_to_add} ke user {user_to_check}. Saldo user menjadi {user.money}")
                    else:
                        print("Jumlah saldo yang akan ditambahkan ke user harus lebih dari 0!")
            if found == False:
                print("Nama user tidak ditemukan di sistem!")
        #action untuk melakukan booking hotel
        elif action == 5:
            user_to_check = input("Masukkan nama user: ")
            user_found = False
            hotel_found = False
            for user in users:
                if user_to_check == user.name:
                    user_found = True
                    hotel_to_check = input("Masukkan nama hotel: ")
                    for hotel in hotels:
                        if hotel_to_check == hotel.name:
                            hotel_found = True
                            kamar_to_book = int(input("Masukkan jumlah kamar yang akan dibooking: "))
                            if kamar_to_book <= 0:
                                print('Jumlah kamar yang akan dipesan harus lebih dari 0!')
                                break
                            if hotel.booking(user, kamar_to_book):
                                bookingable = True
                                print(f"User {user_to_check} berhasil melakukan booking di {hotel_to_check} dengan jumlah {kamar_to_book} kamar!")
                                break
                            else:
                                print("Booking tidak berhasil")
            if user_found == False:
                print("Nama user tidak ditemukan di sistem!")
            elif hotel_found == False:
                print("Nama hotel tidak ditemukan di sistem!")
                
        #action untuk print guest dari sebuah hotel 
        elif action == 6:
            hotel_to_check = input("Masukkan nama hotel : ")
            found = False
            for hotel in hotels:
                if hotel_to_check == hotel.name:
                    found = True
                    if hotel.guest == []:
                        print(f"Hotel {hotel} tidak memiliki pelanggan!")
                        break
                    guest = ", ".join(hotel.guest)
                    print(f"{hotel_to_check} | {guest} ")
            if found == False:
                print(f"Hotel tidak ditemukan")
        #action untuk print bookingan hotel dari sebuah list 
        elif action == 7:
            user_to_check = input("Masukkan nama user : ")
            found = False
            for user in users:
                if user_to_check == user.name:
                    found = True
                    if user.hotel_list == []:
                        print(f'User {user_to_check} tidak pernah melakukan booking!')
                        break
                    hotel = ", ".join(user.hotel_list)
                    print(f"{user_to_check} | {hotel} ")
            if found == False:
                print("User tidak ditemukan")

        #action untuk keluar
        elif action == 8:
            print("Terima kasih sudah mengunjungi Paciloka!")
            active = False
        #jika user melakukan pilihan diluar yang disediakan 

        else:
            print("Perintah tidak diketahui! Masukkan perintah yang valid")
