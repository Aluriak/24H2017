from defaults import PORT_DUMP_FILE
from itertools import islice
from bitstring import BitArray


def decode_ascii(line):

    try:

        return line.decode('ascii')

    except UnicodeDecodeError:

        return "Error"


def decode_unicode(line):

    try:

        return line.decode('utf8')

    except UnicodeDecodeError:

        return "Error"


def decode_hex(line):

    try:

        return line.hex()

    except:

        return "Error"


def decode_binary(line):

    try:

        return BitArray(line).bin

    except:

        return "Error"


def decode_file(filename, length, methods):

    for method in methods:
        with open(filename, 'rb') as in_file:
            print(method.__name__ + ' :\n\n')
            for i, line in enumerate(islice(in_file, 0, length)):
                print(method(line))
            print('\n\n')


methods = [decode_ascii, decode_unicode, decode_hex, decode_binary]

decode_file(PORT_DUMP_FILE, 30, methods)
