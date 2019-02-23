from features.Canvas import Canvas
from features.Ray import Ray
from features.Sphere import Sphere
from features.Matrix import Translate,Scale, Shear
from features.Tuple import Color, Point, Vector
from features.Material import Material
from features.Light import Point_Light

if __name__ == '__main__':
    canvas_size = 200
    wall_size = 10
    pix_size = wall_size/canvas_size
    half = wall_size/2
    wall_z = 10

    c = Canvas(canvas_size,canvas_size)
    s = Sphere()
    s.material.color = Color(0.2,0.8,1)
    s.material.shininess = 100
    # s.transform = Shear(0.5,0,0,0,0,0) * Scale(0.5,1,1)

    light = Point_Light(Point(-10,10,-10),Color(1,1,1))

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
                hit = i.hit()
                p = r.position(hit.t)
                n = hit.object.normal(p)
                camera = -r.direction
                color = hit.object.material.compute_lighting(light,p,camera,n)
                c.write_pixel(x,y,color)
    c.to_ppm('output/sphere_render_3d.ppm')