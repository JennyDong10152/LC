# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = head
        dummy = curr = head.next
        nextNode = None

        while curr:
            nextNode = curr.next
            curr.next = prev
            if not nextNode or not nextNode.next:
                prev.next = nextNode
                curr = None
            else:
                curr = nextNode.next
                prev.next = curr
                prev = nextNode
        return dummy