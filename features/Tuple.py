class Tuple:
    def __init__(self, x, y, z, w):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)
    
    def is_point(self):
        return self.w == 1.0

    def is_vector(self):
        return self.w == 0.0

class Point(Tuple):
    def __init__(self, x, y, z):
        Tuple.__init__(self,x,y,z,1.0)

class Vector(Tuple):
    def __init__(self, x, y, z):
        Tuple.__init__(self,x,y,z,0.0)

