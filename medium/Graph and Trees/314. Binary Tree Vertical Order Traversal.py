# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, index = queue.popleft()
            if node:
                order[index].append(node.val)
                
                queue.append((node.left, index - 1))
                queue.append((node.right, index + 1))
                        
        return [order[x] for x in sorted(order.keys())]