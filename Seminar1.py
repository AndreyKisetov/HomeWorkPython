# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# A = int(input('Введите цифру, обозначающую день недели: '))
# if A == 1 or A ==2 or A ==3 or A ==4 or A ==5:
#     print(f'{A} → нет')
# elif A == 6 or A ==7:
#     print(f'{A} → да')
# else:
#     print('некорректная цифра')

# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# X = int(input('Введите значение предиката X: '))
# Y = int(input('Введите значение предиката Y: '))
# Z = int(input('Введите значение предиката Z: '))
# F1 = not(X or Y or Z)
# F2 = (not X) and (not Y) and (not Z)
# f = bool(F1 == F2)
# print(f)

# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# x = int(input('Введите значение координаты X: '))
# y = int(input('Введите значение координаты Y: '))
# if x > 0 and y > 0:
#     print(f'x={x}; y={y} → 1')
# elif x < 0 and y > 0:
#     print(f'x={x}; y={y} → 2')
# elif x < 0 and y < 0:
#     print(f'x={x}; y={y} → 3')
# elif x > 0 and y < 0:
#     print(f'x={x}; y={y} → 4')
# else:
#     print('одна или две координаты находятся на оси!')

# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# quarterNamber = int(input('Введите номер четверти: '))
# if quarterNamber == 1:
#     print(f'x(0;∞) and y(0;∞)')
# elif quarterNamber == 2:
#     print(f'x(-∞;0) and y(0;∞)')
# elif quarterNamber == 3:
#     print(f'x(-∞;0) and y(-∞;0)')
# elif quarterNamber == 4:
#     print(f'x(0;∞) and y(-∞;0)')
# else:
#     print('номер не соответствует четверти')

# Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.

# x1 = int(input('Введите координату A по оси x: '))
# y1 = int(input('Введите координату A по оси y: '))
# x2 = int(input('Введите координату B по оси x: '))
# y2 = int(input('Введите координату B по оси y: '))
# d = ((x1-x2)**2+(y1-y2)**2)**(1/2)
# c = int(d*100)/100
# print(f'A({x1};{y1}), B({x2};{y2}) → {c}')