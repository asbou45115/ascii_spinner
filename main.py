import time
from src.Renderer import Renderer
from src.Rotation import Rotation
        
def main():
    renderer = Renderer(width=80, height=40, dist_from_screen=60)
    
    step = 0.8
    size = 12
    
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
    
    # Top face - =
    for i in [j * step for j in range(-size, size + 1)]:
        for k in [j * step for j in range(-size, size + 1)]:
            surfaces.append((i, size * step, k, '$'))
    
    # Bottom face - -
    for i in [j * step for j in range(-size, size + 1)]:
        for k in [j * step for j in range(-size, size + 1)]:
            surfaces.append((i, -size * step, k, '-'))
    
    angle = 0
    while True:
        rotation = Rotation(angle, angle*0.7, angle*0.3)
        renderer.clear_frame()
        
        for x, y, z, char in surfaces:
            rx, ry, rz = rotation.rotate_point(x, y, z)
            px, py, pz = renderer.project(rx, ry, rz)
            renderer.set_pixel(px, py, pz, char)
            
        renderer.clear()
        renderer.render()

        angle += 0.05
        time.sleep(0.02)

if __name__ == "__main__":
    main()