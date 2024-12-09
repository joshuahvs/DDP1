number = 0
counter = 0
try:
    file = open("test1.txt", "r")
    for a in file:
        number_interger = int(a)
        number += number_interger
        counter += 1
    mean = number/counter
    print(mean)
    file.close()
except FileNotFoundError:
    print("Error, file tidak ada!")