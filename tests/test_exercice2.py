from exercices.exercice2 import *

liste_eleves = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
liste_notes = [1, 40, 80, 60, 58, 80, 75, 80, 60, 24]

def test_meilleures_notes():
    assert meilleures_notes() == (80, 3, ['c', 'f', 'h'])
