from typing import List


def isBipartite(graph: List[List[int]]) -> bool:
    # DFS with coloring solution
    colors = [0] * len(graph)

    def dfs(node, color):
        # If the node is already colored, return bool of whether the node is colored different than its neighbors
        if colors[node]:
            return colors[node] == color

        # Set the color of the node to color
        colors[node] = color

        # For each node in the adjacency list, set the color to the off-color.
        # If they have already been colored and the color is not alternated, it will return False
        # Indicating that this is not a Bipartite graph
        for v in graph[node]:
            if not dfs(v, -color):
                return False

        return True

    # Loop through each index in the graph and use the dfs to search and color each node
    for i in range(len(graph)):
        # If the node has already been colored, skip it has already been searched as part of a previous DFS
        if not colors[i]:
            if not dfs(i, 1):
                return False

    return True

    # DSU Solution (slow)
    # parents = [_ for _ in range(len(graph))]
    # rank = [0] * len(graph)
    #
    # def find(node):
    #     if parents[node] != node:
    #         return find(parents[node])
    #     return node
    #
    # def union(node1, node2):
    #     if is_connected(node1, node2):
    #         return
    #     if rank[node1] >= rank[node2]:
    #         parents[node2] = node1
    #         rank[node1] += 1
    #     else:
    #         parents[node1] = node2
    #         rank[node2] += 1
    #
    # def is_connected(node1, node2):
    #     return find(node1) == find(node2)
    #
    # for i in range(len(graph)):
    #     for j in range(len(graph[i])):
    #         if is_connected(i, graph[i][j]):
    #             return False
    #         union(graph[i][0], graph[i][j])
    #
    # return True


isBipartite([[1, 2, 3], [0, 2], [1, 3], [0, 1, 2]])
