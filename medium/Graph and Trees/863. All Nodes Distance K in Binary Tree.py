# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.graph = defaultdict(list)
        self.build_graph(root, None)
        k_distance = []
        heap = [(0, target.val)]
        visited = set([target.val])

        while heap:
            distance, node = heappop(heap)
            if distance == k:
                k_distance.append(node)
            if distance > k:
                break
            for neighbor in self.graph[node]:
                if not neighbor in visited:
                    visited.add(neighbor)
                    heappush(heap, (distance+1, neighbor))
        return k_distance

    def build_graph(self, node, parent):
        if node and parent:
            self.graph[node.val].append(parent.val)
            self.graph[parent.val].append(node.val)
        if node.left:
            self.build_graph(node.left, node)
        if node.right:
            self.build_graph(node.right, node)