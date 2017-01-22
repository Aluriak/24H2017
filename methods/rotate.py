


def run(payload):
    lines = payload.strip().splitlines()
    matrice = dict()
    for nol, line in enumerate(lines):
        for idx, char in enumerate(line):
            matrice[nol, idx] = char  # d'assaut  (parce qu'il est un peu 8 heure. Et fuck la PEP8)
    MAX_X = nol
    MAX_Y = idx

    out = ''
    for idx in range(MAX_Y+1):
        for nol in reversed(range(MAX_X+1)):
            out += matrice[nol, idx]
        out += '\n'
    return out


