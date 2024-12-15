# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        firstHead = secondHead = firstTail = secondTail = None
        node = head
        
        while node:
            if node.val < x:
                if not firstHead:
                    firstHead = firstTail = node
                else:
                    firstTail.next = node
                    firstTail = firstTail.next
            else:
                if not secondHead:
                    secondHead = secondTail = node
                else:
                    secondTail.next = node
                    secondTail = secondTail.next
            node = node.next

        if secondTail:
            secondTail.next = None
        if firstHead:
            firstTail.next = secondHead
            return firstHead
        
        return secondHead
