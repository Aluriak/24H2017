

from methods import quoted_hex

def test_example():
    assert quoted_hex.quoted_hex('This is "a" sentence with some "quoted" text') == '6171756F746564'
