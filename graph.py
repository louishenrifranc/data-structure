from collections import defaultdict, deque


class Graph(object):
    def __init__(self, connections, directed=True):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        if node in self._graph:
            del self._graph[node]
        for other_node, neighbor in self._graph.items():
            self._graph[other_node].discard(node)

    def is_connected(self, node1, node2):
        return node1 in self._graph and node2 in self._graph[node1]

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

    def __contains__(self, item):
        return item in self._graph


def dfs(graph, start, end=None, visited=set()):
    # if end in visited:
    #     return visited
    for neighbor in graph[start]:
        if neighbor not in visited:
            visited.add(neighbor)
            dfs(graph, neighbor, end, visited)
    return visited


def dfs_path(graph, start, goal, path=list()):
    if len(path) == 0:
        path += [start]
    if start == goal:
        yield path
    for neighbor in graph[start] - set(path):
        yield from dfs_path(graph, neighbor, goal, path + [neighbor])


def bfs(graph, start, goal=None):
    visited, queue = set(), deque(start)
    while queue:
        current = queue.popleft()
        # if goal in visited:
        #     break
        if current not in visited:
            visited.add(current)
            queue.extend(graph[current] - visited)
    return visited


def bfs_path(graph, start, goal):
    queue = deque([start])
    while queue:
        path = queue.popleft()
        current = path[-1]
        for neighbor in graph[current] - set(path):
            if neighbor == goal:
                yield path + [neighbor]
            else:
                queue.append(path + [neighbor])


if __name__ == '__main__':
    g = Graph([(1, 2), (1, 4), (4, 11), (11, 4), (1, 11), (11, 3)])
    print([path for path in bfs_path(g._graph, 1, 3)])
