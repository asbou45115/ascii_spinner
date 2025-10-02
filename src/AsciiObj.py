import time
from abc import ABC, abstractmethod
from src.Renderer import Renderer
from src.Rotation import Rotation
from typing import List, Tuple

class AsciiObj(ABC):
    def __init__(self, renderer: Renderer, surfaces: List[Tuple[float, float, float, str]]):
        self.renderer = renderer
        self.surfaces = surfaces
    
    @abstractmethod
    def create_faces(self) -> List[Tuple[float, float, float, str]]:
        pass
    
    def run_on_terminal(self):
        angle = 0
        while True:
            rotation = Rotation(angle, angle*0.7, angle*0.3)
            self.renderer.clear_frame()
            
            for x, y, z, char in self.surfaces:
                rx, ry, rz = rotation.rotate_point(x, y, z)
                px, py, pz = self.renderer.project(rx, ry, rz)
                self.renderer.set_pixel(px, py, pz, char)
                
            self.renderer.clear()
            self.renderer.render()

            angle += 0.05
            time.sleep(0.02)

class Cube(AsciiObj):
    def __init__(self, renderer, size: int=12, step: float=0.8):
        surfaces = self.create_faces(size, step)
        super().__init__(renderer, surfaces)

    def create_faces(self, size: int, step: int):
        surfaces: List[Tuple[float, float, float, str]] = []
        
        # Front face - #
        for i in [j * step for j in range(-size, size + 1)]:
            for k in [j * step for j in range(-size, size + 1)]:
                surfaces.append((i, k, size * step, '#'))
        
        # Back face - @
        for i in [j * step for j in range(-size, size + 1)]:
            for k in [j * step for j in range(-size, size + 1)]:
                surfaces.append((i, k, -size * step, '@'))
        
        # Left face - *
        for i in [j * step for j in range(-size, size + 1)]:
            for k in [j * step for j in range(-size, size + 1)]:
                surfaces.append((-size * step, i, k, '*'))
        
        # Right face - +
        for i in [j * step for j in range(-size, size + 1)]:
            for k in [j * step for j in range(-size, size + 1)]:
                surfaces.append((size * step, i, k, '+'))
        
        # Top face - $
        for i in [j * step for j in range(-size, size + 1)]:
            for k in [j * step for j in range(-size, size + 1)]:
                surfaces.append((i, size * step, k, '$'))
        
        # Bottom face - -
        for i in [j * step for j in range(-size, size + 1)]:
            for k in [j * step for j in range(-size, size + 1)]:
                surfaces.append((i, -size * step, k, '-'))
                
        return surfaces
    
class TriangularPyramid(AsciiObj):
    def __init__(self, renderer, size: int=12, step: float=0.8):
        surfaces = self.create_faces(size, step)
        super().__init__(renderer, surfaces)
        
    def create_faces(self, size: int, step: float) -> List[Tuple[float, float, float, str]]:
        surfaces: List[Tuple[float, float, float, str]] = []
        
        # Define pyramid vertices
        apex = (0, size * step, 0)  # Top point
        base1 = (-size * step, -size * step, size * step)   # Base front-left
        base2 = (size * step, -size * step, size * step)    # Base front-right
        base3 = (0, -size * step, -size * step)             # Base back
        
        # Front-left triangular face - #
        surfaces.extend(self._create_triangle(apex, base1, base2, step, '#'))
        
        # Back-left triangular face - *
        surfaces.extend(self._create_triangle(apex, base3, base1, step, '*'))
        
        # Back-right triangular face - +
        surfaces.extend(self._create_triangle(apex, base2, base3, step, '+'))
        
        # Base triangular face - =
        surfaces.extend(self._create_triangle(base1, base2, base3, step, '='))
                
        return surfaces
    
    def _create_triangle(
        self, 
        p1: Tuple[float, float, float], 
        p2: Tuple[float, float, float], 
        p3: Tuple[float, float, float], 
        step: float, 
        char: str
    ) -> List[Tuple[float, float, float, str]]:
        """
        Fill a triangle with points using barycentric coordinates
        """
        points: List[Tuple[float, float, float, str]] = []
        
        # Sample the triangle using a grid and barycentric coordinates
        samples = int(20 / step)  # Adjust density based on step
        
        for i in range(samples + 1):
            for j in range(samples + 1 - i):
                # Barycentric coordinates
                u = i / samples if samples > 0 else 0
                v = j / samples if samples > 0 else 0
                w = 1 - u - v
                
                if w >= 0:  # Valid barycentric coordinate
                    # Interpolate position
                    x = w * p1[0] + u * p2[0] + v * p3[0]
                    y = w * p1[1] + u * p2[1] + v * p3[1]
                    z = w * p1[2] + u * p2[2] + v * p3[2]
                    
                    points.append((x, y, z, char))
        
        return points