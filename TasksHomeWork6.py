# Задача 30: 
# Заполните список элементами арифметической прогрессии. Её первый элемент, разность и количество  элементов нужно 
# ввести с клавиатуры. Формула для  получения n-го члена прогрессии: an  = a1  + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# a1, d, n = map(int, input().split())
# # a1 = int(input('Введите первое число арифметической прогресии a1: '))
# # d = int(input('Введите шаг арифметической прогресии d: '))
# # n = int(input('Введите количество членов арифметической прогресии n: '))
# an= []
# for item in range(n):
#     an.append(a1 + item*2)
# print(an)



# Задача 32: 
# Определить индексы элементов списка, значения которых принадлежат заданному диапазону (т.е. не меньше 
# заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
import random
list_1 = [random.randint(-5, 20) for _ in range(20)]
print(list_1)
list_new = []
min_n = int(input('Задайте минимум: '))
max_n = int(input('Задайте максимум: '))
if max_n >= min_n:
    for item in range(len(list_1)):
        if max_n >= list_1[item] and min_n <= list_1[item]:
           list_new.append(item)
    print(item)
