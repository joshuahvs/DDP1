class Person:
    # Inisiasi class person
    def __init__(self, name, payment, stamina):
        self.__name = name
        self.__payment = payment
        self.__stamina = stamina
        self.__totalwork = 0

    #GETTER
    def get_name(self):
        return self.__name
    def get_payment(self):
        return self.__payment
    def get_stamina(self):
        return self.__stamina
    def get_totalwork(self):
        return self.__totalwork
    
    #SETTER
    def set_stamina(self, new_stamina):
        self.__stamina = new_stamina
    def set_totalwork(self, total_work):
        self.__totalwork = total_work
    def set_payment(self, new_payment):
        self.__payment = new_payment

    # Fungsi yang mengembalikan person bisa bekerja
    def is_available(self,cost_stamina):
        return self.__stamina >= cost_stamina

    # 
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
        payment = self.pay_day()

        return f"{class_name:20} | {name:20} | Total kerja: {total_work:20} | Stamina:{stamina:20} | Gaji:{payment:20}"

# Class manager, yang merupakan inheritence dari class person
class Manager(Person):
    # TODO: Lengkapi constructor
    def __init__(self, name, payment, stamina):
        super().__init__(name, payment, stamina)
        self.__listworker = []
        
    # Lengkapi getter dan setter
    def get_list_worker(self):
        return self.__listworker
    def set_list_worker(self, list_worker):
        self.__listworker += [list_worker]


    # fungsi untuk memnghire worker
    def hire_worker(self, name):
        if name in [worker.get_name() for worker in self.__listworker]:
            return "Sudah ada!"
        else:
            new_worker = Worker(name)
            self.__listworker.append(new_worker)
            self.set_stamina(self.get_stamina() - 10)
            self.set_totalwork(self.get_totalwork()+1)
            return "Berhasil mendapat pegawai baru"
    
    # fungsi untuk memecat worker
    def fire_worker(self, name):
        for worker in self.__listworker:
            if worker.get_name() == name:
                self.__listworker.remove(worker)
                self.set_stamina(self.get_stamina()-10)
                self.set_totalwork(self.get_totalwork()+1)
                return f"Berhasil memecat {name}"
        else:
            return "Nama tidak ditemukan"

    # Fungsi untuk memberi pekerjaan kepada worker
    def give_work(self, name, bonus ,cost_stamina):
        for worker in self.__listworker:
            if worker.get_name() == name:
                if worker.is_available(cost_stamina):
                    worker.work(bonus, cost_stamina)
                    self.set_stamina(self.get_stamina()-10)
                    self.set_totalwork(self.get_totalwork()+1)

                    to_return =  "Hasil cek ketersediaan pegawai:\nPegawai dapat menerima pekerjaan\n"
                    to_return += "========================================\n"
                    to_return += f"Berhasil memberi kerjaan {name}"
                    return to_return
                else:
                    return "Hasil cek ketersediaan pegawai:\nPegawai tidak dapat menerima pekerjaan. Stamina pegawai tidak cukup."

# class Worker, merupakan inheritence dari person
class Worker(Person):
    #agar tidak memiliki nama yang sama
    __uniques_names = set()

    # Inisiasi awal
    def __init__(self, name, payment = 5000, stamina = 100):
        if name in Worker.__uniques_names:
            raise ValueError("Nama harus unik")
        Worker.__uniques_names.add(name)
        super().__init__(name, payment, stamina)
        self.__bonus = 0

   # Fungsi yang akan dipanggil ketika worker bekerja
    def work(self, bonus, cost_stamina):
        if self.is_available(cost_stamina):
            self.__bonus += bonus
            self.set_payment(self.get_payment()+ bonus)
            self.set_totalwork(self.get_totalwork()+1)
            self.set_stamina(self.get_stamina()-cost_stamina)

    # Getter bonus
    def get_bonus(self):
        return self.__bonus

    # Setter bonus
    def set_bonus(self, new_bonus):
        self.__bonus = new_bonus    

def main():
    # TODO: meminta nama
    name =  input("Masukkan nama manajer: ")
    payment = int(input("Masukkan jumlah pembayaran: "))
    stamina = int(input("Masukkan stamina manajer: "))

    # TODO: Inisialisasi Manager
    manager = Manager(name, payment, stamina)

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
        
        # menampilkan keseluruhan data karyawan dan juga manager
        if action == 1:
            print(manager.__str__())
            for worker in manager.get_list_worker():
                print(worker.__str__())            
        # Memberi tugas kepada pegawai
        elif action == 2:
            tugas_kepada = input("Tugas akan diberikan kepada: ")
            bonus_pekerjaan = int(input("Bonus pekerjaan: "))
            beban_stamina = int(input("Beban stamina: "))
            giving_work = manager.give_work(tugas_kepada, bonus_pekerjaan, beban_stamina)
            print(giving_work)
        # Merekrut pegawai baru
        elif action == 3:
            pegawai_baru = input("Nama pegawai baru: ")
            hiring = manager.hire_worker(pegawai_baru)
            print(hiring)
        # Memecat karyawan
        elif action == 4:
            pegawai_untuk_dipecat = input("Masukkan nama pegawai yang akan dipecat: ")
            firing = manager.fire_worker(pegawai_untuk_dipecat)
            print(firing)

        # Keluar dan selesai
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
