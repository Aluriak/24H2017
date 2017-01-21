import serial
from defaults import PORT_DUMP_FILE, PORT_NAME


def gen_bytes(port_name):

    connection = serial.Serial(port_name)  # open serial port
    print(connection.name)         # check which port was really used

    while True:

        yield connection.read()     # write a string

    connection.close()             # close port


def write_bytes(source, output_file):

    source = iter(source)
    with open(output_file, 'wb') as output:
        output.write(next(gen_bytes()))


if __name__ == '__main__':

    write_bytes(gen_bytes(PORT_NAME), PORT_DUMP_FILE)
