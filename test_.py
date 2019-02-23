import math
import pytest
from features.Tuple import *
from features.Canvas import *
from features.Matrix import *
from features.Ray import *
from features.Sphere import *

# EQUALITY TEST
def test_equality():
    a = 0.1 + 0.2
    b = 0.3
    assert equals(a,b)
    assert not b == (0.1 + 0.2)

# TUPLES, VECTORS, POINTS
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

# COLORS
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

def test_color_to_string():
    c = Color(1,0.5,0.2)
    assert c.to_string() == "255 128 51"


# CANVAS
def test_canvas_creation():
    black = Color(0,0,0)
    c = Canvas(10,20)
    assert c.width == 10
    assert c.height == 20
    assert len(c.canvas) == c.height
    assert len(c.canvas[0]) == c.width
    for row in c.canvas:
        for p in row:
            assert p["color"] == black

def test_canvas_write():
    c = Canvas(10,20)
    red = Color(1,0,0)
    c.write_pixel(2,3,red)
    assert c.pixel_at(2,3)["color"] == red
    assert c.canvas[3][2]["color"] == red

def test_canvas_to_ppm_headers():
    c = Canvas(5,3)
    ppm = c.to_ppm()
    header = ppm.split('\n')[:3]
    assert header == ["P3","5 3","255"]

def test_canvas_to_ppm_colors():
    c = Canvas(5,3)
    c1 = Color(1.5,0,0)
    c2 = Color(0,0.5,0)
    c3 = Color(-0.5,0,1)
    c.write_pixel(0,0, c1)
    c.write_pixel(2,1,c2)
    c.write_pixel(4,2,c3)
    ppm = c.to_ppm()
    color_data = ppm.split('\n')[3:-1]
    assert color_data == [
        "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0",
        "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255"
    ]

def test_canvas_to_ppm_line_length():
    c = Canvas(10,2,Color(1,0.8,0.6))
    ppm = c.to_ppm()
    assert ppm.split('\n')[3:-1] == [
        "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204",
        "153 255 204 153 255 204 153 255 204 153 255 204 153",
        "255 204 153 255 204 153 255 204 153 255 204 153 255 204 153 255 204",
        "153 255 204 153 255 204 153 255 204 153 255 204 153"
    ]

def test_canvas_to_ppm_newline_term():
    c = Canvas(5, 3)
    ppm = c.to_ppm()
    assert ppm[-1] == '\n'

# MATRICES
def test_blank_matrix_init():
    m = Matrix(4,4)
    assert len(m) == 4
    assert len(m[0]) == 4

def test_matrix_init():
    m = Matrix(4,4,
            [[1,2,3,4],
            [5.5,6.5,7.5,8.5],
            [9,10,11,12],
            [13.5,14.5,15.5,16.5]]
        )
    assert m[0][0] == 1
    assert m[0][3] == 4
    assert m[1][0] == 5.5
    assert m[1][2] == 7.5
    assert m[2][2] == 11
    assert m[3][0] == 13.5
    assert m[3][2] == 15.5

def test_2x2_matrix():
    m = Matrix(2,2,
            [[-3,5],
            [1,-2]]
        )
    assert m[0][0] == -3
    assert m[0][1] == 5
    assert m[1][0] == 1
    assert m[1][1] == -2

def test_3x3_matrix():
    m = Matrix(3,3,
        [[-3,5,0],
        [1,-2,-7],
        [0,1,1]]
    )
    assert m[0][0] == -3
    assert m[1][1] == -2
    assert m[2][2] == 1

def test_matrix_equality():
    m = Matrix(4,4,
            [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]]
        )
    n = Matrix(4,4,
            [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]]
        )
    assert m == n

def test_matrix_inequality():
    m = Matrix(4,4,
            [[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]]
        )
    n = Matrix(4,4,
            [[5,6,7,8],
            [9,10,11,12],
            [13,14,15,16],
            [4,3,2,1]]
        )
    assert m != n

def test_matrix_multiplication():
    a = Matrix(4,4,
            [[1,2,3,4],
            [5,6,7,8],
            [9,8,7,6],
            [5,4,3,2]]
        )
    b = Matrix(4,4,
            [[-2,1,2,3],
            [3,2,1,-1],
            [4,3,6,5],
            [1,2,7,8]]
        )
    c = Matrix(4,4,
            [[20,22,50,48],
            [44,54,114,108],
            [40,58,110,102],
            [16,26,46,42]]
        )
    assert a * b == c

def test_matrix_multi_tuple():
    a = Matrix(4,4,
            [[1,2,3,4],
            [2,4,4,2],
            [8,6,4,1],
            [0,0,0,1]]
        )
    b = Tuple(1,2,3,1)
    c = Tuple(18,24,33,1)
    assert a * b == c

def test_identity_matrix():
    a = Matrix(4,4,
            [[0,1,2,4],
            [1,2,4,8],
            [2,4,8,16],
            [4,8,16,32]]
        )
    assert a * identity_matrix() == a

def test_identity_matrix_x_tuple():
    a = Tuple(1,2,3,4)
    assert identity_matrix() * a == a

def test_matrix_transpose():
    a = Matrix(4,4,
        [[0,9,3,0],
        [9,8,0,8],
        [1,8,5,3],
        [0,0,5,8]]
    )
    b = Matrix(4,4,
        [[0,9,1,0],
        [9,8,8,0],
        [3,0,5,5],
        [0,8,3,8]]
    )

    assert a.transpose() == b

def test_identity_matrix_transpose():
    a = identity_matrix().transpose()
    assert a == identity_matrix()

def test_matrix_determinant_2x2():
    a = Matrix(2,2,
        [[1,5],
        [-3,2]]
    )
    assert a.determinant == 17

def test_3x3_submatrix():
    a = Matrix(3,3,
        [[1,5,0],
        [-3,2,7],
        [0,6,-3]]
    )
    b = Matrix(2,2,
        [[-3,2],
        [0,6]]
    )
    assert a.submatrix(0,2) == b

def test_4x4_submatrix():
    a = Matrix(4,4,
        [[-6,1,1,6],
        [-8,5,8,6],
        [-1,0,8,2],
        [-7,1,-1,1]]
    )
    b = Matrix(3,3,
        [[-6,1,6],
        [-8,8,6],
        [-7,-1,1]]        
    )
    assert a.submatrix(2,1) == b

def test_3x3_minor():
    a = Matrix(3,3,
        [[3,5,0],
        [2,-1,-7],
        [6,-1,5]]
    )
    b = a.submatrix(1,0)
    assert b.determinant == 25
    assert a.minor(1,0) == 25

def test_3x3_cofactor():
    a = Matrix(3,3,
        [[3,5,0],
        [2,-1,-7],
        [6,-1,5]]
    )
    assert a.minor(0,0) == -12
    assert a.cofactor(0,0) == -12
    assert a.minor(1,0) == 25
    assert a.cofactor(1,0) == -25

def test_3x3_determinant():
    a = Matrix(3,3,
        [[1,2,6],
        [-5,8,-4],
        [2,6,4]]
    )

    assert a.cofactor(0,0) == 56
    assert a.cofactor(0,1) == 12
    assert a.cofactor(0,2) == -46
    assert a.determinant == -196

def test_4x4_determinant():
    a = Matrix(4,4,
        [[-2,-8,3,5],
        [-3,1,7,3],
        [1,2,-9,6],
        [-6,7,7,-9]]
    )

    assert a.cofactor(0,0) == 690
    assert a.cofactor(0,1) == 447
    assert a.cofactor(0,2) == 210
    assert a.cofactor(0,3) == 51
    assert a.determinant == -4071

def test_4x4_invertible():
    a = Matrix(4,4,
        [[6,4,4,4],
        [5,5,7,6],
        [4,-9,3,-7],
        [9,1,7,-6]]
    )
    assert a.determinant == -2120
    assert a.is_invertible

def test_4x4_non_invertible():
    a = Matrix(4,4,
        [[-4,2,-2,-3],
        [9,6,2,6],
        [0,-5,1,-5],
        [0,0,0,0]]
    )
    assert a.determinant == 0
    assert not a.is_invertible

def test_matrix_inversion():
    a = Matrix(4,4,
        [[-5,2,6,-8],
        [1,-5,1,8],
        [7,7,-6,-7],
        [1,-3,7,4]]
    )
    a_ = a.inverse()
    b = Matrix(4,4,
        [[0.21805,0.45113,0.24060,-0.04511],
        [-0.80827,-1.45677,-0.44361,0.52068],
        [0.07895,-0.22368,-0.05263, 0.19737],
        [-0.52256,-0.81391,-0.30075, 0.30639]]
    )

    assert a.determinant == 532
    assert a.cofactor(2,3) == -160
    assert a_[3][2] == -160/532
    assert a.cofactor(3,2) == 105
    assert a_[2][3] == 105/532
    assert a_ == b

def test_matrix_inversion_2():
    a = Matrix(4,4,
        [[8,-5,9,2],
        [7,5,6,1],
        [-6,0,9,6],
        [-3,0,-9,-4]]
    )
    b = Matrix(4,4,
        [[-0.15385,-0.15385,-0.28205,-0.53846],
        [-0.07692,0.12308,0.02564,0.03077],
        [0.35897,0.35897,0.43590,0.92308],
        [-0.69231,-0.69231,-0.76923,-1.92308]]
    )
    assert a.inverse() == b

def test_matrix_inversion_3():
    a = Matrix(4,4,
        [[9,3,0,9],
        [-5,-2,-6,-3],
        [-4,9,6,4],
        [-7,6,6,2]]
    )
    b = Matrix(4,4,
        [[-0.04074,-0.07778,0.14444,-0.22222],
        [-0.07778,0.03333,0.36667,-0.33333],
        [-0.02901,-0.14630,-0.10926,0.12963],
        [0.17778,0.06667,-0.26667,0.33333]]
    )
    assert a.inverse() == b

def test_multiply_product_by_inverse():
    a = Matrix(4,4,
        [[3,-9,7,3],
        [3,-8,2,-9],
        [-4,4,4,1],
        [-6,5,-1,1]]
    )
    b = Matrix(4,4,
        [[8,2,2,2],
        [3,-1,7,0],
        [7,0,5,4],
        [6,-2,0,5]]
    )
    c = a * b
    assert c * b.inverse() == a

# translations
def test_translation():
    transform = Translate(5,-3,2)
    p = Point(-3,4,5)
    assert transform * p == Point(2,1,7)

def test_inverse_translation():
    transform = Translate(5,-3,2)
    i = transform.inverse()
    p = Point(-3,4,5)
    assert i * p == Point(-8,7,3)
    assert p * i == Point(-8,7,3)

def test_vector_translation():
    transform = Translate(5,-3,2)
    v = Vector(-3,4,5)
    assert transform * v == v
    assert v * transform == v

def test_scale_point():
    transform = Scale(2,3,4)
    p = Point(-4,6,8)
    assert transform * p == Point(-8,18,32)

def test_scale_vector():
    transform = Scale(2,3,4)
    v = Vector(-4,6,8)
    assert transform * v == Vector(-8,18,32)

def test_inverse_scale_vector():
    transform = Scale(2,3,4)
    i = transform.inverse()
    v = Vector(-4,6,8)
    assert i * v == Vector(-2,2,2)

def test_reflect_scale():
    transform = Scale(-1,1,1)
    p = Point(2,3,4)
    assert transform * p == Point(-2,3,4)

def test_x_rotation():
    p = Point(0,1,0)
    eighth_turn = RotateX(math.pi/4)
    quarter_turn = RotateX(math.pi/2)
    assert eighth_turn * p == Point(0,math.sqrt(2)/2,math.sqrt(2)/2)
    assert quarter_turn * p == Point(0,0,1)

def test_invert_x_rotation():
    p = Point(0,1,0)
    eighth_turn = RotateX(math.pi/4)
    i = eighth_turn.inverse()
    assert i * p == Point(0,math.sqrt(2)/2,-math.sqrt(2)/2)

def test_y_rotation():
    p = Point(0,0,1)
    eighth_turn = RotateY(math.pi/4)
    quarter_turn = RotateY(math.pi/2)
    assert eighth_turn * p == Point(math.sqrt(2)/2,0,math.sqrt(2)/2)
    assert quarter_turn * p == Point(1,0,0)

def test_z_rotation():
    p = Point(0,1,0)
    eighth_turn = RotateZ(math.pi/4)
    quarter_turn = RotateZ(math.pi/2)
    assert eighth_turn * p == Point(-math.sqrt(2)/2,math.sqrt(2)/2,0)
    assert quarter_turn * p == Point(-1,0,0)

def test_shear_XY():
    transform = Shear(1,0,0,0,0,0)
    p = Point(2,3,4)
    assert transform * p == Point(5,3,4)

def test_shear_XZ():
    transform = Shear(0,1,0,0,0,0)
    p = Point(2,3,4)
    assert transform * p == Point(6,3,4)

def test_shear_YX():
    transform = Shear(0,0,1,0,0,0)
    p = Point(2,3,4)
    assert transform * p == Point(2,5,4)

def test_shear_YZ():
    transform = Shear(0,0,0,1,0,0)
    p = Point(2,3,4)
    assert transform * p == Point(2,7,4)

def test_shear_ZX():
    transform = Shear(0,0,0,0,1,0)
    p = Point(2,3,4)
    assert transform * p == Point(2,3,6)

def test_shear_ZY():
    transform = Shear(0,0,0,0,0,1)
    p = Point(2,3,4)
    assert transform * p == Point(2,3,7)

def test_transform_sequences():
    p = Point(1,0,1)
    a = RotateX(math.pi/2)
    b = Scale(5,5,5)
    c = Translate(10,5,7)
    
    p2 = a * p
    assert p2 == Point(1,-1,0)

    p3 = b * p2
    assert p3 == Point(5,-5,0)

    p4 = c * p3
    assert p4 == Point(15,0,7)

def test_transform_chaining():
    p = Point(1,0,1)
    a = RotateX(math.pi/2)
    b = Scale(5,5,5)
    c = Translate(10,5,7)
    
    t = c * b * a
    assert t * p == Point(15,0,7)

# RAY TRACING!!
def test_create_ray():
    origin = Point(1,2,3)
    direction = Vector(4,5,6)
    r = Ray(origin, direction)
    assert r.origin == origin
    assert r.direction == direction

def test_distance_along_ray():
    r = Ray(Point(2,3,4), Vector(1,0,0))
    assert r.position(0) == Point(2,3,4)
    assert r.position(1) == Point(3,3,4)
    assert r.position(-1) == Point(1,3,4)
    assert r.position(2.5) == Point(4.5,3,4)

def test_ray_sphere_intersection():
    r = Ray(Point(0,0,-5),Vector(0,0,1))
    s = Sphere()
    xs = r.intersect(s)
    assert len(xs) == 2
    assert xs[0].t == 4.0
    assert xs[1].t == 6.0

def test_ray_sphere_tangent_intersection():
    r = Ray(Point(0,1,-5),Vector(0,0,1))
    s = Sphere()
    xs = r.intersect(s)
    assert len(xs) == 2
    assert xs[0].t == 5.0
    assert xs[1].t == 5.0

def test_ray_non_intersection():
    r = Ray(Point(0,2,-5),Vector(0,0,1))
    s = Sphere()
    xs = r.intersect(s)
    assert len(xs) == 0

def test_ray_inside_sphere():
    r = Ray(Point(0,0,0),Vector(0,0,1))
    s = Sphere()
    xs = r.intersect(s)
    assert len(xs) == 2
    assert xs[0].t == -1.0
    assert xs[1].t == 1.0

def test_ray_negative_intersection():
    r = Ray(Point(0,0,5),Vector(0,0,1))
    s = Sphere()
    xs = r.intersect(s)
    assert len(xs) == 2
    assert xs[0].t == -6.0
    assert xs[1].t == -4.0

def test_intersection_class():
    s = Sphere()
    i = Intersection(3.5,s)
    assert i.t == 3.5
    assert i.object == s

def test_intersections_class():
    s = Sphere()
    i1 = Intersection(1,s)
    i2 = Intersection(2,s)
    xs = Intersections([i1,i2])
    assert len(xs) == 2
    assert xs[0].t == 1
    assert xs[1].t == 2

def test_intersection_sets_object():
    r = Ray(Point(0,0,-5),Vector(0,0,1))
    s = Sphere()
    xs = r.intersect(s)
    assert len(xs) == 2
    assert xs[0].object == s
    assert xs[1].object == s

def test_get_hit_from_intersections():
    s = Sphere()
    i1 = Intersection(1,s)
    i2 = Intersection(2,s)
    xs = Intersections([i2,i1])
    i = xs.hit()
    assert i == i1

def test_get_hit_from_ints_w_neg():
    s = Sphere()
    i1 = Intersection(-1,s)
    i2 = Intersection(1,s)
    xs = Intersections([i2,i1])
    i = xs.hit()
    assert i == i2

def test_hit_from_all_neg_t():
    s = Sphere()
    i1 = Intersection(-2,s)
    i2 = Intersection(-1,s)
    xs = Intersections([i2,i1])
    i = xs.hit()
    assert not i

def test_hit_lowest_nonneg():
    s = Sphere()
    i1 = Intersection(5,s)
    i2 = Intersection(7,s)
    i3 = Intersection(-3,s)
    i4 = Intersection(2,s)
    xs = Intersections([i1,i2,i3,i4])
    i = xs.hit()
    assert i == i4

def test_ray_translation():
    r = Ray(Point(1,2,3),Vector(0,1,0))
    m = Translate(3,4,5)
    r2 = r.transform(m)
    assert r2.origin == Point(4,6,8)
    assert r2.direction == Vector(0,1,0)

def test_ray_scale():
    r = Ray(Point(1,2,3),Vector(0,1,0))
    m = Scale(2,3,4)
    r2 = r.transform(m)
    assert r2.origin == Point(2,6,12)
    assert r2.direction == Vector(0,3,0)

def test_sphere_default_transform():
    s = Sphere()
    assert s.transform == identity_matrix()

def test_sphere_transformation():
    s = Sphere()
    t = Translate(2,3,4)
    s.transform = t
    assert s.transform == t

def test_intersect_scaled_sphere():
    r = Ray(Point(0,0,-5),Vector(0,0,1))
    s = Sphere()
    s.transform = Scale(2,2,2)
    xs = r.intersect(s)
    assert len(xs) == 2
    assert xs[0].t == 3
    assert xs[1].t == 7

def test_intersect_translated_sphere():
    r = Ray(Point(0,0,-5),Vector(0,0,1))
    s = Sphere()
    s.transform = Translate(5,0,0)
    xs = r.intersect(s)
    assert len(xs) == 0

# compute normals
def test_x_axis_sphere_normal():
    s = Sphere()
    n = s.normal(Point(1,0,0))
    assert n == Vector(1,0,0)

def test_y_axis_sphere_normal():
    s = Sphere()
    n = s.normal(Point(0,1,0))
    assert n == Vector(0,1,0)

def test_z_axis_sphere_normal():
    s = Sphere()
    n = s.normal(Point(0,0,1))
    assert n == Vector(0,0,1)

def test_non_axial_sphere_normal():
    p = math.sqrt(3)/3
    s = Sphere()
    n = s.normal(Point(p,p,p))
    assert n == Vector(p,p,p)

def test_normal_is_normalized():
    p = math.sqrt(3)/3
    s = Sphere()
    n = s.normal(Point(p,p,p))
    assert n == n.normalize()

def test_normal_of_translated_sphere():
    s = Sphere()
    s.transform = Translate(0,1,0)
    n = s.normal(Point(0,1.70711,-0.70711))
    assert n == Vector(0,0.70711,-0.70711)

def test_normal_of_transformed_sphere():
    s = Sphere()
    m = Scale(1,0.5,1) * RotateZ(math.pi/5)
    s.transform = m
    n = s.normal(Point(0,math.sqrt(2)/2,-math.sqrt(2)/2))
    assert n == Vector(0,0.97014,-0.24254)