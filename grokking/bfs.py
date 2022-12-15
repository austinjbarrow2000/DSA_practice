# Breadth First Search

graph = {"5": ["3", "7"], "3": ["2", "4"], "7": ["8"], "2": [], "4": ["8"], "8": []}

# This uses a list when a queue would be better
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
    return visited


from collections import deque

# distance to check how long
def bfs_queue(graph, start):
    visited = []
    queue = deque([(start, 0)])

    while queue:
        node, dist = queue.popleft()
        if node in visited:
            continue

        visited.append(node)
        for node in graph[node]:
            queue.append((node, dist + 1))

    return visited, node, dist


print(bfs_queue(graph, "3"))
