# Name: Fakhri Al Ghifari Busra
# NIM: 2611531013
# Question Bonus

kalimat = input("Kalimat: ")

clean = kalimat.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")