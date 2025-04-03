from tkinter import Tk, BOTH, Canvas

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)



class Window:
    def __init__(self, width=420, height=420):
        conf={
            'bg': "white",
            'height': f"{height}",
            'width': f"{width}",
            }
        self.__root = Tk()
        #self.__root.minsize(width, height)
        self.__root.geometry(f"{width}x{height}")
        self.__root.title("Maze Solver")
        self.canvas = Canvas(self.__root, conf)
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False
    
    def draw_line(self, line, fill_color="red"):
        line.draw(self.canvas, fill_color)







