nama = "MUAZ       IBNU  SAFAR "

# petunjuk:
# lihat screenshot
# ganti angka 1000 dengan statement yg benar
# output gunakan print() dan f""

print("")
print("------------------------------")
print("")
print(f"nama: '{nama}'")
print("")
print("------------------------------")

print("")
print("panjang:", len(nama))
print(f"nama di-trim: '{nama.strip()}'")
print("panjang setelah trim:", len(nama.strip()))

print("")
print("huruf ke-1:", nama[0])
print("dari huruf ke-2 sampai 4:", nama[1:4])
print("dari huruf ke-4 sampai akhir:", nama[3:])

print("")
print("4 huruf pertama:", nama[:4])
print("5 huruf terakhir:", nama[-5:])

print("")
print("ada kata 'AFA'?", "AFA" in nama)
print("ada kata 'afa'?", "afa" in nama)
print("ada huruf 'x'?", "x" in nama)
print("tidak ada kata 'wkwk'?", "wkwk" not in nama)
