from AsciiObj import AsciiObj
from Renderer import Renderer
from typing import List, Tuple

class Cube(AsciiObj):
    def __init__(self, renderer: Renderer, size: int=12, step: float=0.8):
        surfaces = create_faces(size, step)
        super().__init__(renderer, surfaces)

def create_faces(size: int, step: int) -> List[Tuple[float, float, float, str]]:
    surfaces = []
    
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