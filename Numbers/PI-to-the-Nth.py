from math import pi

# Get user input
digits = int(input("How many digits of PI would you like? "))

PI = str(pi)
PI_Length = []
digit_limit = 15
if digit_limit < digits:
    print("Unable to process")
else:
    for places in range(digits + 1):
        PI_Length.append(str(PI[places]))
    print("".join(PI_Length))

