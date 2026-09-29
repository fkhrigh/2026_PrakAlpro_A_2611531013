tinggi_1013 = int(input("Masukkan tinggi segitiga: "))

for i in range(1, tinggi_1013 + 1):
    print(" " * (tinggi_1013 - i), end="")  # cetak spasi
    for j in range(1,i + 1):
        print("*", end=" ")
    print()  # pindah ke baris berikutnya