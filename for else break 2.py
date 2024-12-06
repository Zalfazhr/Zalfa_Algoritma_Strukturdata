listKota = [ 
  'Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo',
  'Jogjakarta','Semarang','Makassar'
]

kotaYangDicari = input('Ketik nama kota yang kamu cari: Makassar')

for i, kota in enumerate (listKota):
  # kita ubah katanya ke Lowercase agar
  # menjadi case insensitive
  if kota.lower() == kotaYangDicari.lower(): 

    print('Kota yang anda cari berada pada indeks', i)
    break
else:
  print('Maaf, kota yang anda cari tidak ada')
