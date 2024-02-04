import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as c
import random
from flatland.graph import Graph
from flatland.weighted_graph import WeightedGraph


class Gridworld:
    # TODO: combine create_graph() and create_weighted_graph() into one function
    def __init__(self, size, coverage, start, terminal):
        self.__coverage = coverage
        self.size = size
        self.__start = start
        self.__terminal = terminal
        self.__grid = np.zeros(shape=(size, size), dtype=int)
        self.__num_obstacle = 0
        self.__graph = Graph()
        self.__weighted_graph = WeightedGraph()
        self.draw_border()
        self.add_obstacles()
        self.create_graph()
        self.create_weighted_graph()

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
    def graph(self):
        return self.__graph

    @property
    def weighted_graph(self):
        return self.__weighted_graph

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

    def create_graph(self):
        for i in range(1, self.size-1):
            for j in range(1, self.size-1):
                if self.grid[(i, j)] == 0:
                    # go through all neighbors and check if 0, if so, add_edge()
                    north_neighbor = self.grid[(i-1, j)]
                    west_neighbor = self.grid[(i, j-1)]
                    south_neighbor = self.grid[(i+1, j)]
                    east_neighbor = self.grid[(i, j+1)]

                    # Flatten Coordinates to use with Graph.bfs() and Graph.dfs() functions
                    flattened_coords = int(np.ravel_multi_index([[i], [j]], (self.size, self.size)))
                    north_flattened_coords = int(np.ravel_multi_index([[i-1], [j]], (self.size, self.size)))
                    west_flattened_coords = int(np.ravel_multi_index([[i], [j-1]], (self.size, self.size)))
                    south_flattened_coords = int(np.ravel_multi_index([[i+1], [j]], (self.size, self.size)))
                    east_flattened_coords = int(np.ravel_multi_index([[i], [j+1]], (self.size, self.size)))

                    if north_neighbor == 0:
                        self.graph.add_edge(flattened_coords,north_flattened_coords)
                    if west_neighbor == 0:
                        self.graph.add_edge(flattened_coords,west_flattened_coords)
                    if south_neighbor == 0:
                        self.graph.add_edge(flattened_coords,south_flattened_coords)
                    if east_neighbor == 0:
                        self.graph.add_edge(flattened_coords,east_flattened_coords)

    def create_weighted_graph(self):
        for i in range(1, self.size - 1):
            for j in range(1, self.size - 1):
                if self.grid[(i, j)] == 0:
                    # go through all neighbors and check if 0, if so, addEdge()
                    north_neighbor = self.grid[(i - 1, j)]
                    west_neighbor = self.grid[(i, j - 1)]
                    south_neighbor = self.grid[(i + 1, j)]
                    east_neighbor = self.grid[(i, j + 1)]

                    # Flatten Coordinates to use with Graph.bfs() function
                    flattened_coords = int(np.ravel_multi_index([[i], [j]], (self.size, self.size)))
                    north_flattened_coords = int(np.ravel_multi_index([[i - 1], [j]], (self.size, self.size)))
                    west_flattened_coords = int(np.ravel_multi_index([[i], [j - 1]], (self.size, self.size)))
                    south_flattened_coords = int(np.ravel_multi_index([[i + 1], [j]], (self.size, self.size)))
                    east_flattened_coords = int(np.ravel_multi_index([[i], [j + 1]], (self.size, self.size)))

                    if north_neighbor == 0:
                        self.weighted_graph.add_edge(flattened_coords, north_flattened_coords, 1)
                    if west_neighbor == 0:
                        self.weighted_graph.add_edge(flattened_coords, west_flattened_coords, 1)
                    if south_neighbor == 0:
                        self.weighted_graph.add_edge(flattened_coords, south_flattened_coords, 1)
                    if east_neighbor == 0:
                        self.weighted_graph.add_edge(flattened_coords, east_flattened_coords, 1)

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

    def draw_grid(self, path=None, title=''):
        # TODO: for each coord in path, add to path_grid, call plt.show(). Add waiting period.
        fig, axs = plt.subplots()
        path_grid = self.grid
        colors = []
        path_2d = ()
        # If no path given, print only grid
        # else convert flattened path coordinates to 2D coordinates and display
        if path is not None:
            colors = ['w', 'k', 'r']

            # Convert flattened corr
            path_2d = np.unravel_index(path, (self.size, self.size), order='C')

            for idx, i in enumerate(path_2d[0]):
                j = path_2d[1][idx]
                coord = (i, j)
                path_grid[coord] = 2
        else:
            colors = ['w', 'k']


        # Color Mesh used to display a grid
        cmap = c.ListedColormap(colors)
        plt.pcolormesh(path_grid, cmap=cmap)

        axs.set_aspect('equal')
        plt.xticks([])
        plt.yticks([])
        plt.gca().invert_yaxis()
        plt.title(f'{self.size}x{self.size} Gridworld, Obstacle Coverage is {self.coverage*100}% \n {title}')
        plt.show()

        for idx, i in enumerate(path_2d[0]):
            j = path_2d[1][idx]
            coord = (i, j)
            path_grid[coord] = 0