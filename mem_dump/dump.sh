esptool.py --port /dev/ttyUSB0 --baud 230400 read_flash 0x00000 0x400000 wemos-original.bin
strings wemos-original.bin >> string_dump.txt
