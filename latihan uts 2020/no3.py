x, y = 1, -1
# todo Implement counter =
#OUtput yang diinginkan x  =1, y=1
counter = 3
for index in range(0,counter):
    if x>= y:
        x,y = y,x
    elif x<y:
        x = x + 1 
    else:
        continue
print('Nilai x = {} dan y ={}'.format(x,y))