import math
import pytest
from features.Tuple import Tuple, Point, Vector, Color

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

def test_tuple_multiplication():
    a = Tuple(1, -2, 3, -4)
    b = Tuple(3.5, -7, 10.5, -14)
    c = Tuple(0.5, -1, 1.5, -2)
    assert a * 3.5 == b
    assert a * 0.5 == c

def test_tuple_division():
    a = Tuple(1, -2, 3, -4)
    b = Tuple(0.5, -1, 1.5, -2)
    assert a / 2 == b

def test_vector_get_magnitude():
    a = Vector(1, 0, 0)
    assert a.magnitude() == 1
    b = Vector(0, 1, 0)
    assert b.magnitude() == 1
    c = Vector(0, 0, 1)
    assert c.magnitude() == 1
    d = Vector(1, 2, 3)
    assert d.magnitude() == math.sqrt(14)
    e = Vector(-1, -2, -3)
    assert e.magnitude() == math.sqrt(14)

def test_vector_normalization():
    a = Vector(4, 0, 0)
    a_ = a.normalize()
    assert a_ == Vector(1, 0, 0)
    assert a_.magnitude() == 1
    b = Vector(1, 2, 3)
    b_ = b.normalize()
    assert b_ == Vector(0.26726, 0.53452, 0.80178)
    assert b_.magnitude() == 1

def test_vector_dot_product():
    a = Vector(1, 2, 3)
    b = Vector(2, 3, 4)
    assert a.dot(b) == 20
    assert b.dot(a) == 20

def test_vector_cross_product():
    a = Vector(1, 2, 3)
    b = Vector(2, 3, 4)
    assert a.cross(b) == Vector(-1, 2, -1)
    assert b.cross(a) == Vector(1, -2, 1)

def test_color_tuple():
    c = Color(-0.5, 0.4, 1.7)
    assert c.red == -0.5
    assert c.green == 0.4
    assert c.blue == 1.7

def test_color_addition():
    c1 = Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)
    c3 = Color(1.6, 0.7, 1.0)
    assert c1 + c2 == c3

def test_color_subtraction():
    c1 = Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)
    c3 = Color(0.2, 0.5, 0.5)
    assert c1 - c2 == c3

def test_color_scalar_multiplication():
    c = Color(0.2, 0.3, 0.4)
    c2 = Color(0.4, 0.6, 0.8)
    assert c * 2 == c2

def test_color_color_multiplication():
    c1 = Color(1, 0.2, 0.4)
    c2 = Color(0.9, 1, 0.1)
    c3 = Color(0.9, 0.2, 0.04)
    assert c1 * c2 == c3