

from algos import reverse_animals as ra

def test_run():
    in_ = "cheval\nkoala"
    out = "koala\ncheval"
    assert ra.run(in_) == out


