from app import Window, Point, Line

class Cell:
    def __init__(self, window=None, x1=2, y1=2, x2=11, y2=11, left=True, right=True, top=True, bottom=True):
        self.has_left_wall = left
        self.has_right_wall = right
        self.has_top_wall = top
        self.has_bottom_wall = bottom
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = window
    
    def draw(self):
        if self._win is None:
            return
        if self.has_top_wall:
            top_wall = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(top_wall)
        if self.has_right_wall:
            right_wall = Line(Point(self._x2,self._y1), Point(self._x2, self._y2))
            self._win.draw_line(right_wall)
        if self.has_bottom_wall:
            bottom_wall = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(bottom_wall)
        if self.has_left_wall:
            left_wall = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(left_wall)
        
    def center(self):
        x= (self._x1+self._x2)//2
        y= (self._y1+self._y2)//2
        """
        if self._x1 > self._x2:
            x = (self._x1 - self._x2)//2
        else:
            x = (self._x2 - self._x1)//2
        if self._y1 > self._y2:
            y = (self._y1 - self._y2)//2
        else:
            y = (self._y2 - self._y1)//2
        """
        return Point(x,y)
    
    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = "gray"    
        else:
            fill_color = "red"
        self._win.draw_line(Line(self.center(), to_cell.center()),fill_color)
        