print("=== SISTEM REGISTRASI PRAKTIKUM ALPRO 2026 ===")
nama_1013 = input("Masukkan Nama Mahasiswa : ")
jenis_kelamin_1013 = input("Masukkan Jenis Kelamin (L/P) : ")
umur_1013 = int(input("Masukkan Umur           : "))
skor_tes_1013 = float(input("Masukkan Skor Tes Awal  : "))
alamat_1013 = """
  Koto Panjang,
  Kecamatan Pauh,
  Kota Padang
"""
id_token_1013 = 100+3j

print("\n=== DATA PRAKTIKUM & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa :", nama_1013, "| Tipe:", type(nama_1013))
print("Jenis Kelamin  :", jenis_kelamin_1013, "| Tipe:", type(jenis_kelamin_1013))
print("Alamat Domisili:", alamat_1013, "| Tipe:", type(alamat_1013))
print("Umur           :", umur_1013, "tahun | Tipe:", type(umur_1013))
print("Skor Tes Awal  :", skor_tes_1013, "| Tipe:", type(skor_tes_1013))
print("ID Token Sinyal:", id_token_1013, "| Tipe:", type(id_token_1013))

from typing import Final
batas_1013: Final = 75.0

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai:", batas_1013)
hasil_1013 = skor_tes_1013 >= batas_1013
print("Apakah Dinyatakan Lulus?:", hasil_1013, "| Tipe:", type(hasil_1013))