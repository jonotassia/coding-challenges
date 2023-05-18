from functools import cache
from typing import List, Set


def findSmallestSetOfVertices(n: int, edges: List[List[int]]) -> List[int]:
    # Set approach
    """
    Assumption: Anything that does not appear as the "to" in an edge is an origin. This is true because it is a
    directed acyclic graph, implying that each edge is directional and there are no cycles.
    """
    end_points = {edge[1] for edge in edges}
    return set(range(n)) - end_points

    # Naive approach, exceeds time-limit
    # @cache
    # def dfs(node: int) -> List[int]:
    #     neighbors: List[int] = []
    #
    #     for edge in edges:
    #         if edge[0] == node:
    #             neighbors += dfs(edge[1])
    #
    #     return neighbors + [node]
    #
    # # Declare a list that includes the children of each node by index
    # children: List[Set[int]] = [0] * n
    #
    # for node in range(n):
    #     children[node] = set(dfs(node))
    #
    # sorted_nodes = sorted(children, key=len, reverse=True)
    #
    # curr_set: Set[int] = set(sorted_nodes[0])
    # vertex_list: List[int] = [children.index(sorted_nodes[0])]
    # for node in sorted_nodes:
    #     new_set = node - curr_set
    #     if new_set:
    #         curr_set = curr_set.union(node)
    #         vertex_list += [children.index(node)]
    #
    # return vertex_list


findSmallestSetOfVertices(8, [[6, 4], [5, 4], [1, 0], [6, 1], [5, 7], [6, 0], [1, 4], [7, 4], [2, 3], [3, 7], [2, 5],
                              [3, 4], [2, 4], [6, 5], [4, 0]])
