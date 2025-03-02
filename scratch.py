from Class.echiquier import *


def display(board):
    num_line = 8
    nom_col = 'abcdefgh'
    line_top_bot = '  +' + '------+'*8
    
    for i in range(len(board)-1, -1, -1):
        ligne_print = f'{i+1} |'
        if num_line%2 == 0: 
            ligne_up_and_bottom_case = '  |' + '■■■■■■|□□□□□□|'*4
            for j in range(len(board[i])):
                if j%2 == 0:
                    ligne_print += f"■■{board[i][j]}■■|"
                elif j%2 == 1:
                    ligne_print += f"□□{board[i][j]}□□|"
        elif num_line%2 == 1:
            ligne_up_and_bottom_case = '  |' + '□□□□□□|■■■■■■|'*4
            for j in range(len(board[i])):
                if j%2 == 1:
                    ligne_print += f"■■{board[i][j]}■■|"
                elif j%2 == 0:
                    ligne_print += f"□□{board[i][j]}□□|"
        print(line_top_bot)
        print(ligne_up_and_bottom_case)
        print(ligne_print)
        print(ligne_up_and_bottom_case)
        num_line -= 1
    print(line_top_bot)
    ligne_col = '  '
    for i in nom_col:
        ligne_col += f'   {i}   '
    print(ligne_col)
    return None

test = Board.initBoardList()
display(test)
