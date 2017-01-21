import re
import serial
from defaults import PORT_DUMP_FILE, PORT_NAME, BAUD_RATE


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

    REGEX_4TIMES8 = re.compile('([0-9]+)\s*times?\s*([0-9]+)\s*\?')
    ser = serial.Serial(PORT_NAME, baudrate=BAUD_RATE, bytesize=serial.EIGHTBITS,
                        write_timeout=10)
    print('Connection:', ser)
    ser.write(b'\r\n')

    received = ''
    print('InWaiting:', ser.in_waiting)
    while True:
        received += ser.read(1).decode()
        # print('LOOP')

        if received[-1] in b'\n\r\f':
            print(">>", received)

        match = REGEX_4TIMES8.match(received)
        if match:
            first, second = match.groups(0)
            res = int(first) * int(second)
            ser.write(str(res).encode())
            print("found {} × {} -> {}".format(first, second, res))



#    ser.write(b'\r\n')



if __name__ == '__main__':

    write_bytes(gen_bytes(PORT_NAME), PORT_DUMP_FILE)
