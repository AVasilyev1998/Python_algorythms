import os


def which_player(player):
    if player == 1:
        return 'X'
    elif player == 2:
        return 'O'
    else:
        return '-'


def draw_thing(state):
    for i in range(0, 3):
        print(' --- --- ---')
        str_tmp = '| '
        for j in range(0,3):
            str_tmp += which_player(state[i][j]) + ' | '
        print(str_tmp)
    print(' --- --- ---')


def check_win(state_matrix):
    #
    if state_matrix[0][0] == state_matrix[0][1] and state_matrix[0][1] == state_matrix[0][2] and state_matrix[0][0] != 0:
        return state_matrix[0][0]
    elif state_matrix[1][0] == state_matrix[1][1] and state_matrix[1][1] == state_matrix[1][2] and state_matrix[1][0] != 0:
        return state_matrix[1][0]
    elif state_matrix[2][0] == state_matrix[2][1] and state_matrix[2][1] == state_matrix[2][2] and state_matrix[2][0] != 0:
        return state_matrix[2][0]
    #
    elif state_matrix[0][0] == state_matrix[1][0] and state_matrix[1][0] == state_matrix[2][0] and state_matrix[0][0] != 0:
        return state_matrix[0][0]
    elif state_matrix[0][1] == state_matrix[1][1] and state_matrix[1][1] == state_matrix[2][1] and state_matrix[0][1] != 0:
        return state_matrix[0][1]
    elif state_matrix[0][2] == state_matrix[1][2] and state_matrix[1][2] == state_matrix[2][2] and state_matrix[0][2] != 0:
        return state_matrix[1][2]
    #
    elif state_matrix[0][0] == state_matrix[1][1] and state_matrix[1][1] == state_matrix[2][2] and state_matrix[0][0] != 0:
        return state_matrix[0][0]
    elif state_matrix[0][2] == state_matrix[1][1] and state_matrix[1][1] == state_matrix[2][0] and state_matrix[0][2] != 0:
        return state_matrix[0][2]
    else:
        return 0


def change_state(state, player, x, y):
    if state[x][y] == 0:
        state[x][y] = player
    else:
        raise IndexError


def change_player(player):
    if player == 1:
        return 2
    else:
        return 1


def game():
    stop_game = 0
    while not stop_game:
        game_state1 = [[0, 0, 0],
                       [0, 0, 0],
                       [0, 0, 0]]
        player = 1
        draw_thing(game_state1)
        game_won = check_win(game_state1)
        while not game_won:
            print('Игрок ', player)
            try:
                print('Ваш ход')
                x, y = tuple([int(i) for i in input().split()])
            except ValueError:
                print('Неверный ход, попробуйте снова')
                continue
            try:
                change_state(game_state1, player, x, y)
            except IndexError:
                print('Неверный ход, попробуйте снова')
                continue
            draw_thing(game_state1)
            game_won = check_win(game_state1)
            player = change_player(player)
        else:
            print('Игрок ', game_won, ' выиграл игру!')
        print('Если хотите продолжить напечатайте "Да" или нажмите Enter')
        inp = input()
        if inp == 'Да' or inp == '':
            pass
        else:
            stop_game = 1


game()
