# Punto 2D

# Camilo Villa Tamayo
# Miguel Angel Sarmiento Aguiar
# Marlon Perez Rios

import math

class Punto2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
    		return self.y

    def radio_polar(self):
        return math.sqrt((self.x**2) + (self.y**2))

    def angulo_polar(self):
        return math.atan2(self.y, self.x)

    def dist_euclidiana(self, a, b):
    		return math.sqrt(((a - self.x)**2) + ((b - self.y)**2))

p1 = Punto2D(5, 5)
print("Punto: (", p1.x, ",", p1.y, ")")
print("Radio Polar:", p1.radio_polar())
print("Angulo Polar (Radianes):", p1.angulo_polar())
print("Angulo Polar (Grados):",  math.degrees(p1.angulo_polar()))
print("Distancia Euclidiana:",  p1.dist_euclidiana(5, 4))
