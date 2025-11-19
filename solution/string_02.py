nama = "MUAZ       IBNU  SAFAR "

# petunjuk:
# lihat screenshot
# hasil proses ditampung di variabel, namai "hasil"
# ganti angka 1000 dgn variabel tersebut
# output gunakan print() dan f""

print("\n------------------------------\n")
print(f"nama: '{nama}'")
print("\n------------------------------\n")


print("panjang nama berapa karakter")
# variabel = len(var)
hasil = len(nama)
print("hasil:", hasil)

print("\nnama jika di-trim")
# variabel = .strip()
hasil = nama.strip()
print(f"hasil: '{hasil}'")


print("\npanjang nama setelah di-trim berapa karakter")
# variabel = .strip()
# variabel = len(variabel)
hasil = nama.strip()
hasil = len(hasil)
print(f"hasil: '{hasil}'")


print("\nnama huruf ke-1")
# variabel = var[x]
hasil = nama[0]
print("hasil:", hasil)


print("\nnama dari huruf ke-2 sampai 4")
# variabel = var[x:y]
hasil = nama[1:4]
print("hasil:", hasil)


print("\nnama dari huruf ke-4 sampai akhir")
# variabel = var[x:]
hasil = nama[3:]
print("hasil:", hasil)


print("\nnama 4 huruf pertama")
# variabel = var[:x]
hasil = nama[:4]
print("hasil:", hasil)


print("\nnama 5 huruf terakhir")
# variabel = var[-x:])
hasil = nama[-5:]
print("hasil:", hasil)


print("\ncek di nama apakah ada kata 'AFA'?")
# variabel = <string> in var
hasil = "AFA" in nama
print("hasil:", hasil)


print("\ncek di nama apakah ada kata 'afa'?")
# variabel = <string> in var
hasil = "afa" in nama
print("hasil:", hasil)


print("\ncek di nama apakah ada huruf 'x'?")
# variabel = <string> in var
hasil = "x" in nama
print("hasil:", hasil)


print("\ncek di nama apakah TIDAK ada kata 'wkwk'?")
# variabel = <string> not in var
hasil = "wkwk" not in nama
print("hasil:", hasil)
