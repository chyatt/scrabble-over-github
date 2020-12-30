import sys
import utils

# TODO - Fix hard coded filename
with open('bag.txt', 'r') as bag:
    tiles = [line.strip() for line in bag]

# TODO - Handle command line error checking
# TODO - Handle empty bag or not enough tiles remaining
dealtTiles, tiles = tiles[:int(sys.argv[1])], tiles[int(sys.argv[1]):]

# TODO - Fix hard coded filenames
utils.writeBag(tiles,'bag.txt')
utils.logTurn(','.join(dealtTiles),'log.txt')
print(','.join(dealtTiles))