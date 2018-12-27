import math
from features.util import equals

class Tuple:
    def __init__(self, x, y, z, w):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)
        self.coords = [self.x,self.y,self.z,self.w]
    
    def is_point(self):
        return equals(self.w, 1.0)

    def is_vector(self):
        return equals(self.w, 0.0)

    def __eq__(self, t):
        a = self.coords
        b = t.coords
        equal_flag = True
        if len(a) == len(b):
            for i in range(len(a)):
                if not equals(a[i],b[i]):
                    equal_flag = False
        return equal_flag

    def __add__(self, t):
        x = self.x + t.x
        y = self.y + t.y
        z = self.z + t.z
        w = self.w + t.w
        return Tuple(x, y, z, w)

    def __sub__(self, t):
        x = self.x - t.x
        y = self.y - t.y
        z = self.z - t.z
        w = self.w - t.w
        return Tuple(x, y, z, w)

    def __neg__(self):
        assert self.is_vector(), "Unary negation operator only works on vectors, not points."
        zero = Vector(0,0,0)
        return zero - self
    
    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        z = self.z * scalar
        w = self.w * scalar
        return Tuple(x, y, z, w)
    
    def __truediv__(self, scalar):
        x = self.x / scalar
        y = self.y / scalar
        z = self.z / scalar
        w = self.w / scalar
        return Tuple(x, y, z, w)

class Point(Tuple):
    def __init__(self, x, y, z):
        Tuple.__init__(self,x,y,z,1.0)

class Vector(Tuple):
    def __init__(self, x, y, z):
        Tuple.__init__(self,x,y,z,0.0)

    def magnitude(self):
        return math.sqrt(
            self.x ** 2 +
            self.y ** 2 +
            self.z ** 2 +
            self.w ** 2
        )