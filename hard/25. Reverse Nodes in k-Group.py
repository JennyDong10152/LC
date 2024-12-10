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
        canReverse = self.getSize(head, k)
        if not canReverse:
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
    
    def getSize(self, head, k):
        cnt = 0
        while head and cnt < k:
            head = head.next
            cnt += 1
        return cnt == k