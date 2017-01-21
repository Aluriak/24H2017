
from methods import suite_croissante as sc


def test_first_decroissant():

    assert sc.first_decroissant([1, 2, 3, 2, 4]) == 2




def test_run():

    assert sc.run('-189 -100 -50 -60 0') == -60

