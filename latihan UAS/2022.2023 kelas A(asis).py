# daftar_nilai = {"Matematika": {"Ani": 74,"Anto": 77,"Budi": 98,"Bunga": 90,"Chandra": 40,"Cinta": 54,"Danang": 86,"Donita": 98,"Einstein": 99,"Elisa": 76},
#                 "Fisika": {"Ani": 10,"Anto": 20,"Budi": 30,"Bunga": 40,"Chandra": 50,"Cinta": 60,"Danang": 70,"Donita": 80,"Einstein": 100,"Elisa": 90},
#                 "Bahasa Indonesia": {"Ani": 89,"Anto": 90,"Budi": 95,"Bunga": 97,"Chandra": 87,"Cinta": 99,"Danang": 89,"Donita": 90,"Einstein": 60,"Elisa": 89},
#                 "Geografi": {"Ani": 70,"Anto": 70,"Budi": 70,"Bunga": 70,"Chandra": 70,"Cinta": 70,"Danang": 70,"Donita":70,"Einstein": 75,"Elisa": 90},
#                 "Sejarah": {"Ani": 40,"Anto": 50,"Budi": 90,"Bunga": 20,"Chandra": 40,"Cinta": 80,"Danang": 40,"Donita": 95,"Einstein": 85,"Elisa": 100}}

for subject, students in daftar_nilai.items():
    nilai_tertinggi = 0
    nama_siswa = ''
    for student in students:
        if students[student] > nilai_tertinggi:
            nilai_tertinggi = students[student]
            nama_siswa = student
    print(f'nilai tertinggi untuk mata pelajaran {subject} diraih oleh {nama_siswa}')


# network = {"Safira": {"Affan", "Kadek", "Mutia", "Nurmala"},
#             "Affan": {"Safira", "Ridwan", "Mutia", "Ilham"},
#             "Kadek": {"Safira", "Usep", "Mutia", "Gio"},
#             "Mutia": {"Safira", "Affan", "Nurmala", "Dewi"}}

# def friends_of_friends(network, person):
#     all_friends = []
#     for friends in network[person]:
#         try:
#             for friend in network[friends]:
#                 if friend != person:
#                     all_friends.append(friend)
#         except:
#             pass

#     return set(all_friends)


# print(friends_of_friends(network, "Safira"))