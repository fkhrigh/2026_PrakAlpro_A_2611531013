pin = input("Enter PIN: ")
correct_pin = "1234"
attempt = 1
MAX_ATTEMPTS = 3

if pin == correct_pin:
    print("Access granted")
else:
     print("Incorrect Pin")

while pin != correct_pin and attempt < MAX_ATTEMPTS:
    pin = input("Enter PIN: ")
    attempt += 1

print("Account locked")
