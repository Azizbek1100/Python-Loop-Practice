import random

sirli_son = random.randint(1, 10)  # Kompyuter 1 dan 10 gacha son o‘ylaydi
urinish = 1

while urinish <= 3:
    taxmin = int(input(f"{urinish}-urinish: Sonni kiriting: "))
    
    if taxmin == sirli_son:
        print("Topdingiz! ")
        break
    else:
        print("Noto‘g‘ri. Yana urinib ko‘ring.")
    
    urinish += 1

else:
    print("Urinishlar tugadi. Kompyuter o‘ylagan son:", sirli_son)
