# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.array = []
        self.idx = 0
        self.inorder(root)
        
    def inorder(self, node):
        if not node:
            return 
        self.inorder(node.left)
        self.array.append(node.val)
        self.inorder(node.right)

    def next(self) -> int:
        value = self.array[self.idx]
        self.idx += 1
        return value
        
    def hasNext(self) -> bool:
        return self.idx < len(self.array)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()