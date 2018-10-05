# Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
# route between two nodes.

# Time O(V + E)
# Space O(V)


def BFS(start, end, graph):
    queue = [start]
    visited = [start]

    while queue:
        cur = queue.pop(0)
        if cur == end:
            return True
        for node in graph.get(cur, []):
            if not node in visited:
                visited.append(node)
                queue.append(node)

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
