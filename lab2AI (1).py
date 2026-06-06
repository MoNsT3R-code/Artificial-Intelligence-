# COMP360 – Lab 2: Uniform-Cost Search (UCS)

import heapq

def ucs(graph, start, goal):

    """
    Uniform-Cost Search:
    - frontier: priority queue storing (total_cost, node)
    - cost_so_far: best known cost to each node
    - parent: used to reconstruct the final path
    - expansion_order: tracks the order in which nodes are expanded
    """

    frontier = []
    heapq.heappush(frontier, (0, start))  # Start node with cost 0

    cost_so_far = {start: 0}
    parent = {start: None}
    expansion_order = []

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)

        print(f"Popped: {current_node} with cost {current_cost}")

        expansion_order.append(current_node)

        # Task A: Stop if goal reached
        if current_node == goal:
            break

        # Expand neighbors
        for neighbor, step_cost in graph[current_node]:

            # Task B: Accumulate cost correctly
            new_cost = current_cost + step_cost

            # Task C: Update only if new or cheaper path found
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                parent[neighbor] = current_node
                heapq.heappush(frontier, (new_cost, neighbor))

    return parent, cost_so_far, expansion_order


def reconstruct_path(parent, start, goal):
    if goal not in parent:
        return []

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    if not path or path[0] != start:
        return []

    return path


# ===== FCCU Campus Graph (Original) =====

graph = {
    "Main Gate": [("Administration Block", 2)],
    "Administration Block": [("Main Gate", 2), ("Ewing Memorial Library", 4)],
    "Ewing Memorial Library": [("Administration Block", 4), ("Science Block", 3), ("Business Block", 6)],
    "Science Block": [("Ewing Memorial Library", 3)],
    "Business Block": [("Ewing Memorial Library", 6), ("Chapel", 5)],
    "Chapel": [("Business Block", 5), ("Cafeteria", 2)],
    "Cafeteria": [("Chapel", 2)]
}

# ===== Run UCS =====

start = "Main Gate"
goal = "Cafeteria"

parent, cost_so_far, expansion_order = ucs(graph, start, goal)
path = reconstruct_path(parent, start, goal)

print("\nExpansion Order:")
print(" -> ".join(expansion_order))

print("\nShortest Path:")
if path:
    print(" -> ".join(path))
    print("\nTotal Cost:", cost_so_far[goal])
else:
    print("No path found.")



import heapq


def ucs(graph, start, goal):

    """
    Uniform-Cost Search (UCS)

    frontier: priority queue storing (total_cost, node)
    cost_so_far: dictionary storing best known cost to each node
    parent: dictionary to reconstruct final path
    expansion_order: list to track node expansion order
    """

    frontier = []
    heapq.heappush(frontier, (0, start))

    cost_so_far = {start: 0}
    parent = {start: None}
    expansion_order = []

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)

        # Skip outdated entries
        if current_cost > cost_so_far[current_node]:
            continue

        expansion_order.append(current_node)

        # Stop if goal reached
        if current_node == goal:
            break

        # Explore neighbors
        for neighbor, step_cost in graph[current_node]:
            new_cost = current_cost + step_cost

            # Update if new node OR cheaper path found
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                parent[neighbor] = current_node
                heapq.heappush(frontier, (new_cost, neighbor))

    return parent, cost_so_far, expansion_order


def reconstruct_path(parent, start, goal):
    """Reconstruct path from start to goal."""
    if goal not in parent:
        return []

    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = parent[current]

    path.reverse()

    if path[0] != start:
        return []

    return path



original_graph = {
    "Main Gate": [("Administration Block", 2)],
    "Administration Block": [("Main Gate", 2), ("Ewing Memorial Library", 4)],
    "Ewing Memorial Library": [("Administration Block", 4), ("Science Block", 3), ("Business Block", 6)],
    "Science Block": [("Ewing Memorial Library", 3)],
    "Business Block": [("Ewing Memorial Library", 6), ("Chapel", 5)],
    "Chapel": [("Business Block", 5), ("Cafeteria", 2)],
    "Cafeteria": [("Chapel", 2)]
}


# MODIFIED GRAPH (Changed edge cost 6 → 1)


modified_graph = {
    "Main Gate": [("Administration Block", 2)],
    "Administration Block": [("Main Gate", 2), ("Ewing Memorial Library", 4)],
    "Ewing Memorial Library": [("Administration Block", 4), ("Science Block", 3), ("Business Block", 1)],  # changed
    "Science Block": [("Ewing Memorial Library", 3)],
    "Business Block": [("Ewing Memorial Library", 1), ("Chapel", 5)],  # changed
    "Chapel": [("Business Block", 5), ("Cafeteria", 2)],
    "Cafeteria": [("Chapel", 2)]
}



def run_experiment(graph, title):
    print("\n")
    print(title)
    print("\n")

    start = "Main Gate"
    goal = "Cafeteria"

    parent, cost_so_far, expansion_order = ucs(graph, start, goal)
    path = reconstruct_path(parent, start, goal)

    print("\nExpansion Order:")
    print(" -> ".join(expansion_order))

    print("\nShortest Path:")
    if path:
        print(" -> ".join(path))
        print("Total Cost:", cost_so_far[goal])
    else:
        print("No path found.")


# original graph
run_experiment(original_graph, "UCS on Original Graph")

# modified graph
run_experiment(modified_graph, "UCS After Modifying Edge Cost (6 → 1)")

'''
# How and Why the Result Changed

When the edge cost between Ewing Memorial Library and Business Block was reduced from 6 to 1, the total cost of reaching Business Block became smaller than reaching Science Block. Uniform-Cost Search (UCS) always expands the node with the lowest total path cost, Business Block was expanded earlier than before. This changed the expansion order and reduced the overall shortest path cost from 19 to 14. The result changed because UCS decisions depend entirely on cumulative cost, not position or number of steps.

🔹 Reflection (3–4 Sentences Each)

1. Why is UCS optimal when costs are non-negative?
UCS is optimal because it always expands the node with the smallest cumulative path cost first. When all edge costs are non-negative, once a node is removed from the priority queue, we are guaranteed that no cheaper path to that node exists. Therefore, when the goal node is expanded, the path found must be the minimum-cost path. This guarantees optimality.

2. Why does UCS sometimes explore nodes that are not closer to the goal?
UCS does not consider how close a node is to the goal in terms of distance or direction. It only considers the total accumulated cost from the start node. If a node has a lower cumulative cost—even if it moves away from the goal—it will be expanded first. This makes UCS cost-driven rather than goal-directed.

3. How is UCS different from BFS in decision-making?
BFS expands nodes based on the smallest number of edges (level by level), ignoring edge weights. UCS expands nodes based on the smallest cumulative path cost, fully considering edge weights. If all edge costs are equal, UCS behaves exactly like BFS. However, when costs differ, UCS may choose a longer path in terms of steps if it is cheaper overall.

'''