# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = prev = ListNode(0, head)
        for _ in range(left-1):
            prev = prev.next
        curr = prev.next

        for _ in range(right-left):
            nextNode = curr.next
            curr.next = nextNode.next
            nextNode.next = prev.next
            prev.next = nextNode
        return dummy.next
