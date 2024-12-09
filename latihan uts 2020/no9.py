def total_penjualan(becak, delman, sepeda):
    total_becak = becak*3000000
    total_delman = delman*10000000
    total_sepeda = sepeda*2000000
    total = total_becak+total_delman+total_sepeda
    return total

print(total_penjualan(2,2,0))
print(total_penjualan(1,1,10))