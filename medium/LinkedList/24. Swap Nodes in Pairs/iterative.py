# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        first = head
        dummy = second = first.next

        while second:
            third = second.next
            second.next = first
            if not third or not third.next:
                first.next = third
                second = None
            else:
                second = third.next
                first.next = second
                first = third
        return dummy
