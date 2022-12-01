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

    print(costs)
    print(parents)

    node = find_lowest_cost_node(costs, processed)
    print(node)
    while finish not in processed:  # node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = n
        processed.append(node)
        print(processed)

        node = find_lowest_cost_node(costs, processed)
        print(node)

    return processed


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
neighbors = graph["b"]
print(neighbors.keys())

print(dijkstra(graph, "start", "finish"))
