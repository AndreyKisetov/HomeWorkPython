# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# with open("words.txt",encoding='utf_8') as fin:
#     for line in fin:
#         words = line.split()
#         for word in words:
#             if "абв" in word:
#                 words.remove(word)
#         sentence = " ".join(words)
#         print(sentence)

# 2. Создайте программу для игры с конфетами человек против человека. 
# Дано 2021 конфета. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.

# def candy_game(a):
#     if 0 < a < 29:
#         global candys
#         candys -= a
#         print(f'Осталось {candys} конфет\n')
#         return candys
#     print('Введено некорректное число, игрок дисквалифицирован.\n')
    
# candys = 2021
# i = 0
# while i < candys:
#     gamer_1 = int(input('Игрок 1 вводит число от 1 до 28 включительно: '))
#     if candy_game(gamer_1) == None:
#         break
#     if i >= candys:
#         print(f'Ура!!! Игрок 1 забирает все конфеты!')
#         break
#     gamer_2 = int(input('Игрок 2 вводит число от 1 до 28 включительно: '))
#     if candy_game(gamer_2) == None:
#         break
#     if i >= candys:
#         print(f'Ура!!! Игрок 2 забирает все конфеты!')
#         break


# a) Добавьте игру против бота.

# from random import randint

# def candy_game(a):
#     if 0 < a < 29:
#         global candys
#         candys -= a
#         print(f'Осталось {candys} конфет\n')
#         return candys
#     print('Введено некорректное число, игрок дисквалифицирован.\n')

# candys = 2021
# i = 0
# while i < candys:
#     gamer_1 = int(input('Игрок 1 вводит число от 1 до 28 включительно: '))
#     if candy_game(gamer_1) == None:
#         break
#     if i >= candys:
#         print(f'Ура!!! Игрок 1 забирает все конфеты!')
#         break
#     gamer_2 = randint(1,28)
#     print(f'Бот ввёл {gamer_2}')
#     candy_game(gamer_2)
#     if i >= candys:
#         print(f'Ура!!! Игрок 1 забирает все конфеты!')
#         break

# b) Подумайте как наделить бота ""интеллектом""

# def candy_game(a):
#     if 0 < a < 29:
#         global candys
#         candys -= a
#         print(f'Осталось {candys} конфет\n')
#         return candys
#     print('Введено некорректное число, игрок 1 дисквалифицирован.')

# def bot_brains(a):
#     if candys%29 > 0:
#         a = candys%29
#         return a
#     return 1
    
# candys = 2021
# i = 0
# bot = int(input('Введите цифру 1 или 2 в соответствии с очерёдностью хода бота: '))
# if bot == 1 :
#     candys = 2001
#     print(f'Бот ввёл 20 \nОсталось {candys} конфет\n')
# while i < candys:
#     gamer_1 = int(input('Игрок 1 вводит число от 1 до 28 включительно: '))
#     if candy_game(gamer_1) == None:
#         break
#     if i >= candys:
#         print(f'Ура!!! Игрок 1 забирает все конфеты!')
#         break
#     gamer_2 = bot_brains(candys)
#     print(f'Бот ввёл {gamer_2}')
#     candy_game(gamer_2)
#     if i >= candys:
#         print(f'Игрок 1 проиграл боту.')
#         break


# 3. Создайте программу для игры в ""Крестики-нолики"".

# print("\n*" , " Игра Крестики-нолики для двух игроков ", "*")

# board = list(range(1,10))

# def draw_board(board):  # рисуем игровое поле
#    print(" –––" * 3)
#    for i in range(3):
#       print("│", board[0+i*3], "│", board[1+i*3], "│", board[2+i*3], "│")
#       print(" –––" * 3)

# def take_input(player_token):   # принимаем ввод пользователя
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):   # проверяем, выиграл ли игрок
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False

# def main(board):    # запускаем игровой процесс
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("x")
#         else:
#            take_input("○")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(f"Игрок {tmp} выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)

# input("Нажмите Enter для выхода!")


# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# with open('decoded.txt', 'r') as data:
#     my_text = data.read()

# def encode_rle(ss):
#     str_code = ''
#     prev_char = ''
#     count = 1
#     for char in ss:
#         if char != prev_char:
#             if prev_char:
#                 str_code += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     return str_code
            
# str_code = encode_rle(my_text)
# print(str_code)

# with open('encoded.txt', 'w') as data:
#     data.write(str_code)

# with open('encoded.txt', 'r') as data:
#     my_text2 = data.read()

# def decoding_rle(ss:str):
#     count = ''
#     str_decode = ''
#     for char in ss:
#         if char.isdigit():
#             count += char 
#         else:
#             str_decode += char * int(count)
#             count = ''
#     return str_decode

# str_decode = decoding_rle(my_text2)
# print(str_decode)
