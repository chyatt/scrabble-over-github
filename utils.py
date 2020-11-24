def writeBag(tiles, file):
    with open(file, 'w') as bag:
        for tile in tiles:
            bag.write("{}\n".format(tile))