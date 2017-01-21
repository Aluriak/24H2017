

from algos import reverse_text as rt


def test_run():
    assert rt.run('abc def') == 'fed cba'
