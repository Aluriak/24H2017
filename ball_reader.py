import serial
from defaults import PORT_DUMP_FILE, PORT_NAME


def gen_bytes(port_name):

    connection = serial.Serial(port_name, baudrate=230400, bytesize=serial.EIGHTBITS)  # open serial port
    print(connection.name)         # check which port was really used

    while True:

        yield connection.read()     # write a string

    connection.close()             # close port


def write_bytes(source, output_file):

    with open(output_file, 'wb') as output:

        [output.write(byte) for byte in source]


def vitellius_dial():

    ser = serial.Serial(PORT_NAME, baudrate=230400, bytesize=serial.EIGHTBITS)

    out = ''
    while ser.inWaiting() > 0:
        out += ser.read(1)

        if out != '':
            print (">>", out)



#    ser.write(b'\r\n')



if __name__ == '__main__':

    write_bytes(gen_bytes(PORT_NAME), PORT_DUMP_FILE)
