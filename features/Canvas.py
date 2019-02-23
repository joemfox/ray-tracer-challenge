from features.util import equals
from features.Tuple import Tuple, Point, Vector, Color

class Canvas:
    def __init__(self, width, height, color = Color(0,0,0)):
        self.width = width
        self.height = height
        self.canvas = [[{"color":color} for x in range(width)] for y in range(height)]

    def write_pixel(self, x, y, color):
        x = round(x)
        y = round(y)
        if (x >= self.width) or (y >= self.height):
            return
        self.canvas[y][x]["color"] = color

    def pixel_at(self, x, y):
        return self.canvas[y][x]

    def to_ppm(self,filepath=None):
        # ppm headers: P3 height width 255
        ppm = f"P3\n{self.width} {self.height}\n255\n"

        color_data = ""
        for row in self.canvas:
            row = " ".join([i["color"].to_string() for i in row])
            # if(len(" ".join(row)) > 70):
            values = iter(row.split())
            current = next(values)
            for v in values:
                if len(current) + 1 + len(v) > 70:
                    color_data += current + "\n"
                    current = v
                else:
                    current += " " + v
            
            color_data += current + "\n"

        ppm += color_data
        if(filepath):
            with open(filepath,"w") as f:
                f.write(ppm)
        return ppm