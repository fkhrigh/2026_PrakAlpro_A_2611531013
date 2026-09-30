# Buat file dengan nama nested_for3_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_1013 = int(input("masukkan nilai batas: "))
for i_1013 in range(batas_1013 + 1): 
    for j_1013 in range (batas_1013 + 1 ):
        print(i_1013+j_1013, end=" ")
    print() # Pindah ke baris berikutnya