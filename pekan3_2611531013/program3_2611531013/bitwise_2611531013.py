# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angkal_1234
# Program ini menggunakan fungsi input()

print("\n===================================")
print("3. OPERATOR BITWISE")
print("===================================") 

angka1_1013 = int(input("Masukkan angka bitwise-1: "))
angka2_1013 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_1013, "| biner =", bin(angka1_1013))
print("angka2 =", angka2_1013, "| biner =", bin(angka2_1013))

#Bitwise AND
hasil_1013 = angka1_1013 & angka2_1013
print("\nBitwise AND (&)")
print(angka1_1013, "&", angka2_1013, "=", hasil_1013)
print("Biner hasil =", bin(hasil_1013))
print("Biner hasil (8 bit) =", format(hasil_1013, "08b"))

# Bitwise OR
hasil_1013 = angka1_1013 | angka2_1013
print("\nBitwise OR (|)")
print(angka1_1013, "|", angka2_1013, "=", hasil_1013)
print("Biner hasil =", bin(hasil_1013))
print("Biner hasil (8 bit) =", format(hasil_1013, "08b"))

# Bitwise XOR
hasil_1013 = angka1_1013 ^ angka2_1013
print("\nBitwise XOR (^)")
print(angka1_1013, "^", angka2_1013, "=", hasil_1013)
print("Biner hasil", bin(hasil_1013))
print("Biner hasil (8 bit)", format(hasil_1013, "08b"))

# Bitwise NOT
hasil_1013 = ~angka1_1013
print("\nBitwise NOT (~)")
print("~", angka1_1013, "=", hasil_1013)
print("Biner hasil =", bin(hasil_1013))
print("Biner hasil (8 bit) =", format(hasil_1013, "08b"))

# Bitwise geser kiri
jumlah_geser_1013 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_1013 = angka1_1013 << jumlah_geser_1013
print("\nBitwise geser kiri (<<)")
print(angka1_1013, "<<", jumlah_geser_1013, "=", hasil_1013)
print("Biner hasil =", bin(hasil_1013))
print("Biner hasil (8 bit) =", format(hasil_1013, "08b"))

# Bitwise geser kanan
hasil_1013 = angka1_1013 >> jumlah_geser_1013
print("\nBitwise geser kanan (>>)")
print(angka1_1013, ">>", jumlah_geser_1013, "=", hasil_1013)
print("Biner hasil =", bin(hasil_1013))
print("Biner hasil (8 bit) =", format (hasil_1013, "08b"))