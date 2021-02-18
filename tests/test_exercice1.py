from exercices.exercice1 import *

def test_fibo():
    assert fibo(1) == 1
    assert fibo(2) == 1
    assert fibo(25) == 75025
    assert fibo(45) == 1134903170
