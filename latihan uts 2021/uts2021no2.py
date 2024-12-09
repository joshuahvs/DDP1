def my_median(lst):

    if len(lst) == 0:
        return None
    else:
        x = sorted(lst)
        if len(x) %2:
            return x[len(x)//2]
        else:
            return (x[len(x)//2] + x[len(x)//2-1]) /2
        
    
print(my_median([20]))
print(my_median([3,1]))
print(my_median([4,2,3,1]))
print(my_median([3,1,20]))
print(my_median([]))