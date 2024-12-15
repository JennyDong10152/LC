# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = start = ListNode(0, head)
        while start:
            prefix = 0
            end = start.next

            while end:
                prefix += end.val
                if not prefix:
                    start.next = end.next
                end = end.next
            start = start.next
        return dummy.next