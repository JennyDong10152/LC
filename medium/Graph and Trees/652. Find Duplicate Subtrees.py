# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.visited = defaultdict(int)
        self.duplicates = []
        self.traverse(root)
        return self.duplicates

    def traverse(self, node):
        if not node:
            return None
        sequence = tuple([self.traverse(node.left), node.val, self.traverse(node.right)])
        if sequence in self.visited and self.visited[sequence] == 1:
            self.duplicates.append(node)
        self.visited[sequence] += 1
        return sequence