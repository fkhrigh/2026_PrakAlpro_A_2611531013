# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("==================================")
print("1. OPERATOR KEANGGOTAAN")
print("==================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_1013 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_1013 = [int(angka.strip()) for angka in input_data_1013.split(",")]

nilai_dicari_1013 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_1013 = nilai_dicari_1013 in data_1013
print("\nOperator keanggotaan IN")
print(nilai_dicari_1013, "in", data_1013, "=", hasil_1013)

# Operator not in
hasil nilai_dicari not in data_1013
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_1013, "not in", data_1013, "=", hasil_1013)

print("\n=======")
print("2. OPERATOR IDENTITAS")
print("=======

#objek1 menggunakan list dari input pengguna
objek1 = data

# objek2 merujuk pada objek yang sama dengan objek1
objek1 objek2

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3 data.copy()
print("objek1 =", objek1)
print("objek2 =", objek2)
print("objek3 =", objek3)

# Operator is
hasil objek1 is objek2
print("\nOperator identitas IS")
print("objek1 is objek2", hasil_1013)

# Operator is not
hasil objek1 is not objek3
print("\nOperator identitas IS NOT")
print("objeki is not objek3 =", hasil_1013)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3", objek1 is objek3)
print("objek1 = objek3", objek1== objek3)