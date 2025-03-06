name = input("Введите имя, по которому к Вам можно обратиться: ")

print(f"Добрый день, {name}!")
age = int(input("Введите Ваш возраст, и я посчитаю, сколько лет Вам осталось до пенсии: "))

pensionable_age = 65
if age < pensionable_age:
    print(f"Вам до пенсии осталось: {pensionable_age - age} лет.")
else:
    print("Вы уже достигли пенсионного возраста.")