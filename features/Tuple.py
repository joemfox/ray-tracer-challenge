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
        return equals(self.w, 0.0) and not isinstance(self, Color)

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
        if isinstance(self,Color):
            return Color(x,y,z)
        elif w == 0:
            return Vector(x, y, z)
        elif w == 1:
            return Point(x,y,z)

    def __sub__(self, t):
        x = self.x - t.x
        y = self.y - t.y
        z = self.z - t.z
        w = self.w - t.w
        if isinstance(self,Color):
            return Color(x,y,z)
        elif w == 0:
            return Vector(x, y, z)
        elif w == 1:
            return Point(x,y,z)

    def __neg__(self):
        assert self.is_vector(), "Unary negation operator only works on vectors, not points."
        zero = Vector(0,0,0)
        return zero - self
    
    def __mul__(self, other):
        if isinstance(other, Tuple):
            x = self.x * other.x
            y = self.y * other.y
            z = self.z * other.z
            w = self.w * other.w
            return type(self)(x, y, z, w)
        elif isinstance(other,float) or isinstance(other,int):
            coords = [c * other for c in self.coords]
            return Tuple(*coords)
        else:
            return other * self
    
    def __truediv__(self, scalar):
        coords = [c / scalar for c in self.coords]
        return Tuple(*coords)

class Point(Tuple):
    def __init__(self, x, y, z, w = 1.0):
        Tuple.__init__(self,x,y,z,w)

class Vector(Tuple):
    def __init__(self, x, y, z, w = 0.0):
        Tuple.__init__(self,x,y,z,w)

    def magnitude(self):
        coords = [c ** 2 for c in self.coords]
        return math.sqrt(sum(coords))
    
    def normalize(self):
        mag = self.magnitude()
        coords = [c/mag for c in self.coords]
        return Vector(*coords)

    def dot(self, t):
        x = self.x * t.x
        y = self.y * t.y
        z = self.z * t.z
        w = self.w * t.w
        return sum([x, y, z, w])

    def cross(self, t):
        x = self.y * t.z - self.z * t.y
        y = self.z * t.x - self.x * t.z
        z = self.x * t.y - self.y * t.x
        return Vector(x, y, z)

    def reflect(self,normal):
        return self - normal * 2 * self.dot(normal)

class Color(Tuple):
    def __init__(self, r, g, b, w = 0.0):
        Tuple.__init__(self, r, g, b, w)

    def __mul__(self, other):
        if isinstance(other, Color):
            x = self.x * other.x
            y = self.y * other.y
            z = self.z * other.z
            w = self.w * other.w
            return type(self)(x, y, z, 0)
        elif isinstance(other,float) or isinstance(other,int):
            coords = [c * other for c in self.coords]
            return Color(*coords)

    def get_red(self):
        return self.x

    def get_green(self):
        return self.y

    def get_blue(self):
        return self.z

    def to_string(self):
        rgb = []
        for c in [self.x,self.y,self.z]:
            rgb.append(str(max(0,min(round(c*255),255))))
        return " ".join(rgb)

    red = property(get_red)
    green = property(get_green)
    blue = property(get_blue)