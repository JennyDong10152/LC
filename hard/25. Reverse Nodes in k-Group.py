# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = self.reverse(head, k)
        return node

    def reverse(self, head, k):
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        if length < k:
            return head

        prev = None
        curr = head
        for _ in range(k):
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        head.next = self.reverse(curr, k)
        return prev