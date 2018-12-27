import pytest
from features.Tuple import Tuple, Point, Vector

EPSILON = 0.00001

def equals(a,b):
    return abs(a - b) < EPSILON

def test_equality():
    a = 0.1 + 0.2
    b = 0.3
    assert equals(a,b)
    assert not b == (0.1 + 0.2)

def test_tuple_point_assignment():
    a = Tuple(4.3, -4.2, 3.1 ,1.0)
    assert a.x == 4.3
    assert a.y == -4.2
    assert a.z == 3.1
    assert a.w == 1.0
    assert a.is_point()
    assert not a.is_vector()

def test_tuple_vector_assignment():
    a = Tuple(4.3, -4.2, 3.1, 0.0)
    assert a.x == 4.3
    assert a.y == -4.2
    assert a.z == 3.1
    assert a.w == 0.0
    assert a.is_vector()
    assert not a.is_point()

def test_point_creation():
    a = Point(4, -4, 3)
    assert isinstance(a, Tuple), "Point should be instance of Tuple"
    assert a.x == 4.0
    assert a.y == -4.0
    assert a.z == 3.0
    assert a.w == 1.0
    assert a.is_point()
    assert not a.is_vector()

def test_vector_creation():
    a = Vector(4, -4, 3)
    assert isinstance(a, Tuple), "Vector should be instance of Tuple"
    assert a.x == 4.0
    assert a.y == -4.0
    assert a.z == 3.0
    assert a.w == 0.0
    assert a.is_vector()
    assert not a.is_point()

def test_tuples_are_equal():
    a = Vector(4, -4, 3)
    b = Point(4, -4, 3)
    c = Tuple(4, -4, 3, 0)
    d = Tuple(4, -4, 3, 1)
    assert a == (c)
    assert not a == (b)
    assert b == (d)
    assert not b == (c)

def test_tuple_addition():
    a = Tuple(3, -2, 5, 1)
    b = Tuple(-2, 3, 1, 0)
    c = Tuple(1, 1, 6, 1)
    d = a + b
    assert d == c, "tuple addition should produce new tuple"
    assert d.is_point()

def test_point_subtraction():
    a = Point(3, 2, 1)
    b = Point(5, 6, 7)
    c = Vector(-2, -4, -6)
    d = a - b
    assert d == c
    assert d.is_vector()

def test_point_vector_subtraction():
    a = Point(3, 2, 1)
    b = Vector(5, 6, 7)
    c = Point(-2, -4, -6)
    d = a - b
    assert d == c
    assert d.is_point()

def test_vector_vector_subtraction():
    a = Vector(3, 2, 1)
    b = Vector(5, 6, 7)
    c = Vector(-2, -4, -6)
    d = a - b
    assert d == c
    assert d.is_vector()

def test_vector_negation():
    a = Vector(1, -2, 3)
    b = Vector(-1, 2, -3)
    assert -a == b

def test_point_negation_exception():
    a = Point(1, 2, 3)
    with pytest.raises(Exception):
        -a