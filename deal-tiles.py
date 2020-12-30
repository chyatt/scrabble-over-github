import sys
import utils
import os

# TODO - Fix hard coded filename
with open('bag.txt', 'r') as bag:
    tiles = [line.strip() for line in bag]

# TODO - Handle command line error checking
# TODO - Handle empty bag or not enough tiles remaining
numTiles = os.getenv('INPUT_NUMTILES')
print('NumTiles: ')
print(numTiles)

# Note: this no longer works with command line args - needs an 
# environment variable called INPUT_NUMTILES instead (so it can
# be used by GitHub Actions)
dealtTiles, tiles = tiles[numTiles], tiles[numTiles]

# TODO - Fix hard coded filenames
utils.writeBag(tiles,'bag.txt')
utils.logTurn(','.join(dealtTiles),'log.txt')
print(','.join(dealtTiles))