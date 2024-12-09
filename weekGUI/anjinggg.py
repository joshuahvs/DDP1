from tkinter import *
from tkinter.messagebox import showinfo
class Formulirku:
       def __init__(self, master):
            self.master = master
            master.title("Kuy nge-GUI!")
            self.label = Label(master, text="Halo, nama saya..")
            self.label.pack()
            self.nama = StringVar()
            self.field_nama = Entry(master, textvariable=self.nama, width=40)
            self.field_nama.pack()
            self.button = Button(master, text="OK", command=self.edit_nama)
            self.button.pack() 
            def edit_nama(self):
                showinfo(message="Halo, {}!".format(self.nama.get()))

            self.nama = StringVar()
            self.field_nama = Entry(master, textvariable=self.nama, width=40)
            self.field_nama.pack()
            def edit_nama(self):
                showinfo(message="Halo, {}!".format(self.nama.get()))
root = Tk()
my_gui = Formulirku(root)
root.mainloop()
