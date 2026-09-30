# Buat file dengan nama perulangan_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input() 

ulang_1013 = int(input("Masukkan Jumlah perulangan: "))

jumlah_1013 = 0

for i_1013 in range(1, ulang_1013 + 1):
    print(i_1013, end="")
    jumlah_1013 = jumlah_1013 + i_1013

    if i_1013 < ulang_1013:
        print(" + ", end="")
    else:
        print(" + ", jumlah_1013, end="")
print()
print("jumlah =", jumlah_1013)