import vectormath as vmath
import math

class Sphere():

    def __init__(self, x, y, z, radius):
        self.center = vmath.Vector3(x, y, z)
        self.radius = radius

    def intesect(self, origin, ray):
        distance = (self.center - origin).dot(ray)
        point = origin + (ray * distance)

        y = (self.center - point).length
        if(y < self.radius):
            x = math.sqrt(self.radius * self.radius - y*y)

            t1 = distance - x
            t2 = distance + x

            sphere_t = (self.center - origin).length
            return (t1, t2, sphere_t, sphere_t - self.radius)
        return None