
from methods import matching


def test_basic():

    in_ = '([])({})'
    assert matching.iscorrect(in_)
    assert not matching.iscorrect(in_ + '(')


def test_fixer():
    in_ = '([)({})'
    assert matching.iscorrect(matching.fix_matchs(in_))

