from features.util import equals

class Tuple:
    def __init__(self, x, y, z, w):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.w = float(w)
        self.coords = [self.x,self.y,self.z,self.w]
    
    def is_point(self):
        return self.w == 1.0

    def is_vector(self):
        return self.w == 0.0

    def is_equal(self, t):
        a = self.coords
        b = t.coords
        equal_flag = True
        if len(a) == len(b):
            for i in range(len(a)):
                if not equals(a[i],b[i]):
                    equal_flag = False
        return equal_flag

class Point(Tuple):
    def __init__(self, x, y, z):
        Tuple.__init__(self,x,y,z,1.0)

class Vector(Tuple):
    def __init__(self, x, y, z):
        Tuple.__init__(self,x,y,z,0.0)
