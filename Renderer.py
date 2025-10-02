from typing import Tuple

class Renderer:
    def __init__(self, width: int=80, height: int=40, dist_from_screen: float=60):
        self.width = width
        self.height = height
        self.dist_from_screen = dist_from_screen
        self.buffer = [[' ' for _ in range(width)] for _ in range(height)]
    
    def project(self, x: float, y: float, z: float) -> Tuple[int, int]:
        '''
        Project 3d point to 2d 
        (x, y, z) -> h/(h+z) * (x, y)
        '''
        h = self.dist_from_screen
        h_plus_z = h + z
        if h_plus_z == 0:
            h_plus_z = 0.01
            
        scale = h / h_plus_z
        disp_x = int(self.width / 2 + x * scale)
        disp_y = int(self.height / 2 - y * scale)
        
        return (disp_x, disp_y)
    