from random import randint


basket = 0
spray = 20


while basket < 100 and spray > 0:
    mushrooms = randint(0, 100)
    if basket + mushrooms > 100:
        basket = 100
    else:
        basket += mushrooms
    spray -= 1
    print("Поиск грибов...")
    print(f"Найдено грибоы: {mushrooms}")
    print(f"Осталось места в корзине: {100 - basket}")
    print(f"Корзина: {basket}/100")
    print(f"Спрей: {spray}/20")
    print("")

print("")
if basket >= 100:
    print("Корзина полна!")
    print(f"Корзина:  {basket}/100")
    print(f"Спрей: {spray}/20")


elif spray < 1:
    print("Закончился спрей!")
    print(f"Корзина: {basket}/100")
    print(f"Спрей: {spray}/20")
