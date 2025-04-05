import unittest
from maze import Maze

TESTSEED = 10

class Tests(unittest.TestCase):
    def test_maze_creat_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0, num_cols, num_rows, 10, 10, win=None, seed=TESTSEED)
        self.assertEqual(
            len(m1.cells[0]), num_rows,
        )
        
    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0, num_cols, num_rows, 10, 10, win=None, seed=TESTSEED)
        self.assertEqual(m1.cells[0][0].visited, False)
        self.assertEqual(m1.cells[m1.num_cols-1][m1.num_rows-1].visited, False)

if __name__ == "__main__":
    unittest.main()
    
