import numpy as np
import matplotlib.pyplot as plt
import random
from flatland.graph import Graph


class GridWorld:
    def __init__(self, size, coverage, start, terminal):
        self.__coverage = coverage
        self.size = size
        self.__start = start
        self.__terminal = terminal
        self.__grid = np.zeros(shape=(size, size), dtype=int)
        self.__num_obstacle = 0
        self.__state_transition_graph = Graph()
        self.draw_border()

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

    @property
    def start(self):
        return self.__start

    @property
    def terminal(self):
        return self.__terminal

    @property
    def state_transition_graph(self):
        return self.__state_transition_graph

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

    def draw_border(self):
        for i in range(0,self.grid.shape[0]):
            # Top/Bottom Borders
            self.update_cell((0,i),1)
            self.update_cell((self.grid.shape[0]-1,i),1)
            # Left/Right Borders
            self.update_cell((i,0),1)
            self.update_cell((i,self.grid.shape[1]-1),1)

    def create_state_transition_graph(self):
        for i in range(1, self.size-1):
            for j in range(1, self.size-1):
                if self.grid[(i,j)] == 0:
                    # go through all neighbors and check if 0, if so, addEdge()
                    north_neighbor = self.grid[(i-1,j)]
                    west_neighbor = self.grid[(i,j-1)]
                    south_neighbor = self.grid[(i+1,j)]
                    east_neighbor = self.grid[(i,j+1)]

                    flattened_coords = int(np.ravel_multi_index([[i],[j]],(self.size,self.size)))
                    north_flattened_coords = int(np.ravel_multi_index([[i-1],[j]],(self.size,self.size)))
                    west_flattened_coords = int(np.ravel_multi_index([[i],[j-1]],(self.size,self.size)))
                    south_flattened_coords = int(np.ravel_multi_index([[i+1],[j]],(self.size,self.size)))
                    east_flattened_coords = int(np.ravel_multi_index([[i],[j+1]],(self.size,self.size)))

                    if north_neighbor == 0:
                        self.state_transition_graph.addEdge(flattened_coords,north_flattened_coords)
                    if west_neighbor == 0:
                        self.state_transition_graph.addEdge(flattened_coords,west_flattened_coords)
                    if south_neighbor == 0:
                        self.state_transition_graph.addEdge(flattened_coords,south_flattened_coords)
                    if east_neighbor == 0:
                        self.state_transition_graph.addEdge(flattened_coords,east_flattened_coords)

    def add_obstacles(self):
        # TODO: make sure tetrominos don't overlap
        num_obstacles = round(self.size*self.size * self.coverage)
        self.num_obstacle = num_obstacles
        num_tetromino = num_obstacles // 4

        # Draw Tetrominos
        for t in range(num_tetromino):

            # Pick a random tetromino from the four in Fig. 3
            # 0: Fig. 3, first obstacle, straight line
            # 1: Fig. 3, second obstacle
            # 2: Fig. 3, third obstacle
            # 3: Fig. 3, fourth obstacle
            tetromino = random.randint(0, 3)

            if tetromino == 0:
                # print(f'tetromino #1')
                # Check all new locations in grid, if 1, get new start_row and start_col
                start_row = random.randint(1, self.grid.shape[0]-5)
                start_col = random.randint(1, self.grid.shape[1]-2)
                cell_1 = (start_row,start_col)
                cell_2 = (start_row+1,start_col)
                cell_3 = (start_row+2, start_col)
                cell_4 = (start_row+3, start_col)

            elif tetromino == 1:
                # print(f'tetromino #2')
                start_row = random.randint(1,self.grid.shape[0]-4)
                start_col = random.randint(1,self.grid.shape[1]-3)
                cell_1 = (start_row,start_col)
                cell_2 = (start_row,start_col+1)
                cell_3 = (start_row+1, start_col+1)
                cell_4 = (start_row+2, start_col+1)

            elif tetromino == 2:
                # print(f'tetromino #3')
                start_row = random.randint(1,self.grid.shape[0]-4)
                start_col = random.randint(1, self.grid.shape[1] - 3)
                cell_1 = (start_row, start_col)
                cell_2 = (start_row + 1, start_col)
                cell_3 = (start_row + 1, start_col + 1)
                cell_4 = (start_row + 2, start_col + 1)

            else:
                # print(f'tetromino #4')
                start_row = random.randint(1, self.grid.shape[0] - 4)
                start_col = random.randint(2, self.grid.shape[1] - 2)
                cell_1 = (start_row, start_col)
                cell_2 = (start_row + 1, start_col)
                cell_3 = (start_row + 1, start_col - 1)
                cell_4 = (start_row + 2, start_col)

            # Update tetromino cells to 1 indicating obstacle
            self.update_cell(location=cell_1, value=1)
            self.update_cell(location=cell_2, value=1)
            self.update_cell(location=cell_3, value=1)
            self.update_cell(location=cell_4, value=1)

    def draw_grid(self):
        fig, ax = plt.subplots()
        plt.pcolormesh(self.grid)
        ax.set_aspect('equal')
        plt.xticks([])
        plt.yticks([])
        plt.gca().invert_yaxis()
        plt.title(f'{self.size}x{self.size} Gridworld, Obstacle Coverage is {self.coverage*100}%\n {self.size*self.size} cells, {4*(self.num_obstacle // 4)} obstacle cells')
        plt.show()

    def draw_path(self,flattened_path):
        # add path to a copy of grid, then plot
        pass


if __name__ == '__main__':
    size = 128
    start = (1,1)
    start_flattened = int(np.ravel_multi_index([[1],[1]],(size,size)))
    terminal = (size-10,size-10)
    terminal_flattened = int(np.ravel_multi_index([[size-5],[size-5]],(size,size)))
    world = GridWorld(size=size, coverage=0.1, start=start, terminal=terminal)
    world.add_obstacles()
    world.create_state_transition_graph()
    world.draw_grid()
    print(f'start_flattened: {start_flattened}')
    print(f'terminal_flattened: {terminal_flattened}')
    path = world.state_transition_graph.bfs(start_flattened, terminal_flattened)
    print(len(path))
