from time import *
from moscar_class import norm
from math import acos
from math import cos
from math import sin

lst = [0, 1, 2, 3]
lst = lst[:1] + lst[2:]
print(lst)
a = [1, 2]
b = [2, 3]


def derictio(a, b):
    x = b[0] - a[0]
    y = b[1] - a[1]
    n = norm(x, y)
    angle = acos(x / n)
    vx = cos(angle)
    vy = sin(angle)
    return vx, vy
