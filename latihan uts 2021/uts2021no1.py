kata_depan = ["dalam", "atas", "antara", "kepada", "akan", "terhadap", \
              "oleh", "dengan", "berkat", "tentang", "sampai", "guna", \
                "demi", "untuk", "bagi", "menurut"]

try:
    file = open("uts2021no1.txt", "r")
    counter = 0
    for line in file:
        words = line.split()
        print(words)
        for word in words:
            if word.lower() in kata_depan:
                counter += 1
    print(f"Banyaknya kata depan yang muncul adalah {counter}")

except FileNotFoundError:
    print("File tidak ada")