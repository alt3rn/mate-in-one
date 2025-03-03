from Class.echiquier import *
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

class Pawn:
    def __init__(self, numero, color):
        self.position = f'{CONVERT[numero-1]}2'
        if color == 'white':
            self.id = f'❖P{numero}'
        elif color == 'black':
            self.id = f'◇P{numero}'

    

    
        

