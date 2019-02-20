from features.Matrix import *
from features.Canvas import *
from features.Tuple import *

height = 500
c = Canvas(height,height)
p = Point(0,1,0)

for h in range(0,12):
    r = RotateZ(h*((math.pi*2)/12))
    t = Translate(height/2,height/2,0)
    s = Scale(height/3,height/3,0)
    hand = t * s * r * p
    print(hand.coords)
    c.write_pixel(hand.x,hand.y,Color(1,1,0))

c.to_ppm('./output/clock.ppm')