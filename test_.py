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
    assert isinstance(a, Tuple), "should be instance of Tuple"
    assert a.x == 4.0
    assert a.y == -4.0
    assert a.z == 3.0
    assert a.w == 1.0
    assert a.is_point()
    assert not a.is_vector()

def test_vector_creation():
    a = Vector(4, -4, 3)
    assert isinstance(a, Tuple), "should be instance of Tuple"
    assert a.x == 4.0
    assert a.y == -4.0
    assert a.z == 3.0
    assert a.w == 0.0
    assert a.is_vector()
    assert not a.is_point()