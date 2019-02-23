from features.Tuple import Color
from features.util import equals
import math

class Material():
    def __init__(self):
        self.color = Color(1,1,1)
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200.0
    
    def __eq__(self,t):
        if isinstance(t,Material):
            return (
                self.color == t.color
                and equals(self.ambient,t.ambient)
                and equals(self.diffuse,t.diffuse)
                and equals(self.specular,t.specular)
                and equals(self.shininess,t.shininess)
                )
        else: return False
    
    def compute_lighting(self,l,p,e,n):
        effective_color = self.color * l.intensity
        lightv = (l.position - p).normalize()
        ambient = effective_color * self.ambient

        light_dot_normal = lightv.dot(n)
        if light_dot_normal < 0:
            diffuse = Color(0,0,0)
            specular = Color(0,0,0)
        else:
            diffuse = effective_color * self.diffuse * light_dot_normal
            reflectv = -lightv.reflect(e)
            reflect_dot_eye = reflectv.dot(e)

            if reflect_dot_eye <= 0:
                specular = Color(0,0,0)
            else:
                factor = math.pow(reflect_dot_eye,self.shininess)
                specular = l.intensity * self.specular * factor
        
        return ambient + diffuse + specular