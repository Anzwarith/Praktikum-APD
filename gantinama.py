import getpass
akuns = []

print("Halo, Selamat datang di VacaGO, kamu ingin login sebagai apa?")
print("――――――――――――――――――――――――")
print("1. Admin VacaGO")
print("2. User biasa")
print("――――――――――――――――――――――――")
Opsi = input("Pilih opsi: ")
print(" ")

if Opsi == "1":
    print("Halo admin baru, silahkan daftar dulu username dan password kamu disini ya.")
    USERNAME = input("Buat username Anda: ")
    akuna = False
    for akun in akuns:
        if akun[0] == USERNAME:
            akuna = True
            break
    if akuna:
        print("Username yang anda buat telah dipakai, silahkan pilih username yang lain.")
    else:
        PASSWORD = input("Buat password Anda: ")
        akuns.append([USERNAME, PASSWORD, []])
        print(f"Akun anda telah berhasil terdaftar. Selamat datang admin baru VacaGO.")
    
    if Opsi == 2:
        print("Halo! Selamat datang di VacaGO. Tempat pembelian tiket pesawat online terbaikmu")
        print("Silahkan anda membuat akun jika belum mempunyai akun, jika sudah silahkan Login kembali")
        print("――――――――――――――――――――――――")
        print("1. Buat Akun baru")
        print("2. Login")
        print("3. Keluar")
        print("――――――――――――――――――――――――")
        opsi = input("Pilih opsi: ")
        print(" ")

    if opsi == "1":
        print("Hai kamu, baru memakai VacaGO ya? Silahkan buat akun dulu ya")
        Username = input("Buat username Anda: ")
        akuna = False
        for akun in akuns:
            if akun[0] == Username:  # Memeriksa jika username telah terpakai atau belum
                akuna = True
                break
        if akuna:
            print("Username telah terdaftar! Silahkan login jika telah mempunyai akun atau buat akun baru.")
        else:
            Password = input("Buat Password Anda: ")
            akuns.append([Username, Password, []])  # Menyimpan username dan Password
            print(f"Akun Anda berhasil terdaftar dengan ID: {Username}")

    elif opsi == "2":
        print("Hi, Selamat datang kembali ya. Yuk login dulu")
        Username = input("Username: ")
        Password = getpass.getpass("Password: ")
        for akun in akuns:
            if akun[0] == Username and akun[1] == Password:  # Masukkan kembali Username dan Password
                while True:
                    print(f"\nSelamat datang {Username}!")
                    print("―――――――――――Menu―――――――――――")
                    print("1. Beli Tiket Pesawat")
                    print("2. Lihat Jadwal Penerbangan yang telah dipesan")
                    print("3. Edit Jadwal Penerbangan Anda")
                    print("4. Cancel Tiket Penerbangan")
                    print("5. Keluar")
                    print("――――――――――――――――――――――――――――")

                    status = input("Pilih opsi: ")
                    print(" ")

                    if status == "1":
                        tujuan = input("Masukkan tujuan: ")
                        harga = float(input("Masukkan harga: "))
                        akun[2].append([tujuan, harga])  # Melakukan pembelian Tiket
                        print("Tiket Anda sudah dipesan.\n")

                    elif status == "2":
                        if akun[2]:
                            for indeks, ticket in enumerate(akun[2]):  # Menampilkan semua tiket yang telah dibeli
                                print(f"{indeks + 1}. Tujuan: {ticket[0]}, Harga: {ticket[1]}")
                        else:
                            print("Saat ini Anda tidak memiliki jadwal penerbangan yang dipesan\n")

                    elif status == "3":
                        if not akun[2]:
                            print("Tidak ada tiket yang bisa diedit.")
                        else:
                            edit = int(input("Tiket nomor berapa yang ingin Anda edit: ")) - 1
                            if 0 <= edit < len(akun[2]):
                                tujuan_baru = input("Masukkan tujuan yang baru: ")
                                harga_baru = float(input("Masukkan harga yang baru: "))
                                print("Apa Anda yakin ingin mengedit tiket ini?")
                                print("1. Iya")
                                print("2. Tidak")
                                memastikan_edit = input("Pilih: ")
                                if memastikan_edit == "1":
                                    akun[2][edit] = [tujuan_baru, harga_baru]  # Mengedit tiket
                                    print("Tiket yang Anda pilih sudah diedit!\n")
                                elif memastikan_edit == "2":
                                    print("Aksi untuk mengedit tiket dibatalkan.")
                                else:
                                    print("Mohon pilih '1' atau '2'")
                            else:
                                print("Tidak ada nomor tiket yang Anda maksud, pastikan Anda memiliki jadwal penerbangan yang telah dipesan ya.\n")

                    elif status == "4":
                        if not akun[2]:
                            print("Tidak ada tiket yang bisa dihapus.")
                        else:
                            hapus = int(input("Tiket nomor berapa yang ingin dihapus: ")) - 1
                            if 0 <= hapus < len(akun[2]):
                                print("Apa Anda yakin ingin membatalkan penerbangan ini?")
                                print("1. Iya")
                                print("2. Tidak")
                                memastikan_hapus = input("Pilih: ")
                                if memastikan_hapus == "1":
                                    del akun[2][hapus]  # Menghapus tiket dari jadwal anda
                                    print("Tiket yang Anda pilih sudah dihapus!\n")
                                elif memastikan_hapus == "2":
                                    print("Aksi untuk menghapus dibatalkan.")
                                else:
                                    print("Mohon pilih '1' atau '2'")
                            else:
                                print("Tidak ada nomor tiket yang Anda maksud, silahkan input ulang.\n")

                    elif status == "5":
                        print("Terima kasih telah memakai VacaGO! Sampai ketemu lagi ya.\n")
                        break

                    else:
                        print("Input yang Anda masukkan tidak valid, silahkan pilih salah satu dari opsi dibawah.\n")
                break
        else:
            print("Usernaem atau Password yang Anda masukkan salah, silahkan mencoba lagi.\n")

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