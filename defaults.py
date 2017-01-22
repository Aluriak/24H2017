import re


PORT_DUMP_FILE = 'dump01.txt'
PORT_NAME = '/dev/ttyUSB0'
BAUD_RATE = 230400
REGEX_4TIMES8 = re.compile('([0-9]+)\s*times?\s*([0-9]+)\s*\?')
