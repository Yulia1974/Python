def season(moth):
    if month == 12 or month < 3:
        return "Зима"
    elif month == 3 or month < 6:
        return "Весна"
    elif month == 6 or month < 9:
        return "Лето"
    elif month == 9 or month < 11:
        return "Осень"
    else:
        return "нет такого месяца"


month = input("Введите месяц(число):")

while True:
    if not month.isdigit():
        print("Ошибка ввода!")
        print("Используйте только целые числа.")
        month = input("Введите месяц(число):")
        continue
    else:
        break

month = int(month)
while True:
    if month == 0:
        print("Такого месяца несуществует")
        print("Используйте только целые числа.")
        month = input("Введите месяц(число):")
        continue
    else:
        break

month = int(month)

answer = season(month)
print(answer)
