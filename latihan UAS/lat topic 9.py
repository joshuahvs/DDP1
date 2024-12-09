# my_dict = {'bill':3, 'rich':10}
# print(my_dict['rich'])
# my_dict['bill'] = 100
# print(my_dict['bill'])


# #sorting by key and value
# count_of_words = {'to': 2, 'be': 2, 'or': 1, 'not': 1}
# # Sorting by key
# by_key = sorted(count_of_words.items(), key=lambda kv: kv[0])
# # Sorting by value
# by_value = sorted(count_of_words.items(), key=lambda kv: kv[1])
# print(by_key)
# print(dict(by_key))
# print(by_value)
# print(dict(by_value))


# from tkinter import * 
# class MyFirstGUI:
#         def __init__(self, master):
#             self.master = master
#             master.title("Kuy nge-GUI!")
#             self.nilai = IntVar()
#             self.nilai.set(0) # atur nilai bawaan/default
#             rb_pria = Radiobutton(master, text="Pria", variable=self.nilai, value=0, command=self.gender)
#             rb_wanita = Radiobutton(master, text="Wanita", variable=self.nilai, value=1, command=self.gender)
#             rb_pria.pack()
#             rb_wanita.pack()
#             print("Nilai:", self.nilai.get())
#         def gender(self):
#             print("Nilai:", self.nilai.get())
# root = Tk()
# my_gui = MyFirstGUI(root)
# root.mainloop()


# from tkinter import * 
# class MyFirstGUI:
#         def __init__(self, master):
#             self.master = master
#             master.title("Kuy nge-GUI!")
#             self.nilai = StringVar()
#             self.nilai.set('') # atur nilai bawaan/default
#             rb_pria = Radiobutton(master, text="Pria", variable=self.nilai, value='pria', command=self.gender)
#             rb_wanita = Radiobutton(master, text="Wanita", variable=self.nilai, value='wanita', command=self.gender)
#             rb_pria.pack()
#             rb_wanita.pack()
#             # print("Nilai:", self.nilai.get())
#         def gender(self):
#             print("Nilai:", self.nilai.get())

# root = Tk()
# my_gui = MyFirstGUI(root)
# root.mainloop()

haha = 1,23,4

haha[0] = 2
print(haha)