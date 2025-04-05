from app import Window
from maze import Maze

win = Window(800, 600)
maze = Maze(2,2,20,20,25,25,win, seed=0)
maze.solve()



win.wait_for_close()
