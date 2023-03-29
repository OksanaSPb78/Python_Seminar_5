# # семинар 5 рекурсия
# # Задача №31. Решение в группах
# # Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an,
# # где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# # Требуется найти N-е число Фибоначчи
# # Input: 7
# # Output: 21
# # Задание необходимо решать через рекурсию

# def Fib(n):
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 0
#     return(Fib(n-1) + Fib(n-2))
# n = int(input('Введите число: '))
# print(Fib(n))


# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – 
# на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# import random
# list_1 = list()
# n = int(input('Введите число элементов в списке: '))
# n = range(n)
# count = 0
# for i in n:

#     i = random.randint(1,10)
#     list_1.append(i)
# print(list_1)
# min_1 = list_1[0]
# max_1 = list_1[0]
# for i in range(len(list_1)):
#     if min_1 > list_1[i]:
#         min_1 = list_1[i]
#     if max_1 < list_1[i]:
#         max_1 = list_1[i]
# print(f'{min_1} and {max_1}')  
# for i in range(len(list_1)):
#     if max_1 == list_1[i]:
#         list_1[i] = min_1
# print(list_1)

# ВАРИАНТ 2 через функции min и max

# mass = [1,2,3,4,5,5,4,3,2]
# mn = min(mass)
# mx = max(mass)
# print(mass)
# for e in range(len(mass)):
#     if mass[e] == mx:
#         mass[e] = mn
# print(mass)        



# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# # ВАРИАНТ 1
# n = int(input('Введите число: '))
# for i in range(2,(n//2)+ 1):
#     if n % i == 0:
#         print('Число составное')
#     else:
#         print('Число является простым ')

# #ВАРИАНТ 2  
# import math

# def is_simple(number: int)-> bool:
#     if number % 2 == 0:
#         return False
#     elif number in [1,2,3]:
#         return True
#     else:
#         for div in range(3, int(math.sqrt(number) + 1, 2)):
#             if number % div == 0:
#                 return False
#             return True
# number = int(input('Введите число N: '))        
# print(is_simple(number))
              



# # ЗАДАЧА:  УГАДАЙ ЧИСЛО
# # Загадать число от 0 до 1000. Дайте компьютеру отгадать его за 10 попытокю Условие (<) или (>)

# # вводим загаданное число
# number = int(input('Введите загаданное число: '))
# # верхняя граница предела
# max_limit = 1000 
# # нижняя граница предела
# min_limit = 0
# # число, которое угадывает комьютер (спрашивает)
# hidden = 500
# # hidden = (max_limit + min_limit)// 2
# while hidden != number:
#     print(f'Я думаю, что это число {hidden}')
#     # нужно дать подсказку (выбор) компьютеру < или > наше задуманное число
#     choice = input('Больше (>) или Меньше (<): ')
#     if choice == '<':
#        max_limit = hidden
#     else:
#       min_limit = hidden
#     hidden = (max_limit + min_limit)// 2

# print(f'Ты загадал число {hidden}')        




# Задача №37. Решение в группах
# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту 
# последовательность в обратном порядке. 
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3