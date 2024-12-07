# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = new_node = head
        while node:
            length += 1
            node = node.next
        
        remaining = length-n
        if not remaining:
            return head.next
        while remaining > 1:
            new_node = new_node.next
            remaining -= 1
        new_node.next = new_node.next.next
        return head