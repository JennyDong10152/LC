# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = fast = slow = ListNode(0, head)
        for _ in range(k):
            fast = fast.next
        node1 = fast

        while fast:
            fast = fast.next
            slow = slow.next
        node2 = slow

        node1.val, node2.val = node2.val, node1.val
        return dummy.next
        