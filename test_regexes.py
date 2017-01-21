

from defaults import REGEX_4TIMES8


def test_times():
    match = REGEX_4TIMES8.search('\ncoucou\n80 times34   ?\ncoucou')
    first, second = match.groups(0)
    assert int(first) * int(second) == 2720
