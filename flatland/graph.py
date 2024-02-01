# Code from geeksforgeeks.org
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/?ref=lbp
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/?ref=lbp

from collections import defaultdict

# This class represents a directed graph
# using adjacency list representation


class Graph:

    # Constructor
    def __init__(self):

        # Default dictionary to store graph
        self.graph = defaultdict(list)

    # Function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    # def BFS(self, s):
    #     # TODO: start BFS from a start node (source node)
    #     print(f'graph[s]: {self.graph[s]}')
    #     print(f'size of graph: {self.graph}')
    #     # Mark all the vertices as not visited
    #     visited = [False] * (max(self.graph) + 1)
    #
    #     # Create a queue for BFS
    #     queue = []
    #
    #     # Mark the source node as
    #     # visited and enqueue it
    #     queue.append(s)
    #     # print(f's: {s}')
    #     visited[s] = True
    #
    #     while queue:
    #         # Dequeue a vertex from
    #         # queue and print it
    #         s = queue.pop(0)
    #         print(s, end=" ")
    #
    #         # Get all adjacent vertices of the
    #         # dequeued vertex s.
    #         # If an adjacent has not been visited,
    #         # then mark it visited and enqueue it
    #         for i in self.graph[s]:
    #             if visited[i] == False:
    #                 queue.append(i)
    #                 visited[i] = True

    # def bfs(self, start, end):
    #     # maintain a queue of paths
    #     queue = []
    #     # push the first path into the queue
    #     queue.append([start])
    #     while queue:
    #         # get the first path from the queue
    #         path = queue.pop(0)
    #         # get the last node from the path
    #         node = path[-1]
    #         # path found
    #         print(f'node: {node}')
    #         if node == end:
    #             return path
    #         # enumerate all adjacent nodes, construct a
    #         # new path and push it into the queue
    #         for adjacent in self.graph.get(node, []):
    #             new_path = list(path)
    #             new_path.append(adjacent)
    #             queue.append(new_path)

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

    # A function used by DFS
    # def DFSUtil(self, v, visited):
    #
    #     # Mark the current node as visited
    #     # and print it
    #     visited.add(v)
    #     print(v, end=' ')
    #
    #     # Recur for all the vertices
    #     # adjacent to this vertex
    #     for neighbour in self.graph[v]:
    #         if neighbour not in visited:
    #             self.DFSUtil(neighbour, visited)
    #
    # # The function to do DFS traversal. It uses
    # # recursive DFSUtil()
    # def DFS(self, v):
    #
    #     # Create a set to store visited vertices
    #     visited = set()
    #
    #     # Call the recursive helper function
    #     # to print DFS traversal
    #     self.DFSUtil(v, visited)

    def dfs_paths(self, start, goal):
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