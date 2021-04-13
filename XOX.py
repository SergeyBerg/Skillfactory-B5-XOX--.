print('Игра крестики - нолики')
print('Чтобы сделать ход необходимо')
print('вести индекс поля от 1 до 9')
print('На игровом поле имеются следующие индексы')
print('| 1 || 2 || 3 |')
print('| 4 || 5 || 6 |')
print('| 7 || 8 || 9 |')

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]

def print_state(state):
    for i, c in enumerate(state):
        if (i+1)%3==0:
            print(f'| {c} |')
        else:
            print(f'| {c} |', end='')
    print('Текущий статус доски')
    print()

win_comb=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8 ),(2,4,6,)]

def get_win(state, comb):
    for(x, y, z) in comb:
        if state[x] == state[y] and state[y] == state[z] and (state[x]=='X' or state[x]=='O'):
            return state[x]
    return ''

def play_game(board):
    sign = 'X'
    while(get_win(board, win_comb)==''):
        print(f'Текущий ход - {sign}')
        while True:
            index = input(f'Где вы хотите нарисовать {sign} (введите индекс от 1 до 9)?')
            if not index.isnumeric():
                print("Вы ввели не число. Попробуйте снова: ")
            elif not 1 <= int(index) <= 9:
                print("Индекс должен быть от 1 до 9")
            elif not board[int(index) - 1] == ' ':
                print(f'Позиция {index} занята')
            else:
                board[int(index) - 1] = sign
                print(f'В позицию {int(index)} записан символ {sign}')
                print()
                break

        board[int(index)-1] = sign
        print_state(board)
        win_sign = get_win(board, win_comb)
        if win_sign !='':
            print(f'Победа: {win_sign}')
        elif board.count(' ') == 0:
            print('В игровом поле не осталось клеток')
            print('Игра победителя не выявила')
            break
        sign = 'X' if sign == 'O' else 'O'

play_game(board)
