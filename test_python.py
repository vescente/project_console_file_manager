import pytest
import math

def test_filter():
    assert list(filter(lambda x: x > 0, [-1, 0, 1, 2])) == [1, 2]
    assert list(filter(lambda x: x % 2 == 0, range(10))) == [0, 2, 4, 6, 8]

def test_map():
    assert list(map(lambda x: x * 2, [1, 2, 3])) == [2, 4, 6]
    assert list(map(str, [1, 2, 3])) == ['1', '2', '3']

def test_sorted():
    assert sorted([3, 1, 2]) == [1, 2, 3]
    assert sorted(['b', 'a', 'c']) == ['a', 'b', 'c']
    assert sorted([3, 1, 2], reverse=True) == [3, 2, 1]

def test_pi():
    assert math.isclose(math.pi, 3.141592653589793)

def test_sqrt():
    assert math.sqrt(4) == 2
    assert math.sqrt(9) == 3
    assert math.isclose(math.sqrt(2), 1.4142135623730951)

def test_pow():
    assert math.pow(2, 3) == 8
    assert math.pow(3, 2) == 9
    assert math.isclose(math.pow(2, 0.5), 1.4142135623730951)

def test_hypot():
    assert math.hypot(3, 4) == 5
    assert math.hypot(5, 12) == 13
    assert math.isclose(math.hypot(1, 1), 1.4142135623730951)
