# Name: Fakhri Al Ghifari Busra
# NIM: 2611531013
# Question 3

# Bagian A
text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

# Bagian B
text = "Algoritma dan Pemrograman"
count = 0
for char in text:
    if char.lower() in "aiueo":
        count += 1
print("Vowels:", count)

