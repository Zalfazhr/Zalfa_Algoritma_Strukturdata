listkota = [
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo','Jogjakarta','Semarang','Makassar'
  ]
for kota in listkota:
  print(kota)
  for i, kota in enumerate (listkota):
    print(i,kota)
## 0 sampai 4
for i in range(5):
  print("perulangan ke -", i)
  ## 10 sampai 15
for i in range(10, 16):
  print('i=',i)
## Bilangan genap kelipatan 2
for i in range(2,12,2):
  print('i=', i)
  ## Bilangan ganjil kelipatan 2
for bilangan_ganjil in range(1,12,2):
  print(bilangan_ganjil)
  
  