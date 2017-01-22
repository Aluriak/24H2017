import re
import serial
from defaults import PORT_DUMP_FILE, PORT_NAME, BAUD_RATE, REGEX_4TIMES8


def gen_bytes(port_name):

    connection = serial.Serial(port_name, baudrate=230400, bytesize=serial.EIGHTBITS)  # open serial port
    print(connection.name)         # check which port was really used

    while True:

        yield connection.read()     # write a string

    connection.close()             # close port


def write_bytes(source, output_file):

    with open(output_file, 'wb') as output:

        [output.write(byte) for byte in source]


def laumii_protection_against_times():

    ser = serial.Serial(PORT_NAME, baudrate=BAUD_RATE, bytesize=serial.EIGHTBITS,
                        write_timeout=0.5, timeout=0.5)
    print('Connection:', ser)
    ser.write(b'\r\n')
    regex = re.compile(r'"([^"]+)"')

    received = ''
    gotos = set()
    next_is_last = False

    while True:
        bin_char = ser.read(1)
        if bin_char:  # have something to say
            new_char = bin_char.decode()
            received += new_char
            print(new_char, end='', flush=True)
            if ord(new_char) not in range(32, 126) and new_char != '\n':
                print('!{}!'.format(new_char.encode()), end='', flush=True)

            REGEX_WHITE_RABBIT = re.compile('[a-zA-Z ]+White Rabbit[a-zA-Z ]+ "([a-zA-Z0-9]{4})"')
            REGEX_WHITE_RABBIT_INV = re.compile('"([a-zA-Z0-9]{4})"[a-zA-Z ]+White Rabbit[a-zA-Z ]*')
            # REGEX_WHITE_RABBIT_ISFOOLED = re.compile('script[a-zA-Z\s]+fooled[a-zA-Z\s]+"[a-zA-Z0-9]{4}"[a-zA-Z\s]+White\sRabbit[a-zA-Z\s]+"([a-zA-Z0-9]{4})"\s')
            # REGEX_WHITE_RABBIT_FOOLED = re.compile('script[a-zA-Z\s]+fooled[a-zA-Z\s]+"[a-zA-Z0-9]{4}"[a-zA-Z\s]+White\sRabbit[a-zA-Z\s]+"([a-zA-Z0-9]{4})"\s')
            # if REGEX_WHITE_RABBIT_ISFOOLED.search(received)
            for regex in (REGEX_WHITE_RABBIT, REGEX_WHITE_RABBIT_INV):
                match = regex.search(received)
                if match:
                    break
            if match:
                goto = match.groups(0)[0]
                gotos.add(goto)
                print("\nfound:", goto, len(gotos))
                if next_is_last and False:
                    exit()
                if len(gotos) == 185:
                    next_is_last = True
                ser.write((str(goto) + '\n').encode())
                received = ''
        else:  # probably expect an input
            print('<waiting for user input>', end='', flush=True)
            userin = input()
            ser.write((userin.strip() + '\n').encode())





if __name__ == '__main__':

    write_bytes(gen_bytes(PORT_NAME), PORT_DUMP_FILE)
