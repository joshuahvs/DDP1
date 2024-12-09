from tkinter import *

class MyFirstGUI:
    def __init__(self,master):
        self.master = master
        master.title("DDP Lab")
        master.geometry("300x100")
        self.label_user = Label(master, text='Username')
        self.user = StringVar()
        self.field_user = Entry(master, textvariable=self.user)
        self.label_user.pack()
        self.field_user.pack()

        self.label_pass = Label(master, text='Password')
        self.password = StringVar()
        self.field_password = Entry(master, textvariable=self.password)
        self.label_pass.pack()
        self.field_password.pack()

        self.label_nominal = Label(master, text='Nominal')
        self.nominal = IntVar()
        self.field_nominal = Entry(master, textvariable=self.nominal)
        self.label_nominal.pack()
        self.field_nominal.pack()

        self.radio = IntVar()
        self.rb_deposit = Radiobutton(master, text='Deposit', variable=self.radio, value= 0)
        self.rb_withdraw = Radiobutton(master, text='Withdraw', variable=self.radio, value= 1)
        self.rb_signup = Radiobutton(master, text='Withdraw', variable=self.radio, value=2)
        self.rb_deposit.pack()
        self.rb_withdraw.pack()
        self.rb_signup.pack()

        self.button = Button(master, text='Submit', command=self.process)
        self.button.pack()

    def process(self):
        print(self.radio.get())
        if self.radio == 0: #deposit
            pass
        elif self.radio == 1:
            pass
        elif self.radio == 2:
            nama_user = self.user.get()
            password = self.user.get()
            saldo_awal = self.user.get()
            if nama_user not in self.database:
                self.database[nama_user] = {'password' : password, 'saldo': saldo_awal}
            #     showinfo("berhasil mendaftarkan %s dengan saldo awal %d"%(nama_user,saldo_awal))
            # else:

window = Tk()
my_gui = MyFirstGUI(window)
window.mainloop()