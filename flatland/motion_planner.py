import numpy as np
from flatland.graph import Graph
from flatland.gridworld import Gridworld
from flatland.weighted_graph import WeightedGraph


class MotionPlanner:
    def __init__(self):
        self.size = 128
        self.start = (1, 1)
        self.start_flattened = int(np.ravel_multi_index([[1], [1]], (self.size, self.size)))
        self.goal = (self.size - 5, self.size - 5)
        self.goal_flattened = int(np.ravel_multi_index([[self.size - 5], [self.size - 5]], (self.size, self.size)))

        # Initialize Gridworld
        self.world = Gridworld(size=self.size, coverage=0.1, start=self.start, terminal=self.goal)
        self.world.add_obstacles()

        print(f'Start Node: {self.start_flattened}, {self.start}')
        print(f'Goal Node: {self.goal_flattened}, {self.goal}')

    def bfs_planner(self):
        return self.world.graph.bfs(self.start_flattened, self.goal_flattened)

    def dfs_planner(self):
        return self.world.graph.dfs(self.start_flattened, self.goal_flattened)

    def dijkstra_planner(self):
        return self.world.weighted_graph.dijkstra(self.start_flattened)

    def random_planner(self):
        pass

    def draw_path(self):
        pass


if __name__ == '__main__':
    # TODO: Gridworld class should be instantiated here and passed into MotionPlanner class
    # TODO: Handle exception: no path exists from start to goal
    # TODO: BFS, DFS, and Dijkstra should all use the same Graph class
    motion_planner = MotionPlanner()
    bfs_path = motion_planner.bfs_planner()
    dfs_path = motion_planner.dfs_planner()
    dj_prev_nodes, dj_path = motion_planner.dijkstra_planner()
    # print(motion_planner.world.weighted_graph.)
    # print(f'BFS Path (Length {len(bfs_path)}): {bfs_path}')
    # print(f'DFS Path (Length {len(dfs_path)}): {dfs_path}')
    print(f'Dijkstra Path {dj_prev_nodes}')