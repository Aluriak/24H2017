from defaults import PORT_DUMP_FILE


def decode_ascii(line):

    try:

        return line.decode('ascii')

    except:

        return None


def decode_unicode(line):

    try:

        return line.decode('unicode')

    except:

        return None


def decode_hex(line):

    try:

        return line.decode('hexadecimal')

    except:

        return None


def decode_binary(line):

    try:

        return line.decode('binary')

    except:

        return None


def decode_file(filename):

    with open(filename) as in_file:

        for line in in_file:
            for method in methods:
                print(method(line))


methods = [decode_ascii, decode_unicode, decode_hex, decode_binary]

decode_file(PORT_DUMP_FILE)
