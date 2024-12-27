def main():
    # Input langsung yang sudah ditentukan
    nama = "Zalfa"
    usia = 21
    alamat = "jalan Srimenanti 5, sungailiat"
    hobi = "memasak"

    # Menampilkan informasi biodata
    print("\n=== Biodata Pengguna ===")
    print(f"Nama   : {nama}")
    print(f"Usia   : {usia} tahun")
    print(f"Alamat : {alamat}")
    print(f"Hobi   : {hobi}")

if __name__ == "__main__":
    main()

def cetak_pola(baris):
    # Menggunakan perulangan untuk mencetak pola segitiga
    for i in range(1, baris + 1):
        # Mencetak bintang sesuai dengan nomor baris
        print(' ' * (baris - i) + '*' * i)

def cetak_pola(baris):
    # Menggunakan perulangan untuk mencetak pola segitiga
    for i in range(1, baris + 1):
        # Mencetak spasi dan bintang sesuai dengan nomor baris
        print(' ' * (baris - i) + '*' * i)

def main():
    # Contoh input yang bisa diuji
    baris = 5  # Anda bisa mengubah nilai ini untuk menguji jumlah baris yang berbeda

    print(f"Mencetak pola bintang segitiga dengan {baris} baris:\n")
    
    # Memanggil fungsi untuk mencetak pola
    cetak_pola(baris)

if __name__ == "__main__":
    main()

def hitung_gaji(tarif_per_jam, jam_kerja_per_hari):
    # Jam kerja normal
    jam_normal = 8
    total_gaji = 0

    # Menghitung gaji untuk setiap hari kerja
    for jam in jam_kerja_per_hari:
        if jam > jam_normal:
            # Menghitung lembur
            lembur = jam - jam_normal
            gaji_hari = (jam_normal * tarif_per_jam) + (lembur * tarif_per_jam * 1.5)
        else:
            # Gaji tanpa lembur
            gaji_hari = jam * tarif_per_jam
        
        total_gaji += gaji_hari

    return total_gaji

def main():
    # Contoh input yang bisa diuji
    tarif_per_jam = 100000  # Tarif gaji per jam
    hari_kerja = 5          # Jumlah hari kerja dalam sebulan
    jam_kerja_per_hari = [9, 8, 7, 10, 6]  # Jam kerja untuk setiap hari

    print(f"Tarif gaji per jam: {tarif_per_jam}")
    print(f"Jumlah hari kerja: {hari_kerja}")
    print("Jam kerja per hari:", jam_kerja_per_hari)

    # Menghitung total gaji bulanan
    total_gaji = hitung_gaji(tarif_per_jam, jam_kerja_per_hari)
    
    # Menampilkan total gaji bulanan
    print(f"\nTotal gaji bulanan: {total_gaji:.2f}")

if __name__ == "__main__":
    main()

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Error: Pembagian dengan nol tidak diperbolehkan."
    else:
        return a / b

def main():
    # Contoh input yang bisa diuji
    angka1 = 10
    angka2 = 5

    print(f"Angka pertama: {angka1}")
    print(f"Angka kedua: {angka2}")

    print("\nPilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    # Memilih operasi (misalnya kita pilih penjumlahan)
    pilihan = '1'  # Anda dapat mengubah ini untuk menguji pilihan lain

    # Memanggil fungsi yang sesuai berdasarkan pilihan pengguna
    if pilihan == '1':
        hasil = tambah(angka1, angka2)
        operasi = "Penjumlahan"
    elif pilihan == '2':
        hasil = kurang(angka1, angka2)
        operasi = "Pengurangan"
    elif pilihan == '3':
        hasil = kali(angka1, angka2)
        operasi = "Perkalian"
    elif pilihan == '4':
        hasil = bagi(angka1, angka2)
        operasi = "Pembagian"
    else:
        print("Pilihan tidak valid.")
        return

    # Menampilkan hasil
    print(f"\nHasil {operasi} antara {angka1} dan {angka2} adalah: {hasil}")

if __name__ == "__main__":
    main()

def kategori_usia(usia):
    # Menentukan kategori usia berdasarkan rentang yang diberikan
    if 0 <= usia <= 5:
        return "Balita"
    elif 6 <= usia <= 12:
        return "Anak-anak"
    elif 13 <= usia <= 17:
        return "Remaja"
    elif 18 <= usia <= 59:
        return "Dewasa"
    elif usia >= 60:
        return "Lansia"
    else:
        return "Usia tidak valid"

def main():
    # Contoh input yang bisa diuji
    contoh_usia = [3, 10, 15, 30, 65, -1]  # Daftar contoh usia

    for usia in contoh_usia:
        print(f"Usia: {usia} tahun - Kategori: {kategori_usia(usia)}")

    # Jika ingin meminta input dari pengguna
    try:
        usia_input = int(input("\nMasukkan usia Anda: "))
        
        # Mendapatkan kategori berdasarkan usia
        kategori = kategori_usia(usia_input)
        
        # Mencetak hasil kategori
        print(f"Kategori usia: {kategori}")

    except ValueError:
        print("Silakan masukkan angka yang valid.")

if __name__ == "__main__":
    main()
