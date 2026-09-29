# Buat file dengan nama nested_for1_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_1013 = int(input("masukkan nilai batas: "))
for line_1013 in range(1, batas_1013 + 1):
    for j in range (1, (-1 * line_1013 + batas_1013) + 1 ):
        print(".", end="")
    print(line_1013)