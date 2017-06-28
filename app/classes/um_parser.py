import logging
import csv

#   Parses a csv string
#   Input:
#       csvString - a csv of type string
#   Returns:
#       a list of
def parse(csvString):
    logging.info('Parsing file')

    reader = csv.reader(csvString.split('\n'), delimiter=',')

    logging.debug('CSV Reader object created')
    messages = []
    for row in reader:
        logging.debug(' '.join(row))
        messages.append(row)

    logging.info('Done parsing')

    ret = list(reader)
    print('ret in parser' + len(ret))

    return list(reader)
