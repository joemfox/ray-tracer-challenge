from features.Tuple import Point, Vector
from features.Matrix import identity_matrix

class Sphere():
    def __init__(self):
        self.position = Point(0,0,0)
        self.transform = identity_matrix()
    
    def normal(self,p):
        obj_p = self.transform.inverse() * p
        obj_n = obj_p - Point(0,0,0)
        
        n = self.transform.submatrix(3,3).inverse().transpose() * obj_n
        return n.normalize()
