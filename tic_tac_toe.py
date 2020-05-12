def get_tic_tac_toe_board():
    rows = [0, 3, 6]
    board = ''
    for row in rows:
        board += "     |     |     \n"
        board += f'  {row}  |  {row + 1}  |   {row + 2}  \n'
        board += "     |     |     \n"
        board += "- - - - - - - - -\n"
    return board

