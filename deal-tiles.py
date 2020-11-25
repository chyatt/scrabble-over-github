import sys
import utils

# TODO - Fix hard coded filename
with open('bag.txt', 'r') as bag:
    tiles = [line.strip() for line in bag]

# TODO - Handle command line error checking
dealtTiles, tiles = tiles[:int(sys.argv[1])], tiles[int(sys.argv[1]):]

# TODO - Fix hard coded filenames
utils.writeBag(tiles,'bag.txt')
utils.logTurn(','.join(dealtTiles),'log.txt')