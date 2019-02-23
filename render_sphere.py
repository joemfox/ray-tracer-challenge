from features.Canvas import Canvas
from features.Ray import Ray
from features.Sphere import Sphere
from features.Matrix import Translate,Scale, Shear
from features.Tuple import Color, Point, Vector

if __name__ == '__main__':
    canvas_size = 100
    wall_size = 10
    pix_size = wall_size/canvas_size
    half = wall_size/2
    wall_z = 10

    c = Canvas(canvas_size,canvas_size)
    s = Sphere()
    s.transform = Shear(0.5,0,0,0,0,0) * Scale(0.5,1,1)
    origin = Point(0,0,-5)
    for y in range(canvas_size):
        world_y = half - pix_size * y
        for x in range(canvas_size):
            world_x = -half + pix_size * x
            pixel = Point(world_x,world_y,wall_z)
            direction =  pixel - origin
            direction = direction.normalize()
            r = Ray(origin,direction)
            i = r.intersect(s)
            if i.hit():
                c.write_pixel(x,y,Color(1,0,0))
    c.to_ppm('output/sphere_render.ppm')