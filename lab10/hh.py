import tkinter as tk
from tkinter import messagebox

class PacilokaApp:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Paciloka Hotel Booking")
        self.master.geometry("400x300")
        
        self.dict_hotel = {'hotel1': [10, 250000, 'kode_hotel_1'], 'hotel2': [12, 500000, 'kode_hotel_2'], 'hotel3': [10, 7500000, 'kode_hotel_3'], 
                        'hotel4': [1, 1000000, 'kode_hotel_4'], 'hotel5': [10, 900000, 'kode_hotel_5'], 'hotel6': [10, 6000000, 'kode_hotel_6']}
        
        self.homepage()
    
    def homepage(self):
        # Labels
        tk.Label(self.master, text="Paciloka Hotel Booking", font=("Helvetica", 16)).pack(pady=10)
        tk.Label(self.master, text="Choose a hotel:").pack(pady=5)

        # Dropdown for selecting a hotel
        hotel_var = tk.StringVar()
        hotel_var.set(list(self.dict_hotel.keys())[0])  # Set default value
        hotel_dropdown = tk.OptionMenu(self.master, hotel_var, *self.dict_hotel.keys())
        hotel_dropdown.pack(pady=5)
        
        # Entry field for the number of rooms
        tk.Label(self.master, text="Number of rooms:").pack(pady=5)
        rooms_entry = tk.Entry(self.master)
        rooms_entry.pack(pady=5)
        
        # Entry field for the customer code
        tk.Label(self.master, text="Customer code:").pack(pady=5)
        code_entry = tk.Entry(self.master)
        code_entry.pack(pady=5)
        
        # Button to initiate booking
        tk.Button(self.master, text="Book Now", command=lambda: self.booking(hotel_var.get(), rooms_entry.get(), code_entry.get())).pack(pady=10)
    
    def booking(self, selected_hotel, num_rooms, customer_code):
        try:
            num_rooms = int(num_rooms)
            if num_rooms <= 0:
                raise ValueError("Number of rooms must be greater than 0")

            # Assuming customer code validation logic here...

            # Assuming booking logic here...
            total_price = self.dict_hotel[selected_hotel][1] * num_rooms
            messagebox.showinfo("Booking Successful", f"Booking confirmed for {num_rooms} rooms at {selected_hotel}.\nTotal Price: {total_price}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PacilokaApp(master=root)
    root.mainloop()
