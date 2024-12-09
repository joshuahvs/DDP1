def count_a_char(string, yang_dicari):
    karakter_dicari = 0
    for i in string:
        if i == yang_dicari:
            karakter_dicari += 1
    if karakter_dicari > 0:
         print(f"Ada {karakter_dicari} karakter {yang_dicari} di dalam {string}")
    else:
        print("None")
count_a_char("halo kelas b", "h")
count_a_char("halo kelas b", "c")