listkota = ['Jakarta', 'Surabaya', 'Depok', 'Bekasi', 'Solo','Jogjakarta', 'Semarang','Makassar']
# bermain index
i = 0
while i < len(listkota):
    print(listkota[i])
    i += 1
#perulangan while
a = int(input('masukan bilangan ganjil lebih dari 50: '))
while a % 2 != 1 or a <= 50 :
    print('input tidak valid. Silahkan coba lagi.')
    a = int(input('masukan bilangan ganjil lebih dari 50:'))
    print('input valid', a)

#PERULANGAN DENGAN CONTINUE
listkota = ['Jakarta', 'Surabaya', 'Bangka','Sulawesi','Lombok', 'Depok','Jogjakarta', 'Makassar']
KotaYangDicari = input('Bangka')
i = 0
while i < len(listkota):
   if listkota[i].lower()== KotaYangDicari.lower():
     print('Ketemu di index:', i)
     break
   print('bukan', listkota[i])
   i += 1
else:
  print('Maaf, kota yang anda cari tidak ditemukan,')