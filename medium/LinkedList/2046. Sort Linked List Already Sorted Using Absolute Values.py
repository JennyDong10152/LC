# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first = dummy = ListNode(0, head)
        current = head

        while current and current.next:
            if current.next.val < 0:
                negative = current.next
                current.next = current.next.next 
                negative.next = first.next
                first.next = negative
            else:
                current = current.next

        return dummy.next
