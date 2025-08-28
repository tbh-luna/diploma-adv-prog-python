# BFS (queue; level‑order)
# [Slide: Breadth Tree Search] (BFS)
# Visit nodes level-by-level from the root using a queue.
# Use an adjacency list dict[Any, list[Any]] - https://www.cs.usfca.edu/~galles/visualization/BFS.html (choose adjacency list)
from collections import deque

<<<<<<< HEAD
def bfs_iterative_search(graph, start_node, goal_node):
    """Return True iff goal_node is reachable from start_node using BFS."""

    # If start node is the goal node itself
=======
def bfs_search(graph, start_node, goal_node):
    """Return True if goal is reachable from start_node using BFS."""
>>>>>>> 532b5e1e549c8e5d10a76816446deb5188d731da
    if start_node == goal_node:
        return True

    # creates a set of nodes visited (only start node for now)
    visited_nodes = set([start_node])

    # creates a deque (Double ended queue) consisting of only the start node
    queue = deque([start_node])

    while queue:
        current_node = queue.popleft()
        for neighbor in graph.get(current_node, []):
            if neighbor == goal_node:
                return True
            if neighbor not in visited_nodes:
                visited_nodes.add(neighbor)
                queue.append(neighbor)
    return False