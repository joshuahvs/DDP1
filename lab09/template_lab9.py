from random import randint


class Person:
    # TODO: Lengkapi constructor
    #       Perhatikan access modifiernya!
    def __init__(self, name, payment, stamina):
        self.__name = name
        self.__payment = payment
        self.__stamina = stamina
        self.__totalwork = 0

    # TODO: Lengkapi getter dan setter
    #GETTER
    def get_name(self):
        return self.__name
    def get_payment(self):
        return self.__payment
    def get_stamina(self):
        return self.__stamina

    #SETTER
    def set_stamina(self, new_stamina):
        self.__stamina = new_stamina
    def set_totalwork(self, total_work):
        self.__totalwork = total_work

    def is_available(self,cost_stamina):
        return self.__stamina >= cost_stamina

    def pay_day(self):
        return self.__payment*self.__totalwork

    def work(self, cost_stamina):
        self.__stamina -= cost_stamina
        self.__totalwork += 1
    
    def __str__(self):
        class_name = self.__class__.__name__
        name = self.__name
        total_work = self.__totalwork
        stamina = self.__stamina
        payment = self.__payment

        return f"{class_name:20} | {name:20} | Total kerja: {total_work:20} | Stamina:{stamina:20} | Gaji:{payment:20}"


class Manager(Person):
    # TODO: Lengkapi constructor
    def __init__(self, name, payment, stamina):
        ...
        
    # Lengkapi getter dan setter
    def get_list_worker(self):
        ...

    # TODO: Lengkapi method berikut
    def hire_worker(self, name):
        ...
        
    def fire_worker(self, name):
        ...


    def give_work(self, name,bonus ,cost_stamina):
        ...


class Worker(Person):
    # TODO: Lengkapi constructor
    #       Perhatikan access modifiernya!
    def __init__(self, name, payment, stamina):
        ...

    # TODO: Lengkapi method berikut
    def work(self, bonus,cost_stamina):
        ...

    def get_bonus(self):
        return self.__bonus

    def set_bonus(self, new_bonus):
        self.__bonus = new_bonus    
    

def main():
    # TODO: meminta nama
    name =  input("Masukkan nama manajer: ")
    payment = int(input("Masukkan jumlah pembayaran: "))
    stamina = int(input("Masukkan stamina manajer: "))

    # TODO: Inisialisasi Manager
    manager = ...

    while manager.is_available(1):
        print("""
PACILOKA
-----------------------
1. Lihat status pegawai
2. Beri tugas
3. Cari pegawai baru
4. Pecat pegawai
5. Keluar
-----------------------
        """)
        action = int(input("Masukkan pilihan: "))
        
        # TODO
        if action == 1:
            ...

        elif action == 2:
            ...

        elif action == 3:
            ...

        elif action == 4:
            ...

        elif action == 5:
            print("""
----------------------------------------
Berhenti mengawasi hotel, sampai jumpa !
----------------------------------------""")
            return
    print("""
----------------------------------------
Stamina manajer sudah habis, sampai jumpa !
----------------------------------------""")

if __name__ == "__main__":
    main()
