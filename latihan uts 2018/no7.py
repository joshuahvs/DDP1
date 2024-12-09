def mystery(filename):
    infile = open(filename, 'r')
    content = infile.read()
    infile.close()
    grades = content.split()
    print(grades)
    for grade in ['A', 'B', 'C', 'D', 'E']:
        num = grades.count(grade)
        if num > 0:
            print('{} students got {}'.format(num, grade))

mystery("file.txt")