# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k:
            return head
        first = head
        length = self.count(head)
        k = k % length
        if not k:
            return head

        slow = fast = ListNode(0, head)
        for _ in range(k):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        secondHead = slow.next
        slow.next = None
        fast.next = first
        return secondHead
    
    def count(self, head):
        cnt = 0
        while head:
            cnt += 1
            head= head.next
        return cnt