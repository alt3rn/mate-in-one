COLUMNS = ["a","b","c","d","e","f","g","h"]
CONVERT = {'a': 0,
               'b': 1,
               'c': 2,
               'd': 3,
               'e': 4,
               'f': 5,
               'g': 6,
               'h': 7,
               0: 'a',
               1: 'b',
               2: 'c',
               3: 'd',
               4: 'e',
               5: 'f',
               6: 'g',
               7: 'h'
               }

class Board:
    def __init__(self, config):
        self.config = config  # Configuration actuelle du plateau (disposition des pions)


    def initBoardDico():
        """
        Crée le plateau sous forme de dico
        ---
        return: dico
        """
        echiquier = {}
        for colonne in COLUMNS:
            for ligne in range(1, 9):
                echiquier[f"{colonne}{ligne}"] = '   '
        return echiquier
    

    def initBoardList():
        """
        Crée le plateau VIDE sous forme de liste
        ---
        return: list
        """
        echiquier = []
        
        for i in range(0, 8):
            ligne = []
            for j in range(0, 8):
                ligne.append('   ')
            echiquier.append(ligne)
        return echiquier
    

    def initBoard():
        """
        Crée le plateau avec la disposition des pièces de départ, sous forme de liste.
        ---
        return: list
        """
        board = Board.initBoardList()
        # J'ai aucune idée de comment optimiser ce truc donc bon, j'ai ff et j'ai fait à l'ancienne
        # Placement pions blancs
        for i in range(1, 9):
            board[1][i-1] = f'❖P{i}'
            board[6][i-1] = f'◇P{abs(i-9)}'
        board[0] = ['❖R1', '❖N1', '❖B1', '❖Q', '❖K', '❖B2', '❖N2', '❖R2']
        board[7] = ['◇R2', '◇N2', '◇B2', '◇Q', '◇K', '◇B1', '◇N1', '◇R1']

        return board
    

    def convertIndice(position: str):
        """
        Renvoie les indices utilisables pour les listes construisant le plateau
        Parameters:
            position: str - Position du pion. Ex: 'e4', 'b8'
        ---
        return: int, int
        """
        col = CONVERT[position[0]]
        line = int(position[1])-1
        return line, col
    
    def convertPosition(col: int, line: int):
        """
        La fonction convertIndice() mais en reverse : donne un équivalent d'indices pour une position donnée.
        Parameters:
            col: int - Numéro de la colonne
            line: int - Numéro de la ligne (-1 par rapport à la ligne réelle comme c'est un indice)
        ---
        Return: str - La position équivalente
        """
        column = CONVERT[col]
        return f"{column}{line+1}"


    def movement(board: list, piece: str, next_position: str):
        """
        Réalise le mouvement demandé sur le plateau. 
        Parameters:
            board: list - Le plateau sous forme de liste
            piece: str - Pièce qui bouge
            next_position: str - Prochaine position du pion.
        
        Return: list - Plateau avec le mouvement réalisé. L'ancienne position du pion après le mouvement est ainsi vide.
        """
        for i in range(0, 8):
            if piece in board[i]:  # Implique que chaque pièce a un nom UNIQUE
                actual_position_col = board[i].index(piece)
                actual_position_line = i
                actual_position = Board.convertPosition(actual_position_col, actual_position_line)
        line_next, col_next = Board.convertIndice(next_position)
        board[line_next][col_next] = piece
        line_old, col_old = Board.convertIndice(actual_position)
        board[line_old][col_old] = '   '
        return board
    

    def display(board):
        """
        Affiche le plateau actuel dans la console
        Parameters:
            board: list[list] - Echiquier sous forme de liste
        
        Return: None
        """
        num_line = 8
        nom_col = 'abcdefgh'
        line_top_bot = '  +' + '---------+'*8

        for i in range(len(board)-1, -1, -1):
            ligne_print = f'{i+1} |'
            line_border = '  |'
            if num_line%2 == 0: 
                ligne_up_and_bottom_case = '  |' + '■■■■■■■■■|         |'*4
                for j in range(len(board[i])):
                    if j%2 == 0:
                        if board[i][j] == '   ':
                            ligne_print += '■■■■■■■■■|'
                            line_border += '■■■■■■■■■|'
                        elif len(board[i][j]) == 2:
                            ligne_print += f"■■ {board[i][j]}  ■■|"
                            line_border += '■■     ■■|'
                        else:
                            ligne_print += f"■■ {board[i][j]} ■■|"
                            line_border += '■■     ■■|'
                    elif j%2 == 1:
                        if len(board[i][j]) == 2:
                            ligne_print += f"   {board[i][j]}    |"
                            line_border += '         |'
                        else:
                            ligne_print += f"   {board[i][j]}   |"
                            line_border += '         |'
                        
            elif num_line%2 == 1:
                ligne_up_and_bottom_case = '  |' + '         |■■■■■■■■■|'*4
                for j in range(len(board[i])):
                    if j%2 == 1:
                        if board[i][j] == '   ':
                            ligne_print += '■■■■■■■■■|'
                            line_border += '■■■■■■■■■|'
                        elif len(board[i][j]) == 2:
                            ligne_print += f"■■ {board[i][j]}  ■■|"
                            line_border += '■■     ■■|'
                        else:
                            ligne_print += f"■■ {board[i][j]} ■■|"
                            line_border += '■■     ■■|'
                    elif j%2 == 0:
                        if len(board[i][j]) == 2:
                            ligne_print += f"   {board[i][j]}    |"
                            line_border += '         |'
                        else:
                            ligne_print += f"   {board[i][j]}   |"
                            line_border += '         |'
            
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
            ligne_col += f'     {i}    '
        print(ligne_col)
        return None