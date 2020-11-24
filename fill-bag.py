import random

# Default list of letter tiles in Scrabble
tiles = ['A1','A1','A1','A1','A1','A1','A1','A1','A1',
       'B3','B3',
       'C3','C3',
       'D2','D2','D2','D2',
       'E1','E1','E1','E1','E1','E1','E1','E1','E1','E1','E1', 'E1',
       'F4','F4',
       'G2','G2','G2',
       'H4','H4']
# TODO - Add the rest of the tiles!

# Shuffle tiles and add them to bag.txt for later use
random.shuffle(tiles)
with open('bag.txt', 'w') as bag:
    for tile in tiles:
        bag.write("{}\n".format(tile))