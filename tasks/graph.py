from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        def rec_dfs(graph, node, visited):
            if node not in visited:
                visited.append(node)
                for k in graph.outbound:
                    rec_dfs(k,k, visited)
            return visited

        return rec_dfs(self._root, self._root,[])

    def bfs(self) -> list[Node]:
        visited = [] # List to keep track of visited nodes.
        queue = []     #Initialize a queue

        visited.append(self._root)
        queue.append(self._root)

        while queue:
            s = queue.pop(0) 

            for neighbour in s.outbound:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)

        return visited