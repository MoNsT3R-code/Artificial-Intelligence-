import heapq

def astar(graph, heuristic, start, goal):
    """A* graph search. Returns (path, total_cost, expansion_order)."""

    frontier = []
    heapq.heappush(frontier, (0, start))

    came_from = {start: None}
    cost_so_far = {start: 0}
    expansion_order = []

    while frontier:
        _, current = heapq.heappop(frontier)
        expansion_order.append(current)

        if current == goal:
            break

        for neighbor, edge_cost in graph[current]:
            new_cost = cost_so_far[current] + edge_cost

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    # Reconstruct path
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = came_from[node]

    path.reverse()
    total_cost = cost_so_far[goal]

    return path, total_cost, expansion_order


graph = {
    "Main Gate": [("Administration Block", 2)],
    "Administration Block": [("Main Gate", 2), ("Library", 3)],
    "Library": [("Administration Block", 3),
                ("Science Block", 4),
                ("Business Block", 2)],
    "Science Block": [("Library", 4), ("Hostel", 5)],
    "Business Block": [("Library", 2),
                       ("Chapel", 3),
                       ("Sports Complex", 4)],
    "Chapel": [("Business Block", 3),
               ("Cafeteria", 2)],
    "Cafeteria": [("Chapel", 2),
                  ("Sports Complex", 6)],
    "Sports Complex": [("Business Block", 4),
                       ("Cafeteria", 6)],
    "Hostel": [("Science Block", 5)]
}

heuristic = {
    "Main Gate": 7,
    "Administration Block": 6,
    "Library": 4,
    "Science Block": 6,
    "Business Block": 3,
    "Chapel": 2,
    "Cafeteria": 0,
    "Sports Complex": 4,
    "Hostel": 7
}

path, cost, expansions = astar(graph, heuristic, "Main Gate", "Cafeteria")

print("Path:", path)
print("Total Cost:", cost)
print("Expansion Order:", expansions)


'''  
Difference between UCS priority and A priority*

UCS: Priority = g(n) (actual cost from start to node).

A*: Priority = g(n) + h(n) (actual cost + estimated cost to goal).

If all heuristic values are 0, what does A* become?

A* becomes Uniform Cost Search (UCS).

Because priority = g(n) + 0 = g(n).

Why do we store cost_so_far?

To track the cheapest known cost to reach each node.

It prevents revisiting nodes with higher costs and ensures optimal paths.

'''