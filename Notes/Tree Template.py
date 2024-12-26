# Questions regarding finding minPath ->  Dijkastra
# 3243. Shortest Distance After Road Addition Queries I
# 505. The Maze II
# 2577. Minimum Time to Visit a Cell In a Grid.py
# 1514. Path with Maximum Probability
# 1976. Number of Ways to Arrive at Destination

#Iterative Traversals 
def preorderTraversal(root):
    if not root:
        return []
    
    stack = [root]
    result = []
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def inorderTraversal(root):
    stack = []
    result = []
    current = root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        current = current.right
    return result

def postorderTraversal(root):
    if not root:
        return []
    
    stack = [root]
    result = []
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Push left first, then right to process right first
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    # Reverse the result since we collected Root → Right → Left
    return result[::-1]

#For binary trees
# successor: the smallest node after the current one; one step right and go all the way left
# predecessor: the largest node before the current one; one step left and go all the way right
def successor(root: TreeNode) -> TreeNode:
    root = root.right
    while root.left:
        root = root.left
    return root

def predecessor(root: TreeNode) -> TreeNode:
    root = root.left
    while root.right:
        root = root.right
    return root

#Dijkstra
def dijkstra(graph, start):
    # Initialize distances with infinity
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to process nodes
    pq = [(0, start)]  # (distance, node)

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip if the distance in priority queue is outdated
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # Update if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

import heapq

#Prim's minimum spanning tree
def prim(graph, start):
    mst = []  # Stores edges of the Minimum Spanning Tree
    visited = set()  # Track visited nodes
    pq = [(0, start, None)]  # (weight, current_node, parent_node)

    while pq:
        weight, current_node, parent = heapq.heappop(pq)

        # Skip visited nodes
        if current_node in visited:
            continue

        # Add edge to MST (ignore parent for first node)
        if parent is not None:
            mst.append((parent, current_node, weight))
        visited.add(current_node)

        # Explore neighbors
        for neighbor, edge_weight in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, neighbor, current_node))

    return mst