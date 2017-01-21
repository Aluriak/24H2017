from bitstring import BitArray
from itertools import zip_longest


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def convert_to_bool(bit):
    assert bit in '01'
    return bit == '1'


if __name__ == '__main__':
    with open('data/mini_dump.txt', 'rb') as infd:

        key = infd.readline()
        key_b = BitArray(key).bin
        assert infd.readline().decode('utf8').strip() == '24hc17'
        line = infd.readline()
        line_b = BitArray(line).bin
        xor_line = ''
        # print(BitArray(key).bin)
        # print(BitArray(line).bin)
        for group in grouper(line_b, len(key_b)):
            if None in group:
                print("Padding : ", group)
                break
            for bkey, bline in zip(key_b, group):
                if convert_to_bool(bkey) != convert_to_bool(bline):
                    xor_line += '1'
                else:
                    xor_line += '0'

        char_line = ''
        for group in grouper(xor_line, 8):
            t = int("".join(group))
            char_line += chr(t)

        print(char_line)
