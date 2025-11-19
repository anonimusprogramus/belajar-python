nama = "MUAZ       IBNU  SAFAR "

# petunjuk:
# lihat screenshot
# hasil proses ditampung di variabel "hasil"
# ganti angka 1000 variabel "hasil" tersebut
# output gunakan print() dan f""

print("")
print("------------------------------")
print("")
print(f"nama: '{1000}'")
print(f"nama: '{nama}'")
print("")
print("------------------------------")

print("")

print("replace spasi dgn '-'")
# variabel = .replace(old, new)
print("hasil:", 1000)
hasil = nama.replace(" ", "-")
print("hasil:", hasil)

print("replace IBNU dgn 'ibin'")
# variabel = .replace(old, new)
print("hasil:", 1000)
hasil = nama.replace("IBNU", "ibin")
print("hasil:", hasil)

print("")

print("split nama jadi list")
# variabel = .split()
print("hasil:", 1000)
hasil = nama.split()
print("hasil:", hasil)

print("split nama jadi list -> join dgn 1 spasi")
# variabel = .split()
# variabel = <spasi>.join(variabel)
print("hasil:", 1000)
hasil = nama.split()
hasil = " ".join(hasil)
print("hasil:", hasil)

print("")
print("split nama jadi list -> balik pakai reversed() -> join dgn 1 spasi")
# info: fungsi reversed() tidak merubah variabel tapi mengembalikan copy hasil perubahan
# variabel = .split()
# variabel = reversed(variabel)
# variabel = <spasi>.join(variabel)
print("hasil:", 1000)
hasil = nama.split()
hasil = reversed(hasil)
hasil = " ".join(hasil)
print("hasil:", hasil)


print("split nama jadi list -> balik pakai .reverse() -> join dgn 1 spasi")
# info: method .reverse() akan merubah (mutate) variabel itu sendiri
# variabel = .split()
# .reverse()
# variabel = <spasi>.join(variabel)
print("hasil:", 1000)
hasil = nama.split()
hasil.reverse()
hasil = " ".join(hasil)
print("hasil:", hasil)

print("")
print(
    "split nama jadi list huruf pakai list() -> balik pakai .reverse() -> join -> split -> join dgn 1 spasi"
)
# variabel = list(<string>)
# variabel.reverse()
# variabel = <separator>.join(variabel)
# variabel = variabel.split()
# variabel = <separator>.join(variabel)
print("hasil:", 1000)
hasil = list(nama)
hasil.reverse()
hasil = "".join(hasil)
hasil = hasil.split()
hasil = " ".join(hasil)
print("hasil:", hasil)
