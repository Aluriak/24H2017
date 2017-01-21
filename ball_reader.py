import serial

DEFAULT_OUTPUT_FILE = 'dump.txt'
DEFAULT_PORT_NAME = '/dev/ttyUSB0'


def gen_bytes(port_name=DEFAULT_PORT_NAME):

    connection = serial.Serial(port_name)  # open serial port
    print(connection.name)         # check which port was really used

    while True:

        yield connection.read()     # write a string

    connection.close()             # close port


def write_bytes(source, output_file=DEFAULT_OUTPUT_FILE):

    with open(output_file, 'wb') as output:

        [output.write(byte) for byte in source]



if __name__ == '__main__':

    write_bytes(gen_bytes(DEFAULT_PORT_NAME), DEFAULT_OUTPUT_FILE)
