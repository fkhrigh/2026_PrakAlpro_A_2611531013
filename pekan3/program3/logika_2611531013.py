# Buat file dengan nama logika_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: al_1234
# Program ini menggunakan fungsi input()
# Program operator logika dalam Python

# Memamsukkan nilai Boolean 
# Input tidak peka terhadap huruf besar dan kecil 
a1_1013 = input("input nilai boolean-1 (true/false): "). strip().lower() == "true"
a2_1013 = input("input nilai boolean-2 (true/false): "). strip().lower() == "true"

print("\nA1 =", a1_1013)
print("A2 =", a2_1013)

# Konjungsi: bernilai True jika keduanya True 
hasil_1013 = a1_1013 and a2_1013
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_1013)

# Disjungsi: bernilai True jika salah satunya True
hasil_1013 =  a1_1013 or a2_1013
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_1013)

# Negasi A1: membalik nilai A1
hasil_1013 = not a1_1013
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_1013)

# Negasi A2: membalik nilai A2
hasil_1013 =  not a2_1013
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_1013)

# XOR: bernilai True jika kedua nilai berbeda
hasil_1013 = a1_1013 != a2_1013
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_1013)