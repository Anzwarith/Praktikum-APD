import getpass

# 5 Variabel Global
akuns = {}
akunAdmin = {}
jadwal_penerbangan = {}
akunpake = None
keluar = False
MINIMUM_SALDO = 100000  # Global variable baru
MAX_TIKET = 5  # Global variable baru
ADMIN_KEY = "VACAGO2024"  # Global variable baru

# 3 Fungsi dengan Parameter
def validasi_pembayaran(harga, pembayaran):
    """Fungsi untuk validasi pembayaran tiket"""
    return pembayaran >= harga

def cek_kapasitas_tiket(akun, max_tiket=MAX_TIKET):
    """Fungsi untuk mengecek jumlah tiket user"""
    return len(akun["tiket"]) < max_tiket

def hitung_total_harga(harga_tiket, jumlah):
    """Fungsi untuk menghitung total harga tiket"""
    return harga_tiket * jumlah

# 3 Fungsi tanpa Parameter
def tampilkan_header():
    """Fungsi untuk menampilkan header aplikasi"""
    print("="*40)
    print("Welcome to VacaGO - Your Best Flight Partner")
    print("="*40)
    return True

def get_waktu_terbang():
    """Fungsi untuk mendapatkan jadwal default"""
    return ["07:00", "12:00", "15:00", "19:00"]

def generate_booking_id():
    """Fungsi untuk generate ID booking"""
    import random
    return f"VG-{random.randint(1000,9999)}"

# 2 Prosedur
def cetak_tiket(username, tujuan, waktu):
    """Prosedur untuk mencetak tiket"""
    print("\n=== TIKET VACAGO ===")
    print(f"Booking ID: {generate_booking_id()}")
    print(f"Nama: {username}")
    print(f"Tujuan: {tujuan}")
    print(f"Waktu: {waktu}")
    print("==================\n")

def tampilkan_riwayat(tiket_list):
    """Prosedur untuk menampilkan riwayat tiket"""
    print("\n=== RIWAYAT PEMESANAN ===")
    for idx, tiket in enumerate(tiket_list, 1):
        print(f"{idx}. {tiket}")
    print("========================\n")

# Menu Login awal
while not keluar:
    tampilkan_header()
    print("Halo, Selamat datang di VacaGO, kamu ingin login sebagai siapa?")
    print("――――――――――――――――――――――――")
    print("1. User biasa")
    print("2. Admin VacaGO")
    print('3. Keluar')
    print("――――――――――――――――――――――――")
    opsi = input("Pilih opsi: ")
    print(" ")

    # Opsi 1 User
    if opsi == "1":
        #Menu Login User
        while True:
            print("Halo! Selamat datang di VacaGO. Tempat pembelian tiket pesawat online terbaikmu")
            print("Silahkan anda membuat akun jika belum mempunyai akun, jika sudah silahkan Login kembali")
            print("――――――――――――――――――――――――")
            print("1. Buat Akun baru")
            print("2. Login")
            print("3. Keluar")
            print("――――――――――――――――――――――――")
            opsi = input("Pilih opsi: ")
            print(" ")

            # Buat Akun 
            if opsi == "1":
                # Variabel Lokal
                username = input("Buat username Anda: ")
                if username in akuns:
                    print("Username telah terdaftar! Silahkan login jika telah mempunyai akun atau buat akun baru.")
                else:
                    password = input("Buat password Anda: ")  # Variabel Lokal
                    saldo_awal = float(input("Masukkan saldo awal: "))  # Variabel Lokal
                    akuns[username] = {"password": password, "tiket": [], "saldo": saldo_awal}
                    print(f"Akun Anda telah berhasil terdaftar dengan ID: {username}")
            
            # Login kembali
            elif opsi == "2":
                print("Hi, Selamat datang kembali ya. Yuk login dulu")
                username = input("Username: ")
                password = getpass.getpass("Password: ")
                if username in akuns and akuns[username]["password"] == password:
                    akunpake = akuns[username]
                    
                    # Menu utama user
                    while True:
                        print(f"\nSelamat datang {username}!")
                        print("―――――――――――Menu―――――――――――")
                        print("1. Beli Tiket Pesawat")
                        print("2. Lihat Jadwal Penerbangan yang telah dipesan")
                        print("3. Cancel Tiket Penerbangan")
                        print("4. Lihat Jadwal Penerbangan")
                        print("5. Log Out")
                        print("――――――――――――――――――――――――――――")

                        status = input("Pilih opsi: ")
                        print(" ")

                        if status == "1":
                            for id, tiket in jadwal_penerbangan.items():
                                print(f"{id}. Tujuan : {tiket['tujuan']}, Harga : {tiket['harga']}")
                            
                            jadwal = input("Pilih tujuan : ")  # Variabel Lokal
                            jumlah_tiket = int(input("Masukkan jumlah tiket: "))  # Variabel Lokal
                            
                            if jadwal in jadwal_penerbangan:
                                total_harga = hitung_total_harga(jadwal_penerbangan[jadwal]['harga'], jumlah_tiket)
                                if cek_kapasitas_tiket(akunpake):
                                    bayar = float(input("Masukkan uang : "))
                                    if validasi_pembayaran(total_harga, bayar):
                                        waktu_terbang = get_waktu_terbang()[0]
                                        akunpake["tiket"].append(jadwal_penerbangan[jadwal]['tujuan'])
                                        cetak_tiket(username, jadwal_penerbangan[jadwal]['tujuan'], waktu_terbang)
                                        print("Tiket anda telah berhasil dipesan")
                                    else:
                                        print("Maaf, uang yang anda input tidak mencukupi harga penerbangan")
                                else:
                                    print("Maaf, anda telah mencapai batas maksimum pembelian tiket")
                            else:
                                print("Maaf tiket yang anda cari tidak tersedia saat ini")
                            
                        elif status == "2":
                            if akunpake["tiket"]:
                                tampilkan_riwayat(akunpake["tiket"])
                            else:
                                print("Saat ini Anda tidak memiliki jadwal penerbangan yang dipesan\n")
                                
                        elif status == "3":
                            if not akunpake["tiket"]:
                                print("Tidak ada tiket yang bisa dihapus.")
                            else:
                                hapus = int(input("Tiket nomor berapa yang ingin dihapus: ")) - 1
                                if 0 <= hapus < len(akunpake["tiket"]):
                                    print("Apa Anda yakin ingin membatalkan penerbangan ini?")
                                    print("1. Iya")
                                    print("2. Tidak")
                                    memastikan_hapus = input("Pilih: ")
                                    if memastikan_hapus == "1":
                                        del akunpake["tiket"][hapus]
                                        print("Tiket yang Anda pilih sudah dihapus!\n")
                                    elif memastikan_hapus == "2":
                                        print("Aksi untuk menghapus dibatalkan.")
                                    else:
                                        print("Mohon pilih '1' atau '2'")
                                else:
                                    print("Tidak ada nomor tiket yang Anda maksud, silahkan input ulang.\n")
                                    
                        elif status == "4":
                            if jadwal_penerbangan:
                                for id, flight in jadwal_penerbangan.items():
                                    print(f"{id}. Tujuan {flight['tujuan']}, Harga: {flight['harga']}")
                            else:
                                print("Tidak ada jadwal penerbangan yang tersedia")

                        elif status == "5":
                            print("Terima kasih telah memakai VacaGO! Sampai ketemu lagi ya.\n")
                            break

                        else:
                            print("Input yang Anda masukkan tidak valid, silahkan pilih salah satu dari opsi dibawah.\n")
                    break
                else:
                    print("Username atau Password yang Anda masukkan salah, silahkan mencoba lagi.\n")

            elif opsi == "3":
                print("Apakah Anda yakin ingin keluar dari aplikasi? ")
                print("1. Iya")
                print("2. Tidak")
                pilih = input("Input pilihan: ")
                print(" ")
                if pilih == "1":
                    print("Terima kasih sudah menggunakan VacaGO, semoga harimu menyenangkan")
                    break
                elif pilih == "2":
                    continue
                else:
                    print("Input tidak valid, silahkan pilih '1' atau '2'\n")
            else:
                print("Input tidak valid, silahkan pilih 1, 2, atau 3") 
        continue    

    # Opsi 2 Admin
    if opsi == "2":
        # Menu Login Admin
        while True:
            print("Halo Admin! Selamat datang di VacaGO, sebelum itu silahkan pilih salah satu opsi dibawah ya")
            print("Jika kamu baru disini, silahkan buat akun terlebih dahulu, jika sudah ada akun, silahkan login kembali")
            print("――――――――――――――――――――――――")
            print("1. Buat Akun baru")
            print("2. Login")
            print("3. Keluar")
            print("――――――――――――――――――――――――")
            opsi = input("Pilih opsi: ")
            print(" ")

            # Buat Akun Admin
            if opsi == "1":
                print("Halo Admin baru, silahkan buat dulu username dan passwordmu disini ya")
                username = input("Buat username Anda: ")
                if username in akunAdmin:
                    print("Username telah terpakai! Silahkan gunakan username lainnya")
                else:
                    password = input("Buat Password Anda: ")
                    admin_key = input("Masukkan kunci admin: ")  # Menambah validasi admin
                    if admin_key == ADMIN_KEY:
                        akunAdmin[username] = {"password": password}
                        print(f"Akun Anda berhasil terdaftar dengan ID: {username}")
                    else:
                        print("Kunci admin tidak valid!")
            
            # Login kembali
            elif opsi == "2":
                print("Hii Admin, selamat datang kembali ya. Silahkan login dulu")
                username = input("Username: ")
                password = getpass.getpass("Password: ")
                if username in akunAdmin and akunAdmin[username]["password"] == password:
                    
                    # Menu Utama Admin
                    while True:
                        print(f"\nSelamat datang kembali Admin {username}!")
                        print("―――――――――――Menu―――――――――――")
                        print("1. Tambah Jadwal Penerbangan")
                        print("2. Lihat Jadwal Penerbangan yang telah dibuat")
                        print("3. Menghapus jadwal penerbangan")
                        print("4. Log Out")
                        print("――――――――――――――――――――――――――――")

                        status = input("Pilih opsi: ")
                        print(" ")
                        
                        if status == "1":
                            print("Silahkan tambah jadwal tiket penerbangan beserta harganya")
                            tujuan = input("Masukkan tujuan penerbangan: ")
                            harga = float(input("Masukkan harga: "))
                            waktu = get_waktu_terbang()  # Menggunakan fungsi untuk mendapatkan jadwal
                            id = str(len(jadwal_penerbangan) + 1)
                            jadwal_penerbangan[id] = {"tujuan": tujuan, "harga": harga, "waktu": waktu}
                            print(f"Penerbangan ke {tujuan} dengan harga {harga} telah berhasil ditambahkan ")
                            
                        elif status == "2":
                            if jadwal_penerbangan:
                                for id, tiket in jadwal_penerbangan.items():
                                    print(f"{id}. Tujuan : {tiket['tujuan']}, Harga {tiket['harga']}")
                                    print(f"   Waktu penerbangan tersedia: {', '.join(tiket['waktu'])}")
                            else:
                                print("Saat ini anda belum membuat jadwal penerbangan")
                                
                        elif status == "3":
                            if not jadwal_penerbangan:
                                print("Tidak ada tiket yang bisa dihapus.")
                            else:
                                hapus = input("Tiket nomor berapa yang ingin dihapus: ")
                                if hapus in jadwal_penerbangan:
                                    print("Apa Anda yakin ingin membatalkan penerbangan ini?")
                                    print("1. Iya")
                                    print("2. Tidak")
                                    memastikan_hapus = input("Pilih: ")
                                    if memastikan_hapus == "1":
                                        del jadwal_penerbangan[hapus]
                                        print("Tiket yang Anda pilih sudah dihapus!\n")
                                    elif memastikan_hapus == "2":
                                        print("Aksi untuk menghapus dibatalkan.")
                                    else:
                                        print("Mohon pilih '1' atau '2'")
                                else:
                                    print("Tidak ada nomor tiket yang Anda maksud, silahkan input ulang.\n")
                        
                        elif status == "4":
                            print("Sampai ketemu lagi di VacaGO")
                            break
                else:
                    print("Username atau Password yang Anda salah, silahkan coba lagi lain kali")
                    
            elif opsi == "3":
                print("Apakah Anda yakin ingin keluar dari aplikasi? ")
                print("1. Iya")
                print("2. Tidak")
                pilih = input("Input pilihan: ")
                print(" ")
                if pilih == "1":
                    print("Terima kasih sudah menggunakan VacaGO, semoga harimu menyenangkan")
                    break
                elif pilih == "2":
                    continue
                else:
                    print("Input tidak valid, silahkan pilih '1' atau '2'\n")
            else:
                print("Input tidak valid, silahkan pilih 1, 2, atau 3") 
        continue    