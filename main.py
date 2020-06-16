from PIL import Image
import numpy as np
import vectormath as vmath
import math
from sphere import Sphere

h, w = 800, 600
image = np.ndarray((w, h, 3), dtype=np.uint8)
origin = vmath.Vector3(0, 0, 0)
resolution = vmath.Vector2(w, h)

sphere1 = Sphere(0, 0, 4, 1.0)
sphere2 = Sphere(1.3, 1.3, 8, 1.0)

spheres = [sphere1, sphere2]

def normalize(min_val, max_val, val):
    return (val - min_val) / (max_val - min_val)


def get_color(ray):

    distances = []
    for s in spheres:
        distances.append(s.intesect(origin, ray))
    
    min_distance = None

    for d in distances:
        if(d is not None):
            if(min_distance is None or d[0] < min_distance[0]):
                min_distance = d
           
    if(min_distance is not None):
        t1 = min_distance[0]
        t2 = min_distance[1]
        sphere_t_min = min_distance[2]
        sphere_t_max = min_distance[3]

        intensity = normalize(sphere_t_min, sphere_t_max, t1)
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
        