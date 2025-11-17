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
print("replace spasi dgn '-':", nama.replace(" ", "-"))
print("replace IBNU dgn 'ibin':", nama.replace("IBNU", "ibin"))

print("")
print("split nama jadi list:", nama.split())
print("join list dgn 1 spasi:", " ".join(nama.split()))

print("")
print(
    "balik kata (pakai reversed()):",
    " ".join(reversed(nama.split())),
)

gabung = nama.split()
gabung.reverse()
print("balik kata (pakai .reverse):", " ".join(gabung))


print("")
kebalik = list(nama)
kebalik.reverse()
kebalik = "".join(kebalik)
kebalik = kebalik.split()
kebalik = " ".join(kebalik)
print("balik huruf (pakai list()):", kebalik)
