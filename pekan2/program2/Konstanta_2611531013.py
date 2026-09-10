<<<<<<< HEAD
#Program ini menggunakan konstanta untuk menghitung luas lingkaran
#Nama variabel ditambah 4 digit nim terakhir contoh: jari_1234

from typing import Final
PI: Final = 3.14

print("pi: %f" % (PI))

jari_1013 = float(input('Masukkan nilai jari-jari: '))
luas_1013 = PI * jari_1013 * jari_1013

=======
#Program ini menggunakan konstanta untuk menghitung luas lingkaran
#Nama variabel ditambah 4 digit nim terakhir contoh: jari_1234

from typing import Final
PI: Final = 3.14

print("pi: %f" % (PI))

jari_1013 = float(input('Masukkan nilai jari-jari: '))
luas_1013 = PI * jari_1013 * jari_1013

>>>>>>> d6afa4043101782e980e2489c7e034d529665c13
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_1013, luas_1013))