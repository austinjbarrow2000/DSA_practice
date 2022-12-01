def dijkstra(graph, start, finish):
    costs = {}
    parents = {}
    processed = []

    for node in graph:
        if node != start:
            if graph[start].get(node):
                costs[node] = graph[start][node]
                parents[node] = start
            else:
                costs[node] = float("inf")
                parents[node] = None

    while finish not in processed:  # node is not None:
        node = find_lowest_cost_node(costs, processed)
        cost = costs[node]
        neighbors = graph[node]
        for neighbor in neighbors.keys():
            new_cost = cost + neighbors[neighbor]
            if costs[neighbor] > new_cost:
                costs[neighbor] = new_cost
                parents[neighbor] = node
        processed.append(node)

    path = []
    path.append(finish)
    while start not in path:
        path.append(parents[path[-1]])

    path.reverse()
    return path


def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


nodes = ["start", "a", "b", "c", "d", "finish"]

graph = {}
for node in nodes:
    graph[node] = {}

graph["start"]["a"] = 5
graph["start"]["b"] = 2

graph["a"]["c"] = 4
graph["a"]["d"] = 2

graph["b"]["a"] = 8
graph["b"]["d"] = 7

graph["c"]["finish"] = 3
graph["c"]["d"] = 6

graph["d"]["finish"] = 1

start = "start"
finish = "finish"
path = dijkstra(graph, start, finish)
print(path)
