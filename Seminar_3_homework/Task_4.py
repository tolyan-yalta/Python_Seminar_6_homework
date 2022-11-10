# Напишите программу, которая будет преобразовывать десятичное число в двоичное
#  (не использовать функцию bin).


def is_int(value):  
    # Проверка введенного значения на целое число
    try:
        int(value)
        return True
    except ValueError:
        return False

N = input('Введите десятичное число: ')

while not is_int(N) or int(N) < 0 or int(N) == 0 or int(N) == 1:  # Проверка условий для введенного значения
    if not is_int(N):
        print('Введено не целое число')
        N = input('Введите целое число: ')
        continue
    elif int(N) < 0:
        print('Данное число отрицательное')
        N = input('Введите целое положительное число больше ноля: ')
    elif int(N) == 0:
        print('0 и в десятичной и в двоичной системе исчесления равен 0')
        N = input('Введите целое число больше ноля: ')

N = int(N)

result = []
while N != 0:
    result.append(N % 2)
    N = int(N / 2)

result.reverse()

print(''.join(map(str, result)))