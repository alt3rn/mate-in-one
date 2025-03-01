from Class.pieces import *
from Class.echiquier import *
import pprint

Piece1 = Piece()
board = Board.initBoardDico()
board2 = Board.initBoardList()
Piece1.pion()

pprint.pprint(board)
pprint.pprint(board2)
