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
        self.find(root)
        return self.duplicates
    
    def find(self, root):
        if not root:
            return None
        sequence = tuple([self.find(root.left), root.val, self.find(root.right)])
        if sequence in self.visited and self.visited[sequence] == 1:
            self.duplicates.append(root)
        self.visited[sequence] += 1
        return sequence
