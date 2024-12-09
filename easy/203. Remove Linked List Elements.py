# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = node = ListNode(0, head)

        while node and node.next:
            if node.next.val == val:
                running = node.next
                while running and running.val == val:
                    running = running.next
                node.next = running
            else:
                node = node.next
        return dummy.next