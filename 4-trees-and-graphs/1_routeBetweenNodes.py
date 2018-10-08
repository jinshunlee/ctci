# Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.

from collections import deque

# Time O(V + E)
# Space O(V)


def BFS(start, end, graph):
    queue = deque([start])
    visited = set()

    while queue:
        cur = queue.popleft()
        if cur == end:
            return True
        for vertex in graph.get(cur, []):
            if vertex not in visited:
                visited.add(vertex)
                queue.append(vertex)
    return False


def routeBetweenNodes(graph, node1, node2):
    return BFS(node1, node2, graph)


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['E', 'F'],
        'C': ['G'],
        'G': ['H'],
        'I': ['Z']
    }

    print(routeBetweenNodes(graph, 'A', 'H'))
    print(routeBetweenNodes(graph, 'A', 'Z'))
