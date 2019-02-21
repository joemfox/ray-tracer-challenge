import math
from features.Tuple import Point, Vector

class Ray():
    def __init__(self,origin,direction):
        assert isinstance(origin,Point), "Origin must be Point"
        assert isinstance(direction,Vector), "Direction must be Vector"
        self.origin = Point(*origin.coords[:3])
        self.direction = Vector(*direction.coords[:3])

    def position(self,t):
        return self.origin + self.direction * t
    
    def intersect(self, obj):
        sphere_to_ray = self.origin - Point(0,0,0)
        a = self.direction.dot(self.direction)
        b = 2 * self.direction.dot(sphere_to_ray)
        c = sphere_to_ray.dot(sphere_to_ray) - 1
        discriminant = math.pow(b,2) - (4 * a * c)
        if discriminant < 0:
            return list()
        else:        
            t1 = (-b - math.sqrt(discriminant)) / (2 * a)
            t2 = (-b + math.sqrt(discriminant)) / (2 * a)

            return [t1,t2]
    