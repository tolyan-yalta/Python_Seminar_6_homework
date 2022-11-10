# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def is_int(value):  
    # Проверка введенного значения на целое число
    try:
        int(value)
        return True
    except ValueError:
        return False

k = input('Введите число k: ')

while not is_int(k) or int(k) < 2:  # Проверка условий для введенного значения
    if not is_int(k):
        print('Введено не целое число')
        k = input('Введите целое число: ')
        continue
    elif int(k) < 2:
        print('Число k должно быть >= 2 (по условию последовательности чисел Фибоначчи)')
        k = input('Введите целое положительное число больше единицы: ')

k = int(k)

list_positive = [0, 1]
# list_negative = []
for i in range(1, k):
    list_positive.append(list_positive[i] + list_positive[i - 1])
# for i in range(1, k + 1):
#     list_negative.insert(0, int((-1)**(-i + 1)*list_positive[i]))


list_negative = [int((-1)**(-i + 1) * list_positive[i])  for i in range(1, k + 1)]
list_negative.reverse()

print(list_negative + list_positive)

