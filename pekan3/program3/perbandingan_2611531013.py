# Buat file dengan nama perbandingan_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_1013 = int(input("Input angka-1: "))
angka2_1013 = int(input("Input angka-2: "))

# Lebih besar dari
hasil_1013 = angka1_1013 > angka2_1013
print("\nOperator lebih besar dari")
print("angkal > angka2", hasil_1013)

# Lebih kecil dari
hasil_1013 = angka1_1013 < angka2_1013
print("\nOperator lebih kecil dari")
print("angka1 angka2", hasil_1013)

# Lebih besar dari atau sama dengan
hasil_1013 = angka1_1013 > angka2_1013
print("\nOperator lebih besar dari atau sama dengan")
print("angka1 >= angka2", hasil_1013)

# Lebih kecil dari atau sama dengan
hasil_1013 = angka1_1013 <= angka2_1013
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1 <= angka2", hasil_1013)

# Sama dengan
hasil_1013 = angka1_1013 == angka2_1013
print("\nOperator sama dengan")
print("angkal == angka2", hasil_1013)

# Tidak sama dengan
hasil_1013 = angka1_1013 != angka2_1013
print("\nOperator tidak sama dengan")
print("angka1 != angka2", hasil_1013)

# Tambahan: perbandingan berantai dalam Python
hasil_1013 = 0 < angka1_1013 < 100
print("\nPerbandingan berantai")
print("0 < angkal < 100 =", hasil_1013)

hasil_1013 = angka2_1013 < 100
print("< angka2 < 100", hasil_1013)