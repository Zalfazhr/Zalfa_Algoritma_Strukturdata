# Variabel global untuk menyimpan daftar buku
buku = []

# Fungsi untuk menampilkan semua data
def show_data():
    if len(buku) <= 0:
        print("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print(f"[{indeks}] {buku[indeks]}")

# Fungsi untuk menambahkan data
def insert_data():
    buku_baru = input("Judul Buku: ")
    buku.append(buku_baru)
    print(f"Buku '{buku_baru}' telah ditambahkan.")

# Fungsi untuk mengedit data
def edit_data():
    show_data()
    try:
        indeks = int(input("Inputkan ID buku: "))
        if indeks < 0 or indeks >= len(buku):
            print("ID salah")
        else:
            judul_baru = input("Judul baru: ")
            buku[indeks] = judul_baru
            print(f"Buku dengan ID [{indeks}] telah diubah menjadi '{judul_baru}'.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

# Fungsi untuk menghapus data
def delete_data():
    show_data()
    try:
        indeks = int(input("Inputkan ID buku: "))
        if indeks < 0 or indeks >= len(buku):
            print("ID salah")
        else:
            removed_book = buku.pop(indeks)
            print(f"Buku '{removed_book}' telah dihapus.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

# Fungsi untuk menampilkan menu
def show_menu():
    while True:
        print("\n----------MENU---------")
        print("[1] Show Data")
        print("[2] Insert Data")
        print("[3] Edit Data")
        print("[4] Delete Data")
        print("[5] Exit")
        
        menu = input("PILIH MENU> ")
        
        if menu == '1':
            show_data()
        elif menu == '2':
            insert_data()
        elif menu == '3':
            edit_data()
        elif menu == '4':
            delete_data()
        elif menu == '5':
            print("Terima kasih! Keluar dari program.")
            break  # Menghentikan loop dan keluar dari program
        else:
            print("Salah pilih!")

if __name__ == "__main__":
    show_menu()
