import getpass

akuns = {}
akunAdmin = {}
jadwal_penerbangan = {}
akunpake = None
keluar = False

# Menu Login awal
while not keluar:
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
                print("Hai kamu, baru memakai VacaGO ya? Silahkan buat akun dulu ya")
                Username = input("Buat username Anda: ")
                if Username in akuns:
                    print("Username telah terdaftar! Silahkan login jika telah mempunyai akun atau buat akun baru.")
                else:
                    Password = input("Buat password Anda: ")
                    akuns[Username] = {"password": Password, "tiket": []}
                    print(f"Akun Anda telah berhasil terdaftar dengan ID: {Username}")
            
            # Login kembali
            elif opsi == "2":
                print("Hi, Selamat datang kembali ya. Yuk login dulu")
                Username = input("Username: ")
                Password = getpass.getpass("Password: ")
                if Username in akuns and akuns[Username]["password"] == Password:
                    akunpake = akuns[Username]
                    
                    # Menu utama user
                    while True:
                        print(f"\nSelamat datang {Username}!")
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
                            Jadwal = input("Pilih tujuan : ")
                            bayar = float(input("Masukkan uang : "))
                            
                            if Jadwal in jadwal_penerbangan:
                                if bayar >= jadwal_penerbangan[Jadwal]['harga']:
                                    akunpake["tiket"].append(jadwal_penerbangan[Jadwal]['tujuan'])
                                    print("Tiket anda telah berhasil dipesan")
                                else:
                                    print("Maaf, uang yang anda input tidak mencukupi harga penerbangan")
                            else:
                                print("Maaf tiket yang anda cari tidak tersedia saat ini")
                            
                        elif status == "2":
                            if akunpake["tiket"]:
                                for indeks, ticket in enumerate(akunpake["tiket"]):
                                    print(f"{indeks + 1}. Tujuan: {ticket}")
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
                Username = input("Buat username Anda: ")
                if Username in akunAdmin:
                    print("Username telah terpakai! Silahkan gunakan username lainnya")
                else:
                    Password = input("Buat Password Anda: ")
                    akunAdmin[Username] = {"password": Password}
                    print(f"Akun Anda berhasil terdaftar dengan ID: {Username}")
            
            # Login kembali
            elif opsi == "2":
                print("Hii Admin, selamat datang kembali ya. Silahkan login dulu")
                Username = input("Username: ")
                Password = getpass.getpass("Password: ")
                if Username in akunAdmin and akunAdmin[Username]["password"] == Password:
                    
                    # Menu Utama Admin
                    while True:
                        print(f"\nSelamat datang kembali Admin {Username}!")
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
                            id = str(len(jadwal_penerbangan) + 1)
                            jadwal_penerbangan[id] = {"tujuan": tujuan, "harga": harga}
                            print(f"Penerbangan ke {tujuan} dengan harga {harga} telah berhasil ditambahkan ")
                            
                        elif status == "2":
                            if jadwal_penerbangan:
                                for id, tiket in jadwal_penerbangan.items():
                                    print(f"{id}. Tujuan : {tiket['tujuan']}, Harga {tiket['harga']}")
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
                
    if opsi == "3":
        keluar = True