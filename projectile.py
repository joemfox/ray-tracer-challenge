from features.Tuple import Tuple, Vector, Point, Color
from features.Canvas import Canvas
from features.util import equals

class Projectile:
    def __init__(self, position, velocity):
        assert position.is_point()
        assert velocity.is_vector()
        self.position = position
        self.velocity = velocity

class Environment:
    def __init__(self, gravity, wind):
        assert gravity.is_vector()
        assert wind.is_vector()
        self.gravity = gravity
        self.wind = wind

def tick(env, proj):
    p = proj.position + proj.velocity
    v = proj.velocity + env.gravity + env.wind
    return Projectile(p, v)

if __name__ == '__main__':
    height = 200
    width = 400
    c = Canvas(width,height)

    p_start = Point(0, 1, 0)
    v_start = Vector(2, 2, .3).normalize() * 6.5

    grav_start = Vector(0, -0.1, 0)
    wind_start = Vector(-0.01, 0, 0)
    p = Projectile(p_start, v_start)
    e = Environment(grav_start, wind_start)
    
    print(f"x:{p.position.x},y:{p.position.y},z:{p.position.z}")
    while p.position.y > 0:
        p = tick(e, p)
        print(f"x:{p.position.x},y:{p.position.y},z:{p.position.z}")
        c.write_pixel(p.position.x,height - p.position.y,Color(1*p.position.y/height+.25,1*p.position.x/width,0))

    c.to_ppm("output/projectile.ppm")
