# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        self.remove(dummy, n)
        return dummy.next
    
    def remove(self, node, n):
        if node is None:
            return 0
        cnt = 1 + self.remove(node.next, n)
        if cnt == n+1:
            node.next = node.next.next
        return cnt