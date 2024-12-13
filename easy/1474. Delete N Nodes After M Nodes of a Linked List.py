# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        idx = 0

        while head.next:
            idx += 1
            if idx % (m+n) < m:
                head = head.next
            else:
                head.next = head.next.next
        return dummy.next