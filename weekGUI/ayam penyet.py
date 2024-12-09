from tkinter import *
class MyFirstCanvas:
    def __init__(self, master):
        self.master = master
        master.title("kuy nge-Canvas")
        self.canvas = Canvas(master, width=200, height=100, bg="white")
        self.canvas.create_rectangle(10,10,190,90)
        self.canvas.pack()

root = Tk()
my_canvas = MyFirstCanvas(root)
root.mainloop()