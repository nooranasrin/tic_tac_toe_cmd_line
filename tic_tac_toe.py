def get_position():
    return int(input('Enter the position : '))


class TicTacToe:
    def __init__(self):
        self.rows = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.current_player = 2
        self.is_won = False
        self.entered_positions = []
        self.chances = 1
        self.symbols = {0: 'X', 1: 'O'}
        self.win_conditions = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [4, 5, 6], [7, 8, 9], [3, 6, 9], [3, 5, 7]]

    def get_board(self):
        board = ''
        current_row = [0, 3, 6]
        for row in current_row:
            board += "     |     |     \n"
            board += f'  {self.rows[row]}  |  {self.rows[row + 1]}  |   {self.rows[row + 2]}  \n'
            board += "     |     |     \n"
            board += "- - - - - - - - -\n"
        return board

    def change_player(self):
        return int(not self.current_player)

    def get_player_name(self):
        return 'player 1' if self.current_player == 0 else 'player 2'

    def is_valid_position(self, position):
        return position not in self.entered_positions and 0 <= position < 9

    def is_won_the_game(self):
        for condition in self.win_conditions:
            symbol = self.symbols[self.current_player]
            if self.rows[condition[0] - 1] == symbol and self.rows[condition[1] - 1] == symbol and self.rows[condition[2] - 1] == symbol:
                return True
        return False

    def play(self):
        if self.chances > 9:
            return 'draw🙁'
        print(self.get_board())
        if self.is_won:
            return f'{self.get_player_name()} won the game🥳'
        self.current_player = self.change_player()
        print(f'player : {self.get_player_name()}')
        position = get_position()
        is_position_valid = self.is_valid_position(position - 1)
        if is_position_valid:
            self.entered_positions.append(position - 1)
            self.rows[position - 1] = self.symbols[self.current_player]
            self.is_won = self.is_won_the_game()
            self.chances += 1
            return self.play()
        else:
            print('\nThe entered position is not valid! Please enter a valid position')
            self.current_player = self.change_player()
            return self.play()


def main():
    tic_tac_toe = TicTacToe()
    game_status = tic_tac_toe.play()
    print(game_status)


main()
