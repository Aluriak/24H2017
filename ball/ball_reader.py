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
                        write_timeout=0.5)
    print('Connection:', ser)
    ser.write(b'\r\n')

    received = ''
    sent = False
    print('InWaiting:', ser.in_waiting)
    while True:
        new_char = ser.read(1).decode()
        if new_char:  # have something to say
            received += new_char
            print(new_char, end='', flush=True)

            match = REGEX_4TIMES8.search(received)
            if match and not sent:
                sent = True
                first, second = match.groups(0)
                res = int(first) * int(second)
                ser.write((str(res) + '\n').encode())
                # print("\nfound {} × {} -> {}".format(first, second, res))
        else:  # probably expect an input
            print('<waiting for user input>')
            userin = input()
            ser.write((userin.strip() + '\r\n').encode())





if __name__ == '__main__':

    write_bytes(gen_bytes(PORT_NAME), PORT_DUMP_FILE)
