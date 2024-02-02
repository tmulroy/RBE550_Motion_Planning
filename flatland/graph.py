# Code from geeksforgeeks.org
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/?ref=lbp
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/?ref=lbp
from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation

class Graph:

    def __init__(self):
        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start, end):
        # Source: https://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search
        # Source: Author: @SeasonShot
        queue = [(start, [start])]
        visited = set()

        while queue:
            vertex, path = queue.pop(0)
            visited.add(vertex)
            for node in self.graph[vertex]:
                if node == end:
                    return path + [end]
                else:
                    if node not in visited:
                        visited.add(node)
                        queue.append((node, path + [node]))

    def dfs(self, start, goal):
        '''
        Source: https://stackoverflow.com/questions/12864004/tracing-and-returning-a-path-in-depth-first-search
        Source Author: @XueYu
        :param start: int
        :param goal: int
        :return: list
        '''
        stack = [(start, [start])]
        visited = set()
        while stack:
            (vertex, path) = stack.pop()
            if vertex not in visited:
                if vertex == goal:
                    return path
                visited.add(vertex)
                for neighbor in self.graph[vertex]:
                    stack.append((neighbor, path + [neighbor]))
