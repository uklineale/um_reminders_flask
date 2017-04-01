import tablib

class Parser(object):
    def parseCsv(self, csvFile):
        #Setup csv parser
        data = tablib.Dataset().load(csvFile)
        data.headers=['phone','msg']
    
        return data
