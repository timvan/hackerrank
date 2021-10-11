import math


def addNumbers(a: float, b: float) -> int:
    return int(math.floor(a + b))


def test_addNumbers():
    assert addNumbers(2.3, 1.9) == 4
    assert addNumbers(0.1, 1.9) == 2
    assert addNumbers(0.0000001, 1.9) == 1
    assert addNumbers(-0.0000001, 1.9) == 1
