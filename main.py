from src.Renderer import Renderer
from src.AsciiObj import Cube, TriangularPyramid
    
def main():
    renderer = Renderer(width=80, height=40, dist_from_screen=60)
    # cube = Cube(renderer)
    # cube.run_on_terminal()       

    tri_py = TriangularPyramid(renderer)
    tri_py.run_on_terminal()

if __name__ == "__main__":
    main()