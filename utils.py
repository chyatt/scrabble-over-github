def writeBag(tiles, file):
    with open(file, 'w') as bag:
        for tile in tiles:
            bag.write("{}\n".format(tile))

def logTurn(message, file):
    with open(file, 'a') as logfile:
        logfile.write(message + '\n')

def clearLogFile(file):
    open(file, 'w').close()