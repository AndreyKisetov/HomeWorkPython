# 1. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.​

# b = [1, 1, 2, 3, 3, 4, 5]
# a = list(filter((lambda i: b.count(i) == 1), b))
# print(a)


# 2. Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

# a = [3, 5, 10.01]
# b = list(map(lambda i: round((i+0.0)%1, 2), a))
# a = max(b)-min(b)
# print(a)


# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# n = int(input('Введите число для преобразования: '))
# n = list(map(lambda i: n//(2**abs(i))%2, [i for i in range(-7, 1)]))
# print(*n)


# 4. Реализуйте алгоритм перемешивания списка.

# import random

# a = [1, 33, 5, 6]
# b = list(map(lambda i: a.pop(random.randint(0, (len(a)-1))), [i for i in a]))
# print("Перемешенный список:", b)
