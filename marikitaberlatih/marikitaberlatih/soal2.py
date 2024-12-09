number = int(input("masukkan angka: "))
if number <= 0:
    print("angka harus lebih dari 0")
    exit()

factorial = 1
for i in range(number):
    factorial *= number
    number -= 1
print(factorial)