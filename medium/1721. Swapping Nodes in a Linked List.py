# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev1 = prev2 = dummy

        current = dummy
        for _ in range(k):
            prev1 = current
            current = current.next
        node1 = current

        slow = fast = dummy
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            prev2 = slow
            slow = slow.next
        node2 = slow

        if node1 == node2:
            return dummy.next

        prev1.next, prev2.next = node2, node1
        node1.next, node2.next = node2.next, node1.next

        return dummy.next