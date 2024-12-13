# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        
        newHead = head.next
        while newHead.next.val != 0:
            newHead.val += newHead.next.val
            newHead.next = newHead.next.next
        newHead.next = self.mergeNodes(newHead.next)
        return newHead