#Operator Matematika
a,b = 10,3
print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)
print(a, '/', b, '=', a / b)
print(a, '%', b, '=', a % b)
print(a, '**', b, '=', a ** b)
print(a, '//', b, '=', a // b)
#Operator Komparasi atau Perbandingan
a,b=5,10
print(a, '>', b, '=', a > b)
print(a, '<', b, '=', a < b)
print(a, '==', b, '=', a == b)
print(a, '!=', b, '=', a != b)
print(a, '>=', b, '=', a >= b)
print(a, '<=', b, '=', a <= b)
# Penugasan Pertama
a=10
print('a=10->',a)
a+=5
print('a+=->',a)
a-=3
print('a-=3->',a)
a*=6
print('a*=6->',a)
a/=8
print('a/=8->',a)
#Karena a jadi float, maka ubah ke integer
a=int(a)
a%=9
print('a%=9->',a)
a//=6
print('a//=6->',a)
a**=1
print('a**=1->',a)
#Operator Logika
print(True and False)
print(1+2==3 and True)
print('----')
print(False or 1>5)
print(False or 5>2)
print('----')
print(not(1>5))
print(not(1<5))
#Operator Keanggotan
perusahaan = 'Microsoft'
list_pulau = ['Jawa','Sumatra','Sulawesi']
mahasiswa = {
    'nama': 'Zalfa Zahira',
    'asal': 'Bangka'
    }
print(
    "Apakah 'c' ada di variabel perusahan?",
    'c' in perusahaan
)
print(
    "Apakah 'z' ada di variabel perusahan?",
    'z' not in perusahaan
)
#Operator Identitas
a=5
b=5
nama_a='Zalfa'
nama_b='Zalfa'
print('a is b:', a is b)
print('a is not b:', a is not b)
print('nama_a is nama b:', nama_a is nama_b)
print('nama_a is not nama b:', nama_a is not nama_b)

