# --- HEADER DAN INPUT PROGRAM ---
print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
# Meminta masukan skala N dari pengguna
n_1013 = int(input("Masukkan ukuran skala jam pasir (N): "))

# --- PERULANGAN UTAMA MATRIKS 2D ---
# Loop baris i (bergerak dari atas ke bawah)
for i_1013 in range(1, ((n_1013 * 2) + 4)):
    # Loop kolom j (bergerak dari kiri ke kanan)
    for j_1013 in range(1, ((n_1013 * 4) + 8)):
        
        # --- BINGKAI: PENGECEKAN 4 CORNER / SUDUT TERLUAR ---
        if ((i_1013 == 1 and j_1013 == 1) or (i_1013 == 1 and j_1013 == (n_1013 * 4) + 7) or (i_1013 == (n_1013 * 2) + 3 and j_1013 == (n_1013 * 4) + 7) or (i_1013 == (n_1013 * 2) + 3 and j_1013 == 1)):
            print("#", end="")
            
        else:
            # --- BINGKAI: ATAS, BAWAH, KIRI, DAN KANAN ---
            if (i_1013 == 1 or i_1013 == ((n_1013 * 2) + 3)):
               print("=", end="") # Garis horizontal pembatas atas dan bawah
            elif (j_1013 == 1 or j_1013 == ((n_1013 * 4) + 7)):
                print("|", end="") # Dinding vertikal pembatas kiri dan kanan
                
            else:
                # --- ELEMEN POROS KRISTAL TENGAH (<*>) ---
                if (j_1013 == ((n_1013 * 2) + 3)):
                    print("<", end="") # Karakter kiri poros
                elif (j_1013 == ((n_1013 * 2) + 5)):
                    print(">", end="") # Karakter kanan poros
                elif (j_1013 == ((n_1013 * 2) + 4)):
                    print("*", end="") # Karakter tengah poros
                elif (j_1013 == 2 or j_1013 == (n_1013 * 2) + 6):
                    print(" ", end="") # Spasi pemisah di dekat poros/bingkai
                    
                else:
                    # --- MENENTUKAN SKALA ANGKA AKTIF PER BARIS ---
                    if i_1013 - 1 <= n_1013:
                        baris_1013 = (n_1013 - (i_1013 - 2)) # Fase Atas: Nilai N mengecil ke 1
                    else:
                        baris_1013 = (i_1013 - 2) - n_1013    # Fase Bawah: Nilai 1 membesar ke N

                    # --- PENCETAKAN DERET ANGKA PALINDROM ---
                    # Sisi Kiri Poros: Deret angka menurun (misal: 4 3 2 1)
                    if (j_1013 % 2 == 1) and (((n_1013 * 2) + 3 - (baris_1013 * 2)) <= j_1013 < ((n_1013 * 2) + 3)):
                        print(((n_1013 * 2) + 3 - j_1013) // 2, end="")
                    # Sisi Kanan Poros: Deret angka menaik (misal: 1 2 3 4)
                    elif (j_1013 % 2 == 1) and (((n_1013 * 2) + 5) < j_1013 <= ((n_1013 * 2) + 5 + (baris_1013 * 2))):
                        print((j_1013 - ((n_1013 * 2) + 5)) // 2, end="")
                    # Padding Spasi Kosong di Luar Jangkauan Angka
                    else:
                        print(" ", end="")
                        
    # --- PINDAH KE BARIS BARU ---
    print()