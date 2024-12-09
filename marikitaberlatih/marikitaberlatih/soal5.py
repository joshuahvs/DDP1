bilangan = int(input("bilangan bulat: "))
digit_ke = int(input("digit ke-n dari belakang: "))

pembagi = 1
for i in range(digit_ke-1):
    pembagi *= 10

markicob = bilangan//pembagi
angka_yang_dicari = markicob%10

print(f"digitnya adalah {angka_yang_dicari}")
