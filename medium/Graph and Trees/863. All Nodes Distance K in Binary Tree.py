# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        self.build_graph(graph, root, None)
        k_distance = []
        visited = set([target.val])
        queue = deque([(target.val, 0)])
        while queue:
            current, distance = queue.popleft()
            if distance == k:
                k_distance.append(current)
                continue
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, distance+1))
        return k_distance

    def build_graph(self, graph, current, parent):
        if current and parent:
            graph[current.val].append(parent.val)
            graph[parent.val].append(current.val)
        if current.left:
            self.build_graph(graph, current.left, current)
        if current.right:
            self.build_graph(graph, current.right, current)