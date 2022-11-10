# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.


def is_int(value):  
    # Проверка введенного значения на целое число
    try:
        int(value)
        return True
    except ValueError:
        return False

N = input('Введите длину списка: ')

while not is_int(N) or int(N) < 0 or int(N) < 2:  # Проверка условий для введенного значения
    if not is_int(N):
        print('Введено не целое число')
        N = input('Введите целое число: ')
        continue
    elif int(N) < 0:
        print('Длина списка не может быть отрицательным числом')
        N = input('Введите целое положительное число больше единицы: ')
    elif int(N) < 2:
        print('При списке длиной меньше чем два нет элементов для выполнения условия задачи')
        N = input('Введите целое положительное число больше единицы: ')

N = int(N)

import random

# list_random = []
# for i in range(N):
#     list_random.append(round(random.(0, 10), 2))

list_random = [random.uniform(0, 10) for i in range(N)]

print('Случайно сгенерированный список:')
print(list_random)

# for i in range(N):
#     list_random[i] = round(list_random[i] - int(list_random[i]), 2)

list_random = list(map(lambda i: i - int(i), list_random))

list_random.sort()
# print(list_random)

print(f'Разница между максимальным и минимальным значением дробной части элементов = {list_random[-1] - list_random[0]}')