from features.Tuple import Point

class Light():
    def __init__(self,p,i):
        self.position = p
        self.intensity = i

class Point_Light(Light):
    def __init__(self,p,i):
        Light.__init__(self,p,i)