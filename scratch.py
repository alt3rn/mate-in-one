from Class.echiquier import *


def display(board):
        """
        Affiche le plateau actuel dans la console
        Parameters:
            board: list[list] - Echiquier sous forme de liste
        
        Return: None
        """
        num_line = 8
        nom_col = 'abcdefgh'
        line_top_bot = '  +' + '--------+'*8
    
        for i in range(len(board)-1, -1, -1):
            ligne_print = f'{i+1} |'
            line_border = '  |'
            if num_line%2 == 0: 
                ligne_up_and_bottom_case = '  |' + '■■■■■■■■|        |'*4
                for j in range(len(board[i])):
                    if j%2 == 0:
                        if board[i][j] == '  ':
                            ligne_print += '■■■■■■■■|'
                            line_border += '■■■■■■■■|'
                        else:
                            line_border += '■■    ■■|'
                            ligne_print += f"■■ {board[i][j]} ■■|"
                    elif j%2 == 1:
                        ligne_print += f"   {board[i][j]}   |"
                        line_border += '        |'
                        
            elif num_line%2 == 1:
                ligne_up_and_bottom_case = '  |' + '        |■■■■■■■■|'*4
                for j in range(len(board[i])):
                    if j%2 == 1:
                        if board[i][j] == '  ':
                            ligne_print += '■■■■■■■■|'
                            line_border += '■■■■■■■■|'
                        else:
                            ligne_print += f"■■ {board[i][j]} ■■|"
                            line_border += '■■    ■■|'
                    elif j%2 == 0:
                        ligne_print += f"   {board[i][j]}   |"
                        line_border += '        |'
                        

            
            print(line_top_bot)
            print(ligne_up_and_bottom_case)
            print(line_border)
            print(ligne_print)
            print(line_border)
            print(ligne_up_and_bottom_case)
            num_line -= 1
        print(line_top_bot)
        ligne_col = '  '
        for i in nom_col:
            ligne_col += f'    {i}    '
        print(ligne_col)
        return None

test = Board.initBoardList()
display(test)

neuille = '◇'