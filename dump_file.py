from defaults import PORT_DUMP_FILE

def main():


    with open(PORT_DUMP_FILE, 'rb') as fd:


        next(fd)
        yield next(fd)
        yield next(fd)
        yield next(fd)


if __name__ == "__main__":

    with open('coucou.txt', 'wb') as fd:
        for elem in main():
            fd.write(elem)
