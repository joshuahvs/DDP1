import tkinter as tk #import tkinter
from tkinter import messagebox #import untuk show message box

class PacilokaApp:
    # inisiasi awal
    def __init__(self, master=None):
        self.master = master
        self.dict_hotel = {'hotel1': [10, 250000, 'kode_hotel_1'], 'hotel2': [12, 500000, 'kode_hotel_2'], 'hotel3': [10, 7500000, 'kode_hotel_3'], 
                        'hotel4': [1, 1000000, 'kode_hotel_4'], 'hotel5': [10, 900000, 'kode_hotel_5'], 'hotel6': [10, 6000000, 'kode_hotel_6']}
        
        # menambahkan title dan ukuran windows
        master.title('Paciloka App')
        master.geometry('350x700')
        self.homepage()
        
    # menambahkan label, field, dan button yang dibutuhkan
    def homepage(self):
        label = tk.Label(self.master, text='Welcome', font='Halvetica 24 bold')

        teks = tk.Label(self.master, text='Choose your hotel\nto get more information!', font='Halvetica 18')
        label.pack(pady=10)
        teks.pack(pady=5)

       # Dropdown menu untuk memilih hotel
        hotel_var = tk.StringVar()
        hotel_var.set(list(self.dict_hotel.keys())[0])  # Set default value
        hotel_dropdown = tk.OptionMenu(self.master, hotel_var, *self.dict_hotel.keys(), command=self.update_hotel_info)
        hotel_dropdown.pack(pady=5)

        # Label yang menampilkan informasi hotel
        self.hotel_name_label = tk.Label(self.master, text='')
        self.hotel_name_label.pack()
        self.room_label = tk.Label(self.master, text='')
        self.room_label.pack()
        self.price_label = tk.Label(self.master, text='')
        self.price_label.pack()

        # Kolom nama customer
        customer_name_label = tk.Label(self.master, text='Nama Pengguna:')
        customer_name_label.pack(pady=5)
        self.customer_name_entry = tk.Entry(self.master)
        self.customer_name_entry.pack(pady=5)
        # Kolom nama hotel
        hotel_name_label = tk.Label(self.master, text='Nama Hotel:')
        hotel_name_label.pack(pady=5)
        self.hotel_name_entry = tk.Entry(self.master)
        self.hotel_name_entry.pack(pady=5)
        # Kolom jumlah kamar
        room_count_label = tk.Label(self.master, text='Jumlah Kamar:')
        room_count_label.pack(pady=5)
        self.room_count_entry = tk.Entry(self.master)
        self.room_count_entry.pack(pady=5)

        # tombol booking
        book_button = tk.Button(self.master, text='Book Room', command=self.booking)
        book_button.pack(pady=10)

        # tombol booking
        book_button = tk.Button(self.master, text='Exit', command=self.master.destroy)
        book_button.pack(pady=5)

    # Fungsi yang mengupdate informasi hotel
    def update_hotel_info(self, selected_hotel):
        values = self.dict_hotel[selected_hotel]
        self.hotel_name_label.config(text=f'Nama Hotel: {selected_hotel}')
        self.room_label.config(text=f'Jumlah Kamar Tersedia: {values[0]}')
        self.price_label.config(text=f'Harga per Kamar: {values[1]}')
    
    # menambahkan logic untuk validasi proses booking
    def booking(self):
        customer_name = self.customer_name_entry.get()
        hotel_name = self.hotel_name_entry.get()
        # validasi input bila jumlah kamar bukan bilangan bulat
        try:
            room_count = int(self.room_count_entry.get())
        except ValueError:
            messagebox.showerror('Error!','Jumlah kamar harus berupa bilangan bulat.')
        # Validasi input ketersediaan nama hotel
        if hotel_name not in self.dict_hotel:
            messagebox.showerror('Error!',f'Maaf, {hotel_name} tidak tersedia di sistem.')
            return
        # Validasi input jika jumlah kamar yang dipilih kurang dari 1
        if room_count <= 0:
            messagebox.showerror('Error!','Maaf, kamar yang dipesan harus lebih dari 0.')
            return
        # Validasi jumlah kamar yang ingin dibooking dan kamar yang tersedia
        if room_count > self.dict_hotel[hotel_name][0]:
            messagebox.showerror('Error!',f'Maaf, tidak bisa memesan kamar sebanyak {room_count} di hotel {hotel_name}')
        else:
            room_price = self.dict_hotel[hotel_name][1]
            total_price = room_count*room_price

            self.dict_hotel[hotel_name][0] -= room_count #mengurangi jumlah kamar
            kode_hotel = self.dict_hotel[hotel_name][2] 
            ticket_number = f'{kode_hotel}/{room_count}/{customer_name[:3]}' #tiket booking
            
            messagebox.showinfo('Booking Berhasil!',f'Booking Berhasil!\nPesanan untuk {customer_name} di hotel {hotel_name} sebanyak {room_count} kamar!\n\
                                Total Biaya: {total_price}\nNomor Tiket: {ticket_number}')

            # membersihkan entry fields
            self.customer_name_entry.delete(0, tk.END)
            self.hotel_name_entry.delete(0, tk.END)
            self.room_count_entry.delete(0, tk.END)
            
            self.update_hotel_info(hotel_name)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = PacilokaApp(master=root)
    root.mainloop()