nama_depan = "MUAZ"
nama_belakang = "ibnu safar"

# petunjuk:
# lihat screenshot
# hasil proses ditampung di variabel, namai "hasil"
# ganti angka 1000 variabel tersebut
# output gunakan print()

print("\n------------------------------\n")
print("nama_depan", nama_depan)
print("nama_belakang", nama_belakang)
print("\n------------------------------\n")


print("cek apakah type nama_depan itu string")
# variabel = type(var) == str
hasil = type(nama_depan) == str
print("hasil:", hasil)


print("\nnama lengkap")
# hasil = var1 + <spasi> + var2
hasil = nama_depan + " " + nama_belakang
print("hasil:", hasil)


print("\nnama lengkap dalam lowercase")
# variabel = .lower() + <spasi> + .lower()
hasil = nama_depan.lower() + " " + nama_belakang.lower()
print("hasil:", hasil)


print("\nnama lengkap dalam uppercase")
# variabel = .upper() + <spasi> + .upper()
hasil = nama_depan.upper() + " " + nama_belakang.upper()
print("hasil:", hasil)


print("\nnama lengkap dalam capital")
# variabel = .capitalize() + <spasi> + .capitalize()
hasil = nama_depan.capitalize() + " " + nama_belakang.capitalize()
print("hasil:", hasil)


print("\nnama lengkap dalam titlecase")
# variabel = .title() + <spasi> + .title()
hasil = nama_depan.title() + " " + nama_belakang.title()
print("hasil:", hasil)


print("\nnama lengkap dalam swapcase")
# variabel = .swapcase() + <spasi> + .swapcase()
hasil = nama_depan.swapcase() + " " + nama_belakang.swapcase()
print("hasil:", hasil)
