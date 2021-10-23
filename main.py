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


#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
number = input("Введите число n: ")
number_1 = int(number)
number_2 = number + number
number_2 = int(number_2)
number_3 = number + number + number
number_3 = int(number_3)
sum_1 = number_1 + number_2 + number_3
sum = f"Сумма чисел в формате n + nn + nnn равна: {number_1} + {number_2} + {number_3} = {sum_1}"
print(sum)


# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
whole_number = int(input("Введите целое положительное число: "))
z = 0
while whole_number > 10:
    result = whole_number % 10
    if result > z:
        z = result
    whole_number //= 10
print(z)












