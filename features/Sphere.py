from features.Tuple import Point
from features.Matrix import identity_matrix

class Sphere():
    def __init__(self):
        self.position = Point(0,0,0)
        self.transform = identity_matrix()