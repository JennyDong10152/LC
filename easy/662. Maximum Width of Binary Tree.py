# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxWidth = 0
        queue = deque([(root, 0)])
        while queue:
            size = len(queue)
            node, first = queue[0]
            for _ in range(size):
                node, idx = queue.popleft()
                if node.left:
                    queue.append((node.left, 2*idx))
                if node.right:
                    queue.append((node.right, 2*idx+1))
            maxWidth = max(maxWidth, idx - first + 1)
        return maxWidth