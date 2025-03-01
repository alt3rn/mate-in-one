COLUMNS = ["a","b","c","d","e","f","g","h"]
CONVERT_COL= {'a': 1,
               'b': 2,
               'c': 3,
               'd': 4,
               'e': 5,
               'f': 6,
               'g': 7,
               'h': 8
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
        
        for i in range(1, 9):
            ligne = []
            for j in range(1, 9):
                ligne.append('_')
            echiquier.append(ligne)
        return echiquier
    

    def convertPosition(position: str):
        """
        Renvoie les indices utilisables pour les listes construisant le plateau
        position: str - Position du pion. Ex: 'e4', 'b8'
        ---
        return: int, int
        """
        line = CONVERT_COL[position[0]]
        col = int(position[2])
        return line, col


    def movement(board: list, piece: str, next_position: str):
        """
        Réalise le mouvement demandé sur le plateau. 
        board: list - Le plateau sous forme de liste
        piece: str - Pièce qui bouge
        next_position: Prochaine position du pion.
        ---
        return: list - Plateau avec le mouvement réalisé. L'ancienne position du pion après le mouvement est ainsi vide.
        """
        for line in board:
            position_actuelle = line.find(piece)
        col_next, line_next = Board.convertPosition(next_position)
        board[col_next][line_next] = piece
        col_old, line_old = Board.convertPosition(position_actuelle)
        board[col_old][line_old] = '_'
        return board
