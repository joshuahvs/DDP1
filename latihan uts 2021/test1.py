file = open("uts2021no1.txt", "r")
# for line in file:
#     # word = line.split()
#     # print(word)
#     print(line)

# readline = file.readline()
# readline2 = file.readline()
# print(readline)
# print(readline2)

# read = file.read()
# word = read.split()
# print(word)

# readlines = file.readlines()
# print(readlines)

readlines = file.readlines()
# per_line = readlines.seperate("\n")
# print(per_line)

for line in readlines:
    word = line.split()
    print(word)

