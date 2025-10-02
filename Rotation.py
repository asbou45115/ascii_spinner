from math import cos, sin
from typing import Tuple

class Rotation:
    def __init__(self, angle_x: float, angle_y: float, angle_z: float):
        self.A = angle_x
        self.B = angle_y
        self.C = angle_z

    def rotate_x(self, x: float, y: float, z: float) -> float:
        return x * cos(self.A) * cos(self.B) + y * sin(self.A) * cos(self.B) - z * sin(self.B)

    def rotate_y(self, x: float, y: float, z: float) -> float:
        return (
            x * (cos(self.A) * sin(self.B) * sin(self.C) - sin(self.A) * cos(self.C)) + 
            y * (sin(self.A) * sin(self.B) * sin(self.C) + cos(self.A) * cos(self.C)) +
            z * cos(self.B) * sin(self.C)
            )

    def rotate_z(self, x: float, y: float, z: float) -> float:
        return (
            x * (cos(self.A) * sin(self.B) * cos(self.C) + sin(self.A) * sin(self.C)) + 
            y * (sin(self.A) * sin(self.B) * cos(self.C) - cos(self.A) * sin(self.C)) +
            z * cos(self.B) * cos(self.C)
            )

    def rotate_point(self, x: float, y: float, z: float) -> Tuple[float, float, float]:
        return (self.rotate_x(x, y, z), self.rotate_y(x, y, z), self.rotate_z(x, y, z))