nilai_angka = int(input('Masukkan nilai angka: '))
nilai_huruf = ''

if nilai_angka >= 85: 
    nilai_huruf = 'A'
elif nilai_angka >= 80:
    nilai_huruf = 'A-'
elif nilai_angka >= 75:
    nilai_huruf = 'B+'
elif nilai_angka >= 70:
    nilai_huruf = 'B'

print(nilai_huruf)

number_1 = int(input("First number: "))
number_2 = int(input("Second number: "))
result = number_1 + number_2
print("The result is " str(result)")