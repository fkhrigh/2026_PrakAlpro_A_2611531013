# Buat file dengan nama nested_for2_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_1013 = int(input("masukkan nilai batas: "))
for i in range(1, batas_1013 + 1): 
    for j in range (1, batas_1013 + 1 ):
        print("*", end="")
    print() # Pindah ke baris berikutnya