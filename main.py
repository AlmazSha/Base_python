# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран
peremennaya_1 = 5
peremennaya_2 = 28
print("Первая переменная: ", peremennaya_1)
print("Вторая переменная: ", peremennaya_2)

peremennaya_3 = int(input("Введите число: "))
peremennaya_4 = int(input("Введите ещё число: "))
stroke_1 = input("Введите любое предложение: ")
peremennaya_3 = str(peremennaya_3)
peremennaya_4 = str(peremennaya_4)
print("Вы ввели: ", peremennaya_3,"; ", peremennaya_4,"; ", stroke_1)


#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
sec = int(input("Введите время в секундах: "))
sec = sec % (24 * 3600)
hours = sec // 3600
sec %= 3600
minute = sec // 60
sec %= 60
user_time = f"Время в формате чч:мм:сс: {hours:02}:{minute:02}:{sec:02}"
print(user_time)















