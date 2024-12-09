from tkinter import * 

def hello(event):
    print("Single Click, Button-l")
def quit(event):
    print("Double Click, so let's stop") 
    root.destroy()
root = Tk()
widget = Button(root, text='Mouse Clicks')
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit)
root.mainloop()