import math
from features.Tuple import Point, Vector
from features.Intersection import *

class Ray():
    def __init__(self,origin,direction):
        assert origin.is_point, "Origin must be Point"
        assert direction.is_vector, "Direction must be Vector"
        self.origin = Point(*origin.coords[:3])
        self.direction = Vector(*direction.coords[:3])

    def position(self,t):
        return self.origin + self.direction * t
    
    def intersect(self, obj):
        r = self.transform(obj.transform.inverse())
        
        sphere_to_ray = r.origin - Point(0,0,0)
        a = r.direction.dot(r.direction)
        b = 2 * r.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1
        discriminant = math.pow(b,2) - (4 * a * c)
        if discriminant < 0:
            return list()
        else:        
            t1 = Intersection((-b - math.sqrt(discriminant)) / (2 * a),obj)
            t2 = Intersection((-b + math.sqrt(discriminant)) / (2 * a),obj)

            return Intersections([t1,t2])
    
    def transform(self,transformation):
        o = transformation * self.origin
        d = transformation * self.direction
        r = Ray(o,d)
        return r
    