# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        self.double(dummy)
        return dummy if dummy.val else dummy.next
    
    def double(self, node):
        if not node:
            return 0
        num = node.val * 2 + self.double(node.next)
        node.val = num % 10
        return num // 10