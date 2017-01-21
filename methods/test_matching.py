
from methods import matching


def test_closerof():
    assert matching.closerof('(') == ')'
    assert matching.closerof('[') == ']'
    assert matching.closerof('{') == '}'
    assert matching.closerof('<') == '>'

def test_basic():

    in_ = '([])({})'
    assert matching.iscorrect(in_)
    assert not matching.iscorrect(in_ + '(')

def test_correct_false():
    in_ = '([]}({})'
    assert not matching.iscorrect(in_)


def test_fixer():
    in_ = '([{}'
    assert matching.iscorrect(in_ + matching.close_all(in_))

