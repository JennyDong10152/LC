# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        node = dummy = ListNode(0, head)
        while node.next and node.next.next:
            value = node.next.val
            if value == node.next.next.val:
                running = node.next.next
                while running and value == running.val:
                    running = running.next
                node.next  = running
            else:
                node = node.next
        return dummy.next