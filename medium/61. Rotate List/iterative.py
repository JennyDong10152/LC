# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = self.getSize(head)
        if size <= 1 or not k or k==size:
            return head
        moveBy = size - (k%size)
        if not moveBy%size:
            return head
        
        prev = None
        curr = head
        for _ in range(moveBy):
            prev = curr
            curr = curr.next
        dummy = curr
        prev.next = None
        while curr.next:
            curr = curr.next
        curr.next = head
        return dummy
        
    
    def getSize(self, node):
        if not node:
            return 0
        cnt = 0
        while node:
            cnt += 1
            node = node.next
        return cnt