# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

def is_int(value):  
    # Проверка введенного значения на целое число
    try:
        int(value)
        return True
    except ValueError:
        return False


N = input('Введите длину списка: ')

while not is_int(N) or int(N) < 0 or int(N) == 0 or int(N) == 1:  # Проверка условий для введенного значения
    if not is_int(N):
        print('Введено не целое число')
        N = input('Введите целое число: ')
        continue
    elif int(N) < 0:
        print('Длина списка не может быть отрицательным числом')
        N = input('Введите целое положительное число больше единицы: ')
    elif int(N) == 0:
        print('При пустом списке нет элементов стоящих на нечётной позиции')
        N = input('Введите целое положительное число больше единицы: ')
    elif int(N) == 1:
        print('При одном элементе списка нет элементов стоящих на нечётной позиции')
        N = input('Введите целое положительное число больше единицы: ')

N = int(N)

import random

# list_random = []
# for i in range(N):
#     list_random.append(random.randint(-N, N))
print('Случайно сгенерированный список:')

list_random = [random.randint(-N, N) for i in range(N)]

print(list_random)

# sum = 0
# for i in range(1, len(list_random), 2):
#     sum += list_random[i]

s = sum(list_random[1::2])

print(f'Сумма элементов списка, стоящих на нечётной позиции = {s}')


