def is_segitiga_siku(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
    
print(is_segitiga_siku(3,4,5))