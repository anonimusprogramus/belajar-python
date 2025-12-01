spp = 3203000
ruler = "1________11________21________31________41________5"

# petunjuk:
# lihat screenshot
# ganti angka 1000 dgn variabel atau nilai yang tepat
# tambahkan modifier format sesuai instruksi
# output gunakan print() dan f""

print()
print("-" * 30)
print()
print(f"spp: {1000}")
# gunakan len()
print(f"panjang ruler: {1000} karakter")
print()
print("-" * 30)

print("\nformat spp dengan dua desimal")
# gunakan modifier .2f
print("hasil:", f"{1000}")

print("\nformat spp dengan underscore")
# gunakan modifier _
print("hasil:", f"{1000}")

print("\nformat spp dengan koma")
# gunakan modifier ,
print("hasil:", f"{1000}")

print("\nformat spp dengan koma dan desimal")
# gunakan modifier , dan .2f
print("hasil:", f"{1000}")

print()
print(ruler)
# gunakan modifier < dan karakter *
print(f"{'Rata kiri sampai 30'}")

print()
print(ruler)
# gunakan modifier > dan karakter *
print(f"{'Rata kanan sampai 50'}")

print()
print(ruler)
# gunakan modifier < dan >
print(f"{'Rata kiri sampai 30'}{'Rata kanan sampai 50'}")

print()
print(ruler)
# posisi rata kiri 30, rata kiri 30, rata kanan 15
print(f"{'Kopi susu gula aren'}{2}{30000}")
print(f"{'Kopi susu almond'}{1}{15000}")
