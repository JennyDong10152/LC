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
        canReverse = self.count(head, k)
        if not canReverse:
            return head

        current = head
        prev = None
        for _ in range(k):
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        head.next = self.reverse(current, k)
        return prev
    
    def count(self, head, k):
        cnt = 0
        while head and cnt < k:
            cnt += 1
            head = head.next
        return cnt == k