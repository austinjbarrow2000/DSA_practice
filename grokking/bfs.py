# Breadth First Search

graph = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}


def bfs(graph, node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        print(queue[0])
        for node in graph[queue[0]]:
            if node not in visited:
                queue.append(node)
                visited.append(node)
        queue.pop(0)


bfs(graph, "5")
