# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level_sums = self.calculate(root, [])
        self.replace(root, level_sums)
        return root
    
    def replace(self, node, level_sums):
        queue = deque([node])
        idx = 1
        node.val = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()
                sibling_sum = (current.left.val if current.left else 0) + (current.right.val if current.right else 0)
                if current.left:
                    current.left.val = level_sums[idx]-sibling_sum
                    queue.append(current.left)
                if current.right:
                    current.right.val = level_sums[idx]-sibling_sum
                    queue.append(current.right)
            idx += 1

    def calculate(self, node, level_sums):
        queue = deque([node])
        
        while queue:
            level_sum = 0
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()
                level_sum += current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            level_sums.append(level_sum)
        return level_sums