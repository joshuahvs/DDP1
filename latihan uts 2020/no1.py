#guess the output

#Masukkan NPM anda
score = input("Masukkan NPM anda; ")
mystery = 0
for chara in score:
    if int (chara) == 9:
        break
    if int (chara) % 2 > 0: 
        continue
    else:
        mystery += int (chara)
print(mystery)

#2306165540
#output = 206640
#WEHH SALAH GOBLOG
#output = 2 + 6+6+4 = 18