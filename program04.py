from random import randint

secret_number = randint(1, 999)
attempts = 5
found = False

while attempts > 0:
    option = int(input(f"{attempts} urinish qolding — taxminingizni kiriting: "))
    attempts -= 1

    if option == secret_number:
        print("To‘g‘ri topdingiz! ")
        found = True
        break
    else:
        print("Noto‘g‘ri. Yana urinib ko‘ring.")

if not found:
    print("Topolmadingiz. Men o‘ylagan raqam:", secret_number)
