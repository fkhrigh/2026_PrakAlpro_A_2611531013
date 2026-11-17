attempt_1013 = 1
MAX_ATTEMPS_1013 = 3
correct_pin_1013 = "1234"
pin_1013 = input("Enter PIN: ")


while pin_1013 != correct_pin_1013 and attempt_1013 < MAX_ATTEMPS_1013:
    print("Incorrect PIN.")
    pin_1013 = input("Enter PIN: ")
    attempt_1013 += 1

if pin_1013 == correct_pin_1013:
    print("Access granted")
else:
    print("Account locked")