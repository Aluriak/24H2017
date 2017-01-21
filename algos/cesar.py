"""Enigm about ROT13

"""

import codecs


def rot13(string):
    return codecs.encode(string, 'rot13')

def run(payload):
    assert isinstance(payload, str)
    return rot13(payload)
