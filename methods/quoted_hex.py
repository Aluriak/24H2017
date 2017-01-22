
import re


def quoted_hex(data):
    regex = re.compile(r'"([^"]+)"')
    matches = []
    for match in regex.findall(data):
        print(match)
        matches.append(match)
    return ''.join(m.encode().hex() for m in matches).upper()


