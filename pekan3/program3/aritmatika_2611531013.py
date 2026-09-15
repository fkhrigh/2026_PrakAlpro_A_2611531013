# Buat file dengan nama aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel di tambah 4 digit nim terakhir contoh : angka1_1234
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan di konversi menjadi tipe data integer

angka1_1013 = int(input("input angka-1: "))
angka2_1013 = int(input("input angka-2: "))

# Penjumlahan 
hasil_1013 = angka1_1013 + angka2_1013
print("\nOperator Penjumlahan")
print("Hasil =", hasil_1013)

# Pengurangan 
hasil_1013 = angka1_1013 - angka2_1013
print("\nOperator Pengurangan")
print("Hasil =", hasil_1013)

# Perkalian
hasil_1013 = angka1_1013 * angka2_1013
print("\nOperator Perkalian")
print("Hasil =", hasil_1013)

# Pembagian, Pembagian bilangan bulat, dan sisa bagi
if angka2_1013 != 0:
    hasil_1013 = angka1_1013 / angka2_1013
    print("\nOperator Pembagian")
    print("Hasil", hasil_1013)

    hasil_1013 = angka1_1013 // angka2_1013
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_1013)

    hasil_1013 = angka1_1013 % angka2_1013
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_1013)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_1013 = angka1_1013 ** angka2_1013
print("\nOperator Pangkat")
print("Hasil =", hasil_1013)

