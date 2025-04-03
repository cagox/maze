from app import Window
from maze import Maze

win = Window(800, 600)
maze = Maze(2,2,20,20,25,25,win)



win.wait_for_close()
