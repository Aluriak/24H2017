

import pytest
from algos import cesar


def test_rot13():
    assert cesar.rot13('foobar') == 'sbbone'
    assert cesar.rot13(cesar.rot13('foobar')) == 'foobar'


def test_run():
    payload = 'coucou les copaings'
    assert cesar.run(payload) == 'pbhpbh yrf pbcnvatf'
