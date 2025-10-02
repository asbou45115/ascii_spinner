import os
from typing import Tuple

class Renderer:
    def __init__(self, width: int=80, height: int=40, dist_from_screen: float=60):
        '''
        Render screen for 3d ascii object on terminal
        '''
        self.width = width
        self.height = height
        self.dist_from_screen = dist_from_screen
        self.buffer = [[' ' for _ in range(width)] for _ in range(height)]
        self.zbuffer = [[float('-inf') for _ in range(width)] for _ in range(height)]
        
    def clear_frame(self):
        '''
        Resets the buffers to empty for the next frame
        '''
        self.buffer = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        self.zbuffer = [[float('-inf') for _ in range(self.width)] for _ in range(self.height)]
        
    def clear(self):
        '''
        applies terminal 'clear'
        '''
        os.system("cls" if os.name == "nt" else "clear")
    
    def project(self, x: float, y: float, z: float) -> Tuple[int, int, float]:
        '''
        Project 3d point to 2d 
        (x, y, z) -> h/(h+z) * (x, y)
        
        - Returns the projected x, y values and the z value
        '''
        h = self.dist_from_screen
        h_plus_z = h + z
        if h_plus_z == 0:
            h_plus_z = 0.01
            
        scale = h / h_plus_z
        disp_x = int(self.width / 2 + x * scale)
        disp_y = int(self.height / 2 - y * scale)
        
        return (disp_x, disp_y, z)
    
    def set_pixel(self, x: int, y: int, z: float, char: str):
        """
        Set a pixel if it's within screen bounds and closer than existing pixel
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            if z > self.zbuffer[y][x]:
                self.buffer[y][x] = char
                self.zbuffer[y][x] = z
                
    def render(self):
        '''
        Displays to terminal
        '''
        for row in self.buffer:
            print(''.join(row))