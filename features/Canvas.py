import math
from features.util import equals
from features.Tuple import Tuple, Point, Vector, Color

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.canvas = [[{"color":Color(0,0,0)} for x in range(width)] for y in range(height)]

    def write_pixel(self, x, y, color):
        print(x,y,len(self.canvas),len(self.canvas[0]))
        self.canvas[y][x]["color"] = color

    def pixel_at(self, x, y):
        return self.canvas[y][x]

    def to_ppm(self):
        # ppm headers: P3 height width 255
        ppm = f"P3\n{self.width} {self.height}\n255\n"

        color_data = ""
        for row in self.canvas:
            color_data += " ".join([i["color"].to_string()for i in row]) + "\n"

        ppm += color_data
        return ppm
