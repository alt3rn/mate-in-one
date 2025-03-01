from Class.pieces import *
from Class.echiquier import *
import pprint

Piece1 = Piece()
board = Board.initBoardDico()
board_test = Board.initBoardList()
Piece1.pion()


def main():
    # Les indices dans le board sont inversés : a3 correspond à [2][0], soit 3a

    # Cette partie permet de simuler un coup pion e4 (pour les blancs). Pour un print correct
    # du jeu avec les blancs en bas et le plateau dans le bon sens, il faut parcourir avec un for i in range(.., ..., -1)
    board_test[1][4] = 'p'
    print('Avant le mouvement')
    pprint.pprint(board_test)
    print(f" ----- ")
    Board.movement(board_test, 'p', 'e4') 
    print('Après le mouvement :')
    pprint.pprint(board_test)

    Board.display(board_test)  # Première idée de ce à quoi ressemble le board_test, dans le bon sens.

    pass


main()