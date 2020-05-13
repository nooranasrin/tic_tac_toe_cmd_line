def get_tic_tac_toe_board(rows):
    board = ''
    current_row = [0, 3, 6]
    for row in current_row:
        board += "     |     |     \n"
        board += f'  {rows[row]}  |  {rows[row + 1]}  |   {rows[row + 2]}  \n'
        board += "     |     |     \n"
        board += "- - - - - - - - -\n"
    return board


def change_player(current_player):
    return int(not current_player)


def get_player_name(current_player):
    return 'player 1' if current_player == 0 else 'player 2'


def get_position(current_player):
    print(f'player : {get_player_name(current_player)}')
    return int(input('Enter the position : '))


def is_valid_position(entered_positions, position):
    return position not in entered_positions and 0 <= position < 9


def is_won_the_game(symbol, rows):
    win_conditions = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [4, 5, 6], [7, 8, 9], [3, 6, 9], [3, 5, 7]]
    for condition in win_conditions:
        if rows[condition[0] - 1] == symbol and rows[condition[1] - 1] == symbol and rows[condition[2] - 1] == symbol:
            return True
    return False


def play(current_player, is_won, entered_positions, rows, chance):
    if chance > 9:
        return 'draw'
    symbols = {0: 'X', 1: 'O'}
    print(get_tic_tac_toe_board(rows))
    if is_won:
        return f'{get_player_name(current_player)} won the game🥳'
    current_player = change_player(current_player)
    position = get_position(current_player)
    is_position_valid = is_valid_position(entered_positions, position - 1)
    if is_position_valid:
        entered_positions.append(position - 1)
        rows[position - 1] = symbols[current_player]
        is_won = is_won_the_game(symbols[current_player], rows)
        return play(current_player, is_won, entered_positions, rows, chance + 1)
    else:
        print('\nThe entered position is not valid! Please enter a valid position')
        return play(change_player(current_player), is_won, entered_positions, rows, chance)


def main():
    rows = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    game_status = play(2, False, [], rows, 1)
    print(game_status)


main()
