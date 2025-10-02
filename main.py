import time
from src.Renderer import Renderer
from src.Rotation import Rotation
        
def main():
    renderer = Renderer(width=80, height=40, dist_from_screen=60)
    
    step = 1
    surface_points = [(x, y, 0) for x in [i * step for i in range(-10, 11)]
                                 for y in [j * step for j in range(-10, 11)]]
    
    angle = 0
    while True:
        rotation = Rotation(angle, angle * 0.7, angle * 0.3)
        renderer.clear_frame()
        
        for x, y, z in surface_points:
            rx, ry, rz = rotation.rotate_point(x, y, z)
            px, py, pz = renderer.project(rx, ry, rz)
            renderer.set_pixel(px, py, pz, "#")
            
        renderer.clear()
        renderer.render()

        angle += 0.05
        time.sleep(0.05)

if __name__ == "__main__":
    main()