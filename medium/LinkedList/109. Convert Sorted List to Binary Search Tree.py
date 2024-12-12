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
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        array = []
        while head:
            array.append(head.val)
            head = head.next
        n = len(array)
        root = self.sort(array, 0, n-1)
        return root
    
    def sort(self, array, left, right):
        if left > right:
            return None
        mid = left + (right-left)//2
        root = TreeNode(array[mid])
        root.left = self.sort(array, left, mid - 1)
        root.right = self.sort(array, mid + 1, right)
        return root
