from PIL import Image
import numpy as np
import vectormath as vmath
import math

h, w = 100, 100
image = np.ndarray((w, h, 3), dtype=np.uint8)
origin = vmath.Vector3(0, 0, 0)
resolution = vmath.Vector2(w, h)

sphere = vmath.Vector3(0, 0, 4)
radius = 1.0

def normalize(min_val, max_val, val):
    return (val - min_val) / (max_val - min_val)


def get_color(ray):
    distance = (sphere - origin).dot(ray)
    point = origin + (ray * distance)

    y = (sphere - point).length
    if(y < radius):
        x = math.sqrt(radius*radius - y*y)

        t1 = distance - x
        t2 = distance + x

        sphere_t = sphere.length
        intensity = normalize(sphere_t, sphere_t - radius, t1)
        return [255 * intensity, 255 * intensity, 255 * intensity]
    return [0, 0, 0]

for x in range(w):
    for y in range(h):
        coord = vmath.Vector2(x, y)
        center_coord = (coord - (0.5 * resolution))/resolution.y

        ray = vmath.Vector3(center_coord.x, center_coord.y, 1).normalize()
        color = get_color(ray)
        image[x][y] = color

img = Image.fromarray(image, 'RGB')
img.save('render.png')
        