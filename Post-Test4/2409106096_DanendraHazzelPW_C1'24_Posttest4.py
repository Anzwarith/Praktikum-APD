USERNAME = "Hazzel"
PASSWORD = 96
loop = 0
while loop < 3:
    username = input("Masukkan username : ")
    password = int(input("Masukkan password : "))
    
    if username == "Hazzel" and password == 96:
        print("Anda telah berhasil login, ingin melakukan pemesanan?")
        coba = input()
        if coba == "tidak":
            print("Baiklah, sampai jumpa nanti")
            break
        else:
            print("Selamat datang pada pemesanan tiket online, ingin menonton film apa?")
            print("1.Dragon ball 2.Battle Z 3.Ben 10")
            film = input()
        nama = input("Silahkan isi nama anda disini : ")
        hari = input("Ingin menonton di hari apa : ")
        jumlahuang = int(input("masukkan uang anda : "))
        if hari == "senin" or hari == "selasa" or hari == "rabu" or hari == "kamis":
            hargatiket = 40000
        else:
            if hari == "jumaat":
                hargatiket = 45000
            else:
                if hari == "sabtu":
                    hargatiket = 55000
                else:
                    if hari == "minggu":
                        hargatiket = 60000
        if jumlahuang >= hargatiket:
            print("Pemesanan atas nama " + nama + " pada hari " + hari + " telah berhasil dilakukan, selamat menikmati")
            break
        else:
            print("maaf uang anda tidak cukup untuk menonton film yang anda inginkan pada hari " + hari)
            break
    else:
        print("Username atau Password anda salah. Ingin mencoba lagi?")
        coba = input()
        if coba == "iya":
            loop = loop + 1
            print ("anda sudah mencoba sebanyak " + str(loop) + " kali")
        else:
            print("Baik, semoga harimu menyenangkan")
