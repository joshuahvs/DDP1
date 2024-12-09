class Hotel:
    def __init__(self, name, available_room, room_price, profit=0, guest=0):
        self.name = name
        self.available_room = available_room
        self.room_price = room_price
        self.profit = profit
        self.guest = guest
    
    def booking(self, user, jumlah_kamar):
        if jumlah_kamar > 0 and self.available_room >= jumlah_kamar:
            total_cost = jumlah_kamar*self.room_price
            if user.money >= total_cost:
                self.guest += user.name
                self.available_room -= 1
                self.profit += total_cost
                user.money -= total_cost
                return True
            else:
                return False
        else:
            return False


    def __str__(self):
        pass

class User:
    def __init__(self, name, money, hotel_list=0):
        self.name = name
        self.money = money
        self.hotel_list = hotel_list

    def top_up(self, jumlah_top_up):
        self.money += jumlah_top_up

    def __str__(self):
        return self.name
    
if __name__ == '__main__':
    banyak_hotel = int(input("Masukkan banyak hotel : "))
    banyak_user = int(input("Masukkan banyak user : "))
    print()
    hotels = []
    users = []
    for i in range(banyak_hotel):
        nama_hotel = input(f"Masukkan nama hotel ke-{i+1} : ")
        banyak_kamar = int(input(f"Masukkan banyak kamar hotel ke-{i+1} : "))
        harga_kamar = int(input(f"Masukkan harga satu kamar hotel ke-{i+1} : "))
        hotel = Hotel(nama_hotel, banyak_kamar, harga_kamar)
        hotels.append(hotel)

    print()
    for j in range(banyak_user):
        nama_user = input(f"Masukkan nama user ke-{i+1} : ")
        saldo = int(input(f"Masukkan saldo user ke-{i+1} : "))
        user = User(nama_user, saldo)
        users.append(user)

    active = True
    while active == True:
        print()
        print('=============Welcome to Paciloka!=============')
        print()
        action = int(input("Masukkan perintah : "))

        if action == 1:
            print("Daftar Hotel")
            for number, hotel in enumerate(hotels):
                print(f'{number+1}. {hotel.name}')
            print()
            print("Daftar User")
            for number, user in enumerate(users):
                print(f'{number+1}. {user.name}')
        
        elif action == 2:
            hotel_to_check = input("Masukkan nama hotel : ")
            found = False
            for hotel in hotels:
                if hotel_to_check == hotel.name:
                    print(f"Hotel dengan nama {hotel.name} mempunyai profit sebesar {hotel.profit}")
                    found = True
            if found == False:
                print("Nama hotel tidak ditemukan di sistem!")

        elif action == 3:
            user_to_check = input("Masukkan nama user : ")
            found = False
            for user in users:
                if user_to_check == user.name:
                    print(f"User dengan nama {user.name} mempunyai saldo sebesar {user.money}")
                    found = True
            if found == False:
                print("Nama user tidak ditemukan di sistem!")
        
        elif action == 4:
            user_to_check = input("Masukkan nama user : ")
            found = False
            for user in users:
                if user_to_check == user.name:
                    found = True
                    saldo_to_add = int(input("Masukkan jumlah uang yang akan ditambahkan ke user : "))
                    user.top_up(saldo_to_add)
                    print(f"Berhasil menambahkan {saldo_to_add} ke user {user_to_check}. Saldo user menjadi {user.money}")
            if found == False:
                print("Nama user tidak ditemukan di sistem!")

        elif action == 5:
            user_to_check = input("Masukkan nama user : ")
            bookingable = False
            for user in users:
                if user_to_check == user.name:
                    hotel_to_check = input("Masukkan nama hotel : ")
                    for hotel in hotels:
                        if hotel_to_check == hotel.name:
                            kamar_to_book = int(input("Masukkan jumlah kamar yang akan dibooking : "))
                            if hotel.available_room > 0 and hotel.available_room >= kamar_to_book:
                                bookingable = hotel.booking(user,kamar_to_book)
            if bookingable == True:
                print(f"User dengan nama {user_to_check} berhasil melakukan booking di hotel {hotel_to_check} dengan jumlah {kamar_to_book} kamar!")
                                
        
        elif action == 8:
            print("Terima kasih sudah mengunjungi Paciloka!")
        
        else:
            print("Perintah tidak diketahui! Masukkan perintah yang valid")
