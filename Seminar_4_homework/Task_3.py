# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


def is_int(value):  
    # Проверка введенного значения на целое число
    try:
        int(value)
        return True
    except ValueError:
        return False

string = input('Задайте последовательность цифр: ')

while not is_int(string) or len(string) <= 1:  # Проверка условий для введенного значения
    if not is_int(string):
        print('Не вся последовательность из цифр')
        string = input('Задайте последовательность цифр: ')
        continue
    elif len(string) <= 1:
        print('Длина последовательности не может быть равна 0 или 1, нет смысла в задаче')
        string = input('Задайте последовательность цифр: ')

print(list(map(int, (filter(lambda x: string.count(x) < 2, string)))))
