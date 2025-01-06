# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.graph = defaultdict(list)
        self.build_graph(None, root)
        heap = [(0, target.val)]
        visited = set([target.val])
        answer = []

        while heap:
            distance, node = heappop(heap)
            if distance == k:
                answer.append(node)
            if distance > k:
                break
            for neighbor in self.graph[node]:
                if not neighbor in visited:
                    visited.add(neighbor)
                    heappush(heap, (distance+1, neighbor))
        return answer
    
    def build_graph(self, parent, node):
        if parent and node:
            self.graph[parent.val].append(node.val)
            self.graph[node.val].append(parent.val)
        if node.left:
            self.build_graph(node, node.left)
        if node.right:
            self.build_graph(node, node.right)