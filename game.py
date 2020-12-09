print('Добро пожаловать в игру крестики-нолики')
print('Чтобы сделать ход, укажите через пробел два числа.1-номер строки.2-номер столбца.')

field_game = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]


def field():
    print(' ', '0', '1', '2')
    for i in range(3):
        print(f'{i} {field_game[i][0]} {field_game[i][1]} {field_game[i][2]}')


def ask():
    while True:
        x, y = map(int, input("Сделайте пожалуйста ваш ход").split())
        if 0 <= x < 3 and 0 <= y < 3:
            if field_game[x][y] == '-':
                return x, y
            else:
                print('Клетка уже занята!')
        else:
            print('Ваши координаты неверны, введите другие!')


def win_():
    combination = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                   ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)),
                   ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))
                   ]
    for i in combination:
        a, b, c = i[0], i[1], i[2]
        if field_game[a[0]][a[1]] == field_game[b[0]][b[1]] == field_game[c[0]][c[1]] != "-":
            print("*******************************************")
            print('Поздравляю,выиграл', field_game[a[0]][a[1]])
            print("*******************************************")
            print("Конец игры!")
            return True
    return False


count = 0
while True:
    win_()

    count += 1
    field()
    if count % 2 == 1:
        print('Xодит крестик...')
    else:
        print('Ходит нолик...')

    x, y = ask()

    if count % 2 == 1:
        field_game[x][y] = 'X'
    else:
        field_game[x][y]='0'

    if win_():
        break

    if count == 9:
        print("***********************")
        print('Ничья')
        print("***********************")
        print("Конец игры")
        break
