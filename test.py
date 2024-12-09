saldo_akhir_bulan = 100000000
n = 12
bunga = 2.5
for bulan in range(0,n):
  saldo_akhir_bulan = saldo_akhir_bulan + (saldo_akhir_bulan * (bunga/100))
  print(f'Bulan ke-{bulan:<3d} | Saldo = Rp. {saldo_akhir_bulan:<20,.2f}  |')