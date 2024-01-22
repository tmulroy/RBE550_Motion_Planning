import numpy as np
import matplotlib.pyplot as plt
import random


class GridWorld:
    def __init__(self, size, coverage):
        self.__coverage = coverage
        self.size = size
        self.__grid = np.zeros(shape=(size, size), dtype=int)
        # self.rng = random.seed()
        self.__num_obstacles = 0
        pass

    # GETTERS
    @property
    def grid(self):
        return self.__grid

    @property
    def coverage(self):
        return self.__coverage

    @property
    def num_obstacle(self):
        return self.__num_obstacles

    # SETTERS
    @grid.setter
    def grid(self, new_grid):
        self.__grid = new_grid

    @coverage.setter
    def coverage(self, new_coverage):
        self.__coverage = new_coverage

    @num_obstacle.setter
    def num_obstacle(self, new_num_obstacle):
        self.__num_obstacles = new_num_obstacle

    def update_cell(self, location, value):
        self.__grid[location] = value

    def f(self):
        # TODO: make sure tetrominos don't overlap
        num_obstacles = round(self.size*self.size * self.coverage)
        self.num_obstacles = num_obstacles
        num_tetromino = num_obstacles // 4
        print(f'Number of Tetrominos: {num_tetromino}')

        # Draw Tetrominos
        for t in range(num_tetromino):

            # Pick a random tetromino from the four in Fig. 3
            # 0: Fig. 3, first obstacle, straight line
            # 1: Fig. 3, second obstacle
            # 2: Fig. 3, third obstacle
            # 3: Fig. 3, fourth obstacle
            tetromino = random.randint(0,3)

            if tetromino == 0:
                print(f'tetromino #1')
                start_row = random.randint(0,self.grid.shape[0]-4)
                start_col = random.randint(0,self.grid.shape[1]-1)
                self.update_cell(location=(start_row,start_col), value=1)
                self.update_cell(location=(start_row+1,start_col), value=1)
                self.update_cell(location=(start_row+2, start_col), value=1)
                self.update_cell(location=(start_row+3, start_col), value=1)
            elif tetromino == 1:
                print(f'tetromino #2')
                start_row = random.randint(0,self.grid.shape[0]-3)
                start_col = random.randint(0,self.grid.shape[1]-2)
                self.update_cell(location=(start_row, start_col), value=1)
                self.update_cell(location=(start_row, start_col+1), value=1)
                self.update_cell(location=(start_row + 1, start_col+1), value=1)
                self.update_cell(location=(start_row + 2, start_col+1), value=1)
            elif tetromino == 2:
                print(f'tetromino #3')
                start_row = random.randint(0,self.grid.shape[0]-3)
                start_col = random.randint(0, self.grid.shape[1] - 2)
                self.update_cell(location=(start_row, start_col), value=1)
                self.update_cell(location=(start_row + 1, start_col), value=1)
                self.update_cell(location=(start_row + 1, start_col + 1), value=1)
                self.update_cell(location=(start_row + 2, start_col + 1), value=1)
            else:
                print(f'tetromino #4')
                start_row = random.randint(0, self.grid.shape[0] - 3)
                start_col = random.randint(1, self.grid.shape[1] - 1)
                self.update_cell(location=(start_row, start_col), value=1)
                self.update_cell(location=(start_row + 1, start_col), value=1)
                self.update_cell(location=(start_row + 1, start_col - 1), value=1)
                self.update_cell(location=(start_row + 2, start_col), value=1)



    def draw_grid(self):
        fig,ax = plt.subplots()
        plt.pcolormesh(self.grid)
        ax.set_aspect('equal')
        plt.xticks([])
        plt.yticks([])
        plt.gca().invert_yaxis()
        plt.title(f'{self.size}x{self.size} Gridworld, Obstacle Coverage is {self.coverage*100}%\n {self.size*self.size} cells, {4*(self.num_obstacles // 4)} obstacle cells')
        plt.show()


if __name__ == '__main__':
    world = GridWorld(size=20, coverage=0.1)
    world.f()
    world.draw_grid()
