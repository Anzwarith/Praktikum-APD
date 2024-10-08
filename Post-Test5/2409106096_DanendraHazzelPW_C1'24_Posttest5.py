import getpass
akuns = []
akunAdmin = []
jadwal_penerbangan = []
akunpake = []
keluar = False

# Menu Login awal
while keluar == False:
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
                akuna = False
                for akun in akuns:
                    if akun[0] == Username:
                        akuna = True
                        break
                if akuna:
                    print("Username telah terdaftar! Silahkan login jika telah mempunyai akun atau buat akun baru.")
                else:
                    Password = input("Buat password Anda: ")
                    akuns.append([Username, Password, []])
                    print(f"Akun Anda telah berhasil terdaftar dengan ID: {Username}")
            
            # Login kembali
            elif opsi == "2":
                print("Hi, Selamat datang kembali ya. Yuk login dulu")
                Username = input("Username: ")
                Password = getpass.getpass("Password: ")
                for akun in akuns:
                    if akun[0] == Username and akun[1] == Password:  # Masukkan kembali Username dan Password
                        akunpake = akun
                        
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
                                for i, tiket in enumerate(jadwal_penerbangan):
                                    print(f"{i + 1}. Tujuan : {tiket[0]}, Harga : {tiket[1]}")
                                Jadwal = input("Pilih tujuan : ")
                                bayar = float(input("Masukkan uang : "))
                                
                                for i, tiket in enumerate(jadwal_penerbangan):
                                    if Jadwal == str(i+1):
                                        if bayar >= tiket[1]:
                                            akunpake[2].append([tiket[0]])
                                            print("Tiket anda telah berhasil dipesan")
                                            
                                        else:
                                            print("Maaf, uang yang anda input tidak mencukupi harga penerbangan")
                                if int(Jadwal) > len(jadwal_penerbangan):
                                    print("Maaf tiket yang anda cari tidak tersedia saat ini")
                                
                            elif status == "2":
                                if jadwal_penerbangan:
                                    for indeks, ticket in enumerate(jadwal_penerbangan):  # Menampilkan semua tiket yang telah dibeli
                                        print(f"{indeks + 1}. Tujuan: {ticket[0]}, Harga: {ticket[1]}")
                                else:
                                    print("Saat ini Anda tidak memiliki jadwal penerbangan yang dipesan\n")
                                    
                            elif status == "3":
                                if not jadwal_penerbangan:
                                    print("Tidak ada tiket yang bisa dihapus.")
                                else:
                                    hapus = int(input("Tiket nomor berapa yang ingin dihapus: ")) - 1
                                    if 0 <= hapus < len(jadwal_penerbangan):
                                        print("Apa Anda yakin ingin membatalkan penerbangan ini?")
                                        print("1. Iya")
                                        print("2. Tidak")
                                        memastikan_hapus = input("Pilih: ")
                                        if memastikan_hapus == "1":
                                            del jadwal_penerbangan[hapus]  # Menghapus tiket dari jadwal anda
                                            print("Tiket yang Anda pilih sudah dihapus!\n")
                                        elif memastikan_hapus == "2":
                                            print("Aksi untuk menghapus dibatalkan.")
                                        else:
                                            print("Mohon pilih '1' atau '2'")
                                    else:
                                        print("Tidak ada nomor tiket yang Anda maksud, silahkan input ulang.\n")
                                        
                            elif status == "4":
                                if jadwal_penerbangan:
                                    for indeks, flight in enumerate(jadwal_penerbangan):
                                        print(f"{indeks + 1}. Tujuan {flight[0]}, Harga: {flight[1]}")
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
                akuna = False
                for akun in akunAdmin:
                    if akun[0] == Username:  # Memeriksa jika username telah terpakai atau belum
                        akuna = True
                        break
                if akuna:
                    print("Username telah terpakai! Silahkan gunakan username lainnya")
                else:
                    Password = input("Buat Password Anda: ")
                    akunAdmin.append([Username, Password, []])  # Menyimpan username dan Password
                    print(f"Akun Anda berhasil terdaftar dengan ID: {Username}")
            
            # Login kembali
            elif opsi == "2":
                print("Hii Admin, selamat datang kembali ya. Silahkan login dulu")
                Username = input("Username: ")
                Password = getpass.getpass("Password: ")
                for akun in akunAdmin:
                    if akun[0] == Username and akun[1] == Password:  # Masukkan kembali Username dan Password
                        
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
                                jadwal_penerbangan.append([tujuan, harga])
                                print("Penerbangan ke {tujuan} dengan harga {harga} telah berhasil ditambahkan ")
                                
                            elif status == "2":
                                if jadwal_penerbangan:
                                    for indeks, tiket in enumerate(jadwal_penerbangan):
                                        print(f"{indeks + 1}. Tujuan : {tiket[0]}, Harga {tiket[1]}")
                                else:
                                    print("Saat ini anda belum membuat jadwal penerbangan")
                                    
                            elif status == "3":
                                if not jadwal_penerbangan:
                                    print("Tidak ada tiket yang bisa dihapus.")
                                else:
                                    hapus = int(input("Tiket nomor berapa yang ingin dihapus: ")) - 1
                                    if 0 <= hapus < len(jadwal_penerbangan):
                                        print("Apa Anda yakin ingin membatalkan penerbangan ini?")
                                        print("1. Iya")
                                        print("2. Tidak")
                                        memastikan_hapus = input("Pilih: ")
                                        if memastikan_hapus == "1":
                                            del jadwal_penerbangan[hapus]  # Menghapus tiket dari jadwal anda
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
                    continue
                                
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