import vectormath as vmath

class Sphere():

    def __init__(self, x, y, z, radius):
        self.center = vmath.Vector3(x, y, z)
        self.radius = radius