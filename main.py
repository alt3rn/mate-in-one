from Class.pieces import *
from Class.echiquier import *
import pprint


board_test = Board.initBoard()



SLOTS = []
for column in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
    for i in range(1, 9):
        SLOTS.append(f"{column}{i}")

    

def player_turn(turn, slots_available, pieces_available):
    """
    Affiche dans la console une demande au joueur pour choisir la pièce qu'il souhaite jouer, et ensuite où.
    Parameters:
    turn: str - 'white' ou 'black' -> Sert à changer l'output de la pièce utilisée (comme elles ont un ID unique)
    slots_available: list - Les cases du plateau où le pion peut bouger (toutes les cases du plateau, donc ça sert juste à vérifier que le joueur demande pas à sortir du plateau)

    """
    if turn == 'white':
        piece_to_move = '❖' + input('Au tour des blancs. Quelle pièce souhaitez-vous jouer ? ')
        while piece_to_move not in pieces_available:
            piece_to_move = '❖' + input('Au tour des blancs. Quelle pièce souhaitez-vous jouer ? ')
        where_to_move = input('Où voulez-vous jouer cette pièce ? ')
        while where_to_move not in slots_available:
            where_to_move = input('Où voulez-vous jouer cette pièce ? ')
        return piece_to_move, where_to_move
    
    if turn == 'black':
        piece_to_move = '◇' + input('Au tour des noirs. Quelle pièce souhaitez-vous jouer ? ')
        while piece_to_move not in pieces_available:
            piece_to_move = '◇' + input('Au tour des noirs. Quelle pièce souhaitez-vous jouer ? ')
        where_to_move = input('Où voulez-vous jouer cette pièce ? ')
        while where_to_move not in slots_available:
            where_to_move = input('Où voulez-vous jouer cette pièce ? ')
        return piece_to_move, where_to_move
    
    
def create_pieces():
    list_pieces = []
    for pawn_white_num in range(1, 9):
        pion = Pawn(pawn_white_num, 'white')
        list_pieces.append(pion.id)
    for pawn_black_num in range(1, 9):
        pion = Pawn(pawn_black_num, 'black')
        list_pieces.append(pion.id)
    return list_pieces




def main():
    # Les indices dans le board sont inversés : a3 correspond à [2][0], soit 3a

    # board_test[1][4] = '❖P5'
    #     # piece_to_move = input('Quelle pièce souhaitez-vous jouer ? ')
    # where_to_move = input('Où voulez-vous jouer cette pièce ? ')
    # Board.movement(board_test, piece_to_move, where_to_move)
    Board.display(board_test)  # Première idée de ce à quoi ressemble le board_test, dans le bon sens.
    pieces_available = create_pieces()
    print(pieces_available)
    wP1 = Pawn(1, 'white')
    print(wP1.position, wP1.id)
    
    # Initialisation du jeu
    moves = 0
    game_ended = True
    turn = 'white'
    
     # Boucle de jeu
    while not game_ended:
        moves += 1
        piece_to_move, where_to_move = player_turn(turn, SLOTS, pieces_available)
        

        Board.movement(board_test, piece_to_move, where_to_move)
        Board.display(board_test)

        # Limite imposée, à retirer avant la version finale, et remplacer par isCheckMate()
        if moves == 5:
            game_ended = True

        # Alterne les joueurs blancs et noirs
        if turn == 'white':
            turn = 'black'
        else:
            turn = 'white'
    pass


main()