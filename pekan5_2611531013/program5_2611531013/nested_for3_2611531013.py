# Buat file dengan nama nested_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_1013 = int(input("masukkan nilai batas: "))
for i in range(batas_1013 + 1): 
    for j in range (batas_1013 + 1 ):
        print(i+j, end=" ")
    print() # Pindah ke baris berikutnya