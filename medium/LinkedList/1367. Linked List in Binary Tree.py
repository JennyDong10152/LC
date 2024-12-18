# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isPath(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def isPath(self, head, root):
        if head is None:
            return True
        if root is None or root.val != head.val:
            return False
        return self.isPath(head.next, root.left) or self.isPath(head.next, root.right)