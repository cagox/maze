from app import Window
from cell import Cell
import time
import random

WAIT_TIME = 0.25

class Maze:
    def __init__(self,
                 x1,
                 y1,
                 num_cols,
                 num_rows,
                 cell_size_x,
                 cell_size_y,
                 win=None,
                 seed=None):
        if seed is not None:
            seed = random.seed(seed)
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = [[None for _ in range(self.num_rows)] for _ in range(self.num_cols)]
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        
    def _create_cells(self):
        for y in range(self.num_rows):
            for x in range(self.num_cols):
                x1 = self.x1 + x * self.cell_size_x
                x2 = x1 + self.cell_size_x
                y1 = self.y1 + y * self.cell_size_y
                y2 = y1 + self.cell_size_y
                self.cells[x][y] = Cell(self.win, x1,y1, x2,y2)
                self._draw_cell(x,y)

    
    def _animate(self):
        self.win.redraw()
        time.sleep(WAIT_TIME)
    
    def _draw_cell(self, row, col):
        if self.win is not None:
            self.cells[row][col].draw()
    
    def _break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self.cells[self.num_cols-1][self.num_rows-1].has_right_wall = False
        self._draw_cell(self.num_rows-1, self.num_cols-1)
    
    def _break_walls_r( self, i, j):
        self.cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self.cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self.num_cols - 1 and not self.cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self.cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self.num_rows - 1 and not self.cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self.cells[i][j].has_right_wall = False
                self.cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self.cells[i][j].has_left_wall = False
                self.cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
            
    def _reset_cells_visited(self):
        for c in range(self.num_cols):
            for r in range(self.num_rows):
                self.cells[c][r].visited = False
    
    def solve(self):
        self._solve_r(0,0)
    
    def _solve_r(self, x, y):
        self._animate()
        self.cells[x][y].visited = True
        if x == self.num_cols-1 and y == self.num_rows-1:
            return True
        # Check directions:
        #top
        if y != 0:
            if not self.cells[x][y].has_top_wall:
                if not self.cells[x][y-1].visited:
                    self.cells[x][y].draw_move(self.cells[x][y-1])
                    if self._solve_r(x,y-1):
                        return True
                    self.cells[x][y].draw_move(self.cells[x][y-1], undo=True)
        #right
        if x != self.num_cols-1:
            if not self.cells[x][y].has_right_wall:
                if not self.cells[x+1][y].visited:
                    self.cells[x][y].draw_move(self.cells[x+1][y])
                    if self._solve_r(x+1,y):
                        return True
                    self.cells[x][y].draw_move(self.cells[x+1][y], undo=True)
        #bottom
        if y != self.num_rows-1:
            if not self.cells[x][y].has_bottom_wall:
                if not self.cells[x][y+1].visited:
                    self.cells[x][y].draw_move(self.cells[x][y+1])
                    if self._solve_r(x,y+1):
                        return True
                    self.cells[x][y].draw_move(self.cells[x][y+1], undo=True)
        #left
        if x != 0:
            if not self.cells[x][y].has_left_wall:
                if not self.cells[x-1][y].visited:
                    self.cells[x][y].draw_move(self.cells[x-1][y])
                    if self._solve_r(x-1,y):
                        return True
                    self.cells[x][y].draw_move(self.cells[x-1][y], undo=True)
        #None worked
        return False
            

