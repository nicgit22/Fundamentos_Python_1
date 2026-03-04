class Triangulo:
    lado_A: float
    lado_B: float
    lado_C: float


    def area(self) -> float:
        from math import sqrt
        p = (self.lado_A + self.lado_B + self.lado_C) / 2
        return sqrt( p * ( p = self.lado_A) * (p * self.lado_B))
