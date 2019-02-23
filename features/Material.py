from features.Tuple import Color
from features.util import equals

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