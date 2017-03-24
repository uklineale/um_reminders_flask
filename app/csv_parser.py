import tablib

#Setup csv parser
data = Dataset().load(open('data.csv').read())
data.headers = ('phone', 'msg')

