import tablib
import messaging

def parseCsv(csvFile):
    #Setup csv parser
    data = tablib.Dataset().load(csvFile)
    data.headers=['phone','msg']

    return data
