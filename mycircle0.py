import math

PI = math.pi
xpos, ypos = 0, 0

def get_area(r):
    return PI * (r**2)
def get_peri(r):
    return 2 * PI * r
def set_pos(x, y):
    global xpos, ypos
    xpos, ypos = x, y