# Lab_3_1.py
# Хімчинський Орест
# Лабораторна робота No 3.1
# Розгалуження, задане формулою: функція однієї змінної. #15
x = int(input('Введіть х'))  # вхідний параметр
import math

result = None
# спосіб 1: розгалуження в скороченій формі
if x < 4:
    result = 5 * x ** 8 + x ** 6 - x ** 2 + 3
if 4 <= x < 7:
    result = 1 / (math.atan(math.fabs((x + 3) / 2))) + 7 * x
if x >= 7:
    result = math.log10(2 * x + math.e ** (5 * x + 5))

y = x ** 3 + 2 + result  # результат обчислення виразу

print(f'Перший спосіб:{y}')

# спосіб 2: розгалуження в повній формі

if x < 4:
    result = 5 * x ** 8 + x ** 6 - x ** 2 + 3
elif 4 <= x < 7:
    result = 1 / (math.atan(math.fabs((x + 3) / 2))) + 7 * x
else:
    result = math.log10(2 * x + math.e ** (5 * x + 5))

y = x ** 3 + 2 + result  # результат обчислення виразу

print(f'Другий спосіб:{y}')
