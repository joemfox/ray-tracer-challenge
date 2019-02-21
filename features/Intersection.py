class Intersection():
    def __init__(self,t,object):
        self.t = t 
        self.object = object

class Intersections(list):
    def __init__(self,i):
        self += i
    
    def hit(self):
        hit = None
        pos = list(filter(lambda x: x.t >= 0,self))
        if len(pos):
            hit = min(pos,key=lambda x:x.t)
        return hit