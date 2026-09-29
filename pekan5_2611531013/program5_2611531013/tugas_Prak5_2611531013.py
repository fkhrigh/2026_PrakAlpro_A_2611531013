tinggi_1013 = int(input("Masukkan tinggi segitiga: "))

for i_1013 in range(1, tinggi_1013 + 1):
    print(" " * (tinggi_1013 - i_1013), end="")  # cetak spasi
    for j_1013 in range(1,i_1013 + 1):
        print("*", end=" ")
    print()  # Pindah ke baris berikutnya