# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = first = ListNode(0, head)
        node = head
        
        while node and node.next:
            if node.next.val < 0:
                negative = node.next
                node.next = node.next.next
                negative.next = first.next
                first.next = negative
            else:
                node = node.next
        return dummy.next