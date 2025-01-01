# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        order = defaultdict(list)
        queue = deque([(0, root)])
        while queue:
            column, node = queue.popleft()
            order[column].append(node.val)
            if node.left:
                queue.append((column-1, node.left))
            if node.right:
                queue.append((column+1, node.right))
        return [order[key] for key in sorted(order.keys())]