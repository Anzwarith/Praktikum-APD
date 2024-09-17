nama = input("masukkan Nama")
nim = input("masukkan Nim")
HargaGula = 21000

diskon = {
    "diskonGulaku" : 0.07,
    "diskonManisKita" : 0.11,
    "diskonGunungMadu" : 0.13
}

HargaAkhirGulaku = HargaGula * diskon["diskonGulaku"]
HargaAkhirManisKita = HargaGula * diskon["diskonManisKita"]
HargaAkhirGunungMadu = HargaGula * diskon["diskonGunungMadu"]

print(f"{nama} dengan NIM {nim} ingin membeli gula seharga Rp {HargaGula}")
print(f"jika dia membeli Gulaku ia harus membayar {HargaAkhirGulaku} setelah mendapat diskon 7%")
print(f"jika dia membeli ManisKita ia harus membayar {HargaAkhirManisKita} setelah mendapat diskon 11%")
print(f"jika dia membeli GunungMadu ia harus membayar {HargaAkhirGunungMadu} setelah mendapat diskon 13%")