kalimat = input("Kalimat: ")

clean = kalimat.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")