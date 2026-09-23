# ==============================================================================
# PROGRAM: SISTEM TRANSAKSI TOKO
# MODUL: OPERATOR PYTHON
# ==============================================================================

# --- 1. MENGELUARKAN HEADER & MENERIMA MASUKAN (INPUT) DENGAN TYPE CASTING ---
print("=== SISTEM TRANSAKSI TOKO ===")
nama_1013 = input("Masukkan Nama Pelanggan    : ")
status_1013 = input("Masukkan Status Pelanggan (member/nonmember) : ").strip().lower()
total_1013 = int(input("Masukkan Total Belanja     : "))
jumlah_1013 = int(input("Masukkan Jumlah Barang     : "))
kode_1013 = input("Masukkan Kode Promo        : ").strip().upper()

# --- 2. MENAMPILKAN RINGKASAN DATA MASUKAN ---
print("\n=== DATA TRANSAKSI ===")
print("Nama Pelanggan   :", nama_1013)
print("Status Pelanggan :", status_1013)
print("Total Belanja    : Rp", total_1013)
print("Jumlah Barang    :", jumlah_1013)
print("Kode Promo       :", kode_1013)

# --- 3. DEKLARASI KOLEKSI DATA (LIST KODE PROMO) ---
daftar_kode_1013 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]

# --- 4. EVALUASI KONDISI DENGAN OPERATOR PERBANDINGAN, LOGIKA & KEANGGOTAAN ---
print("\n=== Hasil Validasi ===")
print("Belanja >= Rp200000 :", total_1013 >= 200000)
print("Jumlah Barang >= 3  :", jumlah_1013 >= 3)
print("Status Member       :", status_1013 == "member")
print("Kode Promo Tersedia :", kode_1013 in daftar_kode_1013)
print("Kode Promo Expired  :", kode_1013 not in daftar_kode_1013)
print("Mendapatkan Diskon  :", (status_1013 == "member") and ((total_1013 >= 200000) or (jumlah_1013 >= 3)))
print("Mendapatkan Promo   :", kode_1013 in daftar_kode_1013 and not (status_1013 == "nonmember"))

# --- 5. STRUKTUR PERCABANGAN UNTUK PENENTUAN DISKON ---
if kode_1013 == daftar_kode_1013[0]:
    diskon_1013 = total_1013 / 10
elif kode_1013 == daftar_kode_1013[1]:
    diskon_1013 = total_1013 / 20
else:
    diskon_1013 = 15000

# --- 6. OPERASI ARITMETIKA & PENUGASAN (ASSIGNMENT) ---
bayar_1013 = total_1013 - diskon_1013

sisa_barang_1013 = jumlah_1013 % 3
bayar_akhir_1013 = bayar_1013
bayar_akhir_1013 += 0

# --- 7. MENAMPILKAN HASIL PERHITUNGAN TRANSAKSI ---
print("\n=== HASIL PERHITUNGAN ===")
print("Diskon                 : Rp", diskon_1013)
print("Total Pembayaran       : Rp", bayar_1013)
print("Rata-Rata Harga Barang : Rp", bayar_1013 / jumlah_1013)
print("Sisa Pembagian Barang  :", sisa_barang_1013)
print("Total Akhir            : Rp", bayar_akhir_1013)

# --- 8. EVALUASI OPERATOR IDENTITAS (IS & IS NOT) ---
cek_tipe_1013 = type(bayar_1013) is float
cek_identitas_1013 = total_1013 is not bayar_1013

# --- 9. MENAMPILKAN VALIDASI HAK AKSES PELANGGAN ---
print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses       : ")
print("Member Access        : ", status_1013 == "member")
print("Promo Access         : ", kode_1013 in daftar_kode_1013)
print("Free Shipping Access : ")
print("Cek Tipe Float       : ", cek_tipe_1013)
print("Cek Identitas        : ", cek_identitas_1013)

# --- 10. INISIALISASI BITWISE FLAG (KODE STATUS 4-BIT) ---
bit_member_1013 = 0b0000
bit_total_1013 = 0b0000
bit_jumlah_1013 = 0b0000
bit_kode_1013 = 0b0000

# Penentuan aktifasi bit berdasarkan kondisi
if status_1013 == "member":
    bit_member_1013 = 0b0001
if total_1013 >= 200000:
    bit_total_1013 = 0b0010
if jumlah_1013 >= 3:
    bit_jumlah_1013 = 0b0100
if kode_1013 in daftar_kode_1013:
    bit_kode_1013 = 0b1000

# Penggabungan bit flag dengan operator Bitwise OR (|)
bit_status_1013 = bit_member_1013 | bit_total_1013 | bit_jumlah_1013 | bit_kode_1013
bit_referensi_1013 = 0b1111

# --- 11. MANIPULASI & PEMERIKSAAN DATA BITWISE (AND, XOR, LEFT SHIFT) ---
print("\n=== OPERASI BITWISE ===")
print("\n=== Kode Status Transaksi ===")
print(format(bit_member_1013, "04b"), " | ", format(bit_total_1013, "04b"), " | ", format(bit_jumlah_1013, "04b"), " | ", format(bit_kode_1013, "04b"))
print("Kode Biner   :", format(bit_status_1013, "04b"))
print("Kode Desimal :", bit_status_1013)

# Pengecekan bit individual dengan Bitwise AND (&)
print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print("1111 & 0001")
print("Kode Biner   :", format(bit_status_1013 & bit_member_1013, "04b"))
print("Kode Desimal :", bit_status_1013 & bit_member_1013)

print("\nCek Total")
print("1111 & 0010")
print("Kode Biner   :", format(bit_status_1013 & bit_total_1013, "04b"))
print("Kode Desimal :", bit_status_1013 & bit_total_1013)

print("\nCek Jumlah")
print("1111 & 0100")
print("Kode Biner   :", format(bit_status_1013 & bit_jumlah_1013, "04b"))
print("Kode Desimal :", bit_status_1013 & bit_jumlah_1013)

print("\nCek Promo")
print("1111 & 1000")
print("Kode Biner   :", format(bit_status_1013 & bit_kode_1013, "04b"))
print("Kode Desimal :", bit_status_1013 & bit_kode_1013)

# Perbandingan bit status dengan Bitwise XOR (^)
print("\n=== Perbandingan Status ===")
print("Kode Transaksi :", format(bit_status_1013, "04b"))
print("Kode Referensi :", format(bit_referensi_1013, "04b"))
print(format(bit_status_1013, "04b"), " ^ ", format(bit_referensi_1013, "04b"))
print("Hasil Biner    :", format(bit_status_1013 ^ bit_referensi_1013, "04b"))
print("Hasil Desimal  :", bit_status_1013 ^ bit_referensi_1013)

# Pergeseran bit dengan Bitwise Left Shift (<<)
bin_shift_1013 = bit_status_1013 << 1
print("\n=== Shift ===")
print(format(bit_status_1013, "04b"), " << ", 1)
print("Hasil Biner    :", format(bin_shift_1013, "04b"))
print("Hasil Desimal  :", bin_shift_1013)

# --- 12. AKHIR PROGRAM ---
print("\n=== SELESAI ===")