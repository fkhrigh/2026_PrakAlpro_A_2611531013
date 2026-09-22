umur = int(input("Input umur anda: "))
sim = input("Apakah Anda SUdah Punya Sim C (y/t): ")

if umur >= 17 and sim == 'y':
        print("Anda Sudah dewasa dan boleh bawa motor")

if umur >= 17 and sim != 'y':
        print("Anda Sudah dewasa tetapi tidak boleh bawa motor")


if umur < 17 and sim == 'y':
        print("Anda Belum Cukup Umur punya SIM")


if umur < 17 and sim != 'y':
        print("Anda Belum Cukup Umur bawa motor")




