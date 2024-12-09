from tkinter import *
class MyGrid:
       def __init__(self, master):
               self.master = master
               master.title("Kuy nge-Grid!")
               message = Message(master, text = "Message of 3 rows and 2 columns")
               message.grid(row = 1, column = 1, rowspan = 3, columnspan = 2)
               Label(master, text = "First Name:").grid(row = 1, column = 3)
               Entry(master).grid(row = 1, column = 4)
               Label(master, text = "Last Name:").grid(row = 2, column = 3)
               Entry(master).grid(row = 2, column = 4)
               Button(master, text = "Get Name").grid(row = 3, column = 4)
root = Tk()
my_grid = MyGrid(root)
root.mainloop()