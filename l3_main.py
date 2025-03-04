print("Введите имя, по которому к Вам можно обратиться:")
name = str(input())

print("Добрый день,", name, "! Введите Ваш возраст, и я посчитаю, сколько Вам осталось до пенсии в годах:")
age = int(input())

pensionable_age = 65
if age < pensionable_age:
    print("Вам до пенсии осталось:", pensionable_age - age, "лет.")
else:
    print("Вы уже достигли пенсионного возраста.")