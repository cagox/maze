from app import Window
from cell import Cell
import time

class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_rows,
                 num_cols,
                 cell_size_x,
                 cell_size_y,
                 win=None,):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = [[None for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        self._create_cells()
        
    def _create_cells(self):
        for y in range(self.num_rows):
            for x in range(self.num_cols):
                x1 = self.x1 + x * self.cell_size_x
                x2 = x1 + self.cell_size_x
                y1 = self.y1 + y * self.cell_size_y
                y2 = y1 + self.cell_size_y
                self.cells[x][y] = Cell(self.win, x1,y1, x2,y2)
                if self.win is not None:
                    self.cells[x][y].draw()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.5)
                