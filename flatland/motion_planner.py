import numpy as np
from flatland.graph import Graph
from flatland.gridworld import Gridworld
from flatland.weighted_graph import WeightedGraph


class MotionPlanner:
    def __init__(self):
        self.size = 32
        self.start = (1, 1)
        self.start_flattened = int(np.ravel_multi_index([[1], [1]], (self.size, self.size)))
        self.goal = (self.size - 1, self.size - 1)
        self.goal_flattened = int(np.ravel_multi_index([[self.size - 2], [self.size - 2]], (self.size, self.size)))

        # Initialize Gridworld
        self.world = Gridworld(size=self.size, coverage=0.2, start=self.start, terminal=self.goal)

        print(f'Start Node: {self.start_flattened}, {self.start}')
        print(f'Goal Node: {self.goal_flattened}, {self.goal}')

    def bfs_planner(self):
        return self.world.graph.bfs(self.start_flattened, self.goal_flattened)

    def dfs_planner(self):
        return self.world.graph.dfs(self.start_flattened, self.goal_flattened)

    def dijkstra_planner(self):
        # Cycle through Dijkstra Visited Nodes to Backtrace Shortest Path
        dj_prev_nodes, dj_path = self.world.weighted_graph.dijkstra(self.start_flattened)
        path = []
        curr_node = self.goal_flattened
        while curr_node != self.start_flattened:
            path.append(curr_node)
            curr_node = dj_prev_nodes[curr_node]
        return path

    def random_planner(self):
        pass

    def draw_path(self, path, title):
        '''
        Draws path in Gridworld
        :param paths: list of lists, flattened coordinates
        :param title: string of plot title
        '''
        self.world.draw_grid(path=path, title=title)

    def draw_grid(self):
        pass


if __name__ == '__main__':
    # TODO: Gridworld class should be instantiated here and passed into MotionPlanner class
    # TODO: Handle exception: no path exists from start to goal
    # TODO: BFS, DFS, and Dijkstra should all use the same Graph class
    motion_planner = MotionPlanner()
    bfs_path = motion_planner.bfs_planner()
    dfs_path = motion_planner.dfs_planner()
    dj_path = motion_planner.dijkstra_planner()
    print(f'BFS Path (Length {len(bfs_path)}): {bfs_path}')
    print(f'DFS Path (Length {len(dfs_path)}): {dfs_path}')
    print(f'Dijkstra Path (Length {len(dj_path)}): {dj_path}')
    motion_planner.draw_path(path=dj_path, title='Dijkstra\'s Path')
    motion_planner.draw_path(path=dfs_path, title='Depth First Search Path')
    motion_planner.draw_path(path=bfs_path, title='Breadth First Search Path')
