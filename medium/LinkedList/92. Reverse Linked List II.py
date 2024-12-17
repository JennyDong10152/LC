# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = reverseTail = ListNode(0, head)
        for _ in range(left-1):
            reverseTail = reverseTail.next

        current = reverseTail.next
        prev = None
        for _ in range(right-left+1):
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        reverseTail.next.next = current
        reverseTail.next = prev
        return dummy.next