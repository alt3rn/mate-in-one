from Class.pieces import *
from Class.echiquier import *
import pprint

Piece1 = Piece()
board_test = Board.initBoard()
Piece1.pion()


SLOTS = []
for column in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
    for i in range(1, 9):
        SLOTS.append(f"{column}{i}")

    

def player_turn(slots_available, pieces_available):
    piece_to_move = input('Quelle pièce souhaitez-vous jouer ? ')
    while piece_to_move not in pieces_available:
        piece_to_move = input('Quelle pièce souhaitez-vous jouer ? ')
    where_to_move = input('Où voulez-vous jouer cette pièce ? ')
    while where_to_move not in slots_available:
        where_to_move = input('Où voulez-vous jouer cette pièce ? ')
    return piece_to_move, where_to_move
    




def main():
    # Les indices dans le board sont inversés : a3 correspond à [2][0], soit 3a

    # Cette partie permet de simuler un coup pion e4 (pour les blancs). Pour un print correct
    # du jeu avec les blancs en bas et le plateau dans le bon sens, il faut parcourir avec un for i in range(.., ..., -1)
    # board_test[1][4] = '❖P5'
    Board.display(board_test) 
    # piece_to_move = input('Quelle pièce souhaitez-vous jouer ? ')
    # where_to_move = input('Où voulez-vous jouer cette pièce ? ')
    # Board.movement(board_test, piece_to_move, where_to_move)
    Board.display(board_test)  # Première idée de ce à quoi ressemble le board_test, dans le bon sens.
    
    
    # Boucle de jeu
    moves = 0
    game_ended = False
    while not game_ended:
        moves += 1
        piece_to_move, where_to_move = player_turn(SLOTS, ['❖P1', '❖P3', "❖P5", "❖P7", "❖Q"])
        Board.movement(board_test, piece_to_move, where_to_move)
        Board.display(board_test)
        if moves == 5:
            game_ended = True
    pass


main()