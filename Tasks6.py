# Задача №39.
# Даны два списка чисел. Требуется вывести те элементы первого списка (в том порядке, в каком они идут в первом
# списке), которых нет во втором списке. Пользователь вводит число N - количество элементов в первом списке, \
# затем N чисел - элементы списка. Затем число M - количество элементов во втором списке. Затем элементы второго 
# списка
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

# # ВАРИАНТ ЕВГЕНИИ
# import random
# nums1 = [random.randint(1,15) for _ in range(random.randint(5,10))]
# nums2 = [random.randint(1,15) for _ in range(random.randint(5,10))]

# result = []
# for num_1 in nums1:
#     unique = True
#     for num_2 in nums2:
#         if num_1 == num_2:
#             unique = False
#             break

#     if unique:
#         result.append(num_1)   
# print(f'{nums1} - {nums2} -> {result}')         


# ВАРИАНТ 
# import random
# # создаем два списка случайных чисел
# list_1 = [random.randint(1, 20) for _ in range(int(input('Введите размер 1 списка: ')))]
# list_2 = [random.randint(1, 20) for _ in range(int(input('Введите размер 2 списка: ')))]

# print(list_1)
# print(list_2)
# # создаем новый список
# final_list = []
# # заполняем новый список с том же порядке ,что и первый, но без повторения второго списка
# for item in list_1:
#     # если элемент входит в наш список, то не записываем
#     if not item in list_2:
#         # если входит в список , то записываем
#         final_list.append(item)

# print(final_list)


#??????
# import random
# list_set = list()
# n = int(input('Введите число элементов в списке N: '))
# list_n = [random.randint(0,15) for i in range(n)]
# print(list_n)
# m = int(input('Введите число элементов в списке M: '))
# list_m = [random.randint(0,15) for i in range(m)]
# print(list_m)
# print(len(set([random.randint(0,15) for i in range(n)]) and set([random.randint(0,15) for i in range(m)])))




# Задача №41.
# Дан список, состоящий из целых чисел. Напишите программу, которая в данном списке определит количество элементов, 
# у которых два соседних и, при  этом, оба соседних элемента меньше данного. Сначала вводится число N — количество
# элементов в списке. Далее записаны N чисел — элементы списка. Список состоит из целых чисел.
# Ввод: Ввод:
# 5 5
# 1 2 3 4 5 1 5 1 5 1
# Вывод: Вывод:
# 0 2
# (каждое число вводится с новой строки)

# # ВАРИАНТ КИРИЛЛ
# import random
# my_list = [random.randint(0,100) for _ in range(10)]
# for i in range(50):
#     print(my_list[(i - 1) % len(my_list)] ,my_list[i%len(my_list)], my_list[(i + 1)%len(my_list)])

# # ВАРИАНТ САВЕЛИЙ ЧЕРЕЗ ФУНКЦИЮ
# from random import randint
# def circ(a, mn, mx):
#     return a % mx + mn
# N = 7
# list_1 = [randint(1, 15) for e in range(N)]
# print(list_1)
# counts = 0
# for e in range(len(list_1)):
#     if list_1[circ(e - 1), 0, N] < list_1[e] > list_1[circ(e + 1, 0, N)]:
#         counts +=1
#         # print(e)
# print(counts)        
    
# # ВАРИАНТ НАДЕЖДЫ
# import random
# list_1 = [random.randint(1,20) for _ in range(int(input('Введите размер списка: ')))]
# print(list_1)

# count = 0
# for i in range(1, len(list_1) - 1):
#     if list_1[i - 1] < list_1[i] > list_1[i + 1]:
#         count += 1
# print(f'Количество элементов = {count}')        





# Задача №45.
# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но 
# исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите
# все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное 
# число k, не превосходящее 105 . Программа должна вывести все пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена 
# только один раз (перестановка чисел новую пару не дает).
# Ввод: Вывод:
# 300 220 284

# # ВАРИАНТ ЕВГЕНИИ
# def sum_del(p):
#     summa = 0
#     for e in range(1, p // 2 + 1):
#         if p % e == 0:
#             summa += e
#     return summa
# k = 300
# for n in range(1, k):
#     m = sum_del(n)
#     if n < m <= k and n == sum_del(m):
#         print(n,m)        

# # ВАРИАНТ СТОУНА 
# def deviders(number: int) -> int:
#     list_dev = []
#     for div in range(1, number//2 + 1):
#         if not number % div:
#             list_dev.append(div)
#     return sum(list_dev)


# unique_list = []
# for num in range(10000):
#     if deviders(deviders(num)) == num and num != deviders(num):
#         if not ((num, deviders(num))) in unique_list:
#             unique_list.append((deviders(num), num))
#             print(num, deviders(num))


# Задача №43.
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые  два элемента, 
# равные друг другу образуют одну пару, которую необходимо посчитать. Вводится список чисел. Все числа списка находятся 
# на разных  строках.
# Ввод: Вывод:
# 1 2 3 2 3 2
