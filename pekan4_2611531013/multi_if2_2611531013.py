# Buat file dengan nama multi_if2_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: total_belanja_1234
# Program ini menggunakan fungsi input()
# Program Menghitung Diskon Belanja

# Input dari user
total_belanja_1013 = float(input("Masukkan total belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_1013 = input("Apakah Anda member? (y/t): ").strip().lower()
is_member_1013 = input_member_1013 in ["y", "ya"]

# Input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_1013 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_1013 = input_promo_1013 in ["y", "ya"]

total_diskon_persen_1013 = 0

# Multi-IF terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_1013 > 1000000:
    total_diskon_persen_1013 + 10 # Diskon belanja besar

if is_member_1013:
    total_diskon_persen_1013 += 5 # Diskon member

if kode_promo_valid_1013:
    total_diskon_persen_1013 += 15 # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_1013 = total_belanja_1013*(total_diskon_persen_1013 / 100)
total_bayar_1013 = total_belanja_1013 - nominal_diskon_1013

# Output hasil
print("\n--- Rincian Pembayaran ---")
print (f"Total Diskon {total_diskon_persen_1013}% (Rp (nominal_diskon:,.0f))")
print(f"Total Bayar : Rp {total_bayar_1013:,.0f}")

print(f"Total diskon yang Anda dapatkan: {total_diskon_persen_1013}%")
# Output: Total diskon yang Anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid