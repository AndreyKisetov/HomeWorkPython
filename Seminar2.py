# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

# real_number = input('Введите вещественное число: ')
# number = real_number.replace(',','.')
# list = []
# for symbol in number:
#     if'1234567890'.find(symbol) != -1:
#         list.append(int(symbol))
# print(f'{real_number} → {sum(list)}')

# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

# N = int(input('Введите число: '))
# a = []
# while 0 < N:
#     N -= 1
#     f = 1
#     for i in range(1, N+2):
#         f *= i
#     a.append(int(f))   
# A = a[::-1]
# print(A)

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ 
# и выведите на экран их сумму.

# n = int(input('Введите значение n: '))
# b = float(n)
# a = []
# while 0 < n:
#     n -= 1
#     f = 1
#     for i in range(1, n+2):
#         f = (1+1/i)**i
#     a.append(float(f))
# print(sum(a))

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

# N = int(input('Введите значение N: '))
# b = -N
# a = []
# while N > b-1:
#     a.append(int(b))
#     b += 1
# print(a)
# data = open('file.txt')
# x = int(data.read(1))
# y = int(data.read(2))
# data.close
# a.append(a[x] * a[y])
# print(a)

# Реализуйте алгоритм перемешивания списка.

# import random


# a = [1, 2, 3, 4, 5, 6]
# print("Исходный список:    ", a)
# n = len(a)
# for i in range(n):
#     b = random.randint(0, n-1)
#     e = a.pop(b)
#     a.append(e)
# print("Перемешенный список:", a)