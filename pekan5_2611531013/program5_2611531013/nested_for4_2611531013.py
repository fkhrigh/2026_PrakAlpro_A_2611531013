# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_1013 = int(input("Masukkan tinggi pola(bilangan genap, misal 10): "))

if tinggi_1013 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_1013 = tinggi_1013
    c_1013 = a_1013
    lebar_1013 = (2 * tinggi_1013) - 2

    for i_1013 in range(1, tinggi_1013 + 1): 
        b_1013 = c_1013 + 1

        for j_1013 in range (1, lebar_1013 + 1 ):

            # Baris atas dan bawah
            if i_1013 == 1 or i_1013 == tinggi_1013:
                if j_1013 == 1 or j_1013 == lebar_1013:
                    print("#", end=" ")
                else:
                    print("=", end=" ")

            # Baris isi
            else:
                if j_1013 == 1 or j_1013 == lebar_1013:
                    print("!", end="")
                else:
                    if j_1013 == c_1013:
                        print("<", end="")
                    elif j_1013 == b_1013:
                        print(">", end="")
                    elif j_1013 == (lebar_1013 - c_1013):
                        print("<", end="")
                    elif j_1013 == (lebar_1013 - c_1013 + 1):
                        print(">", end="")
                    elif j_1013 == (lebar_1013 - c_1013 + 1):
                        print(".", end="")
                    else:
                        print(" ", end="")

print()

# Logika asli Java 
a_1013 -= 2

if a_1013 <= 0:
    c_1013 = (-a_1013) + 2
else: 
    c_1013 = a_1013
                    