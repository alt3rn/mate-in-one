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
                echiquier[f"{colonne}{ligne}"] = '_'
        return echiquier
    

    def initBoardList():
        """
        Crée le plateau sous forme de liste
        ---
        return: list
        """
        echiquier = []
        
        for i in range(0, 8):
            ligne = []
            for j in range(0, 8):
                ligne.append('_')
            echiquier.append(ligne)
        return echiquier
    

    def convertIndice(position: str):
        """
        Renvoie les indices utilisables pour les listes construisant le plateau
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
        col: int - Numéro de la colonne
        line: int - Numéro de la ligne (-1 par rapport à la ligne réelle comme c'est un indice)
        ---
        return: str - La position équivalente
        """
        column = CONVERT[col]
        return f"{column}{line+1}"


    def movement(board: list, piece: str, next_position: str):
        """
        Réalise le mouvement demandé sur le plateau. 
        board: list - Le plateau sous forme de liste
        piece: str - Pièce qui bouge
        next_position: Prochaine position du pion.
        ---
        return: list - Plateau avec le mouvement réalisé. L'ancienne position du pion après le mouvement est ainsi vide.
        """
        for i in range(0, 8):
            if piece in board[i]:  # Implique que chaque pièce a un nom UNIQUE
                actual_position_col = board[i].index(piece)
                actual_position_line = i
                actual_position = Board.convertPosition(actual_position_col, actual_position_line)
        line_next, col_next = Board.convertIndice(next_position)
        board[line_next][col_next] = piece
        line_old, col_old = Board.convertIndice(actual_position)
        board[line_old][col_old] = '_'
        return board
    

    def display(board):
        for i in range(len(board)-1, -1, -1):
            ligne_print = ''
            for square in board[i]:
                ligne_print += f"{square} "
            print(ligne_print)
        return None