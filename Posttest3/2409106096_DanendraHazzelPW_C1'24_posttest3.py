print("Selamat datang pada pemesanan tiket online, ingin menonton film apa?")
print("1.Dragon ball 2.Battle Z 3.Ben 10")
# memasukkan film yang ingin dipesan
film = input()

print("Silahkan isi nama anda disini")
# memasukkan nama yang melakukan pemesanan
nama = input()

print("Ingin menonton di hari apa")
# memasukkan hari apa anda akan menonton film
hari = input()

print("masukkan uang anda")
# memasukkan jumlah uang yang anda miliki
jumlahuang = float(input())
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
    print("Pemesanan atas nama " + nama + " pada hari " + hari + " telah berhasil dilakukan")
else:
    print("maaf uang anda tidak cukup untuk menonton film yang anda inginkan pada hari " + hari)