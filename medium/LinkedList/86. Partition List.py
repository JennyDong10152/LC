# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        firstHead = firstTail = secondHead = secondTail = None
        
        while head:
            if head.val < x:
                if not firstHead:
                    firstHead = head
                    firstTail = head
                else:
                    firstTail.next = head
                    firstTail = firstTail.next
            else:
                if not secondHead:
                    secondHead = head
                    secondTail = head
                else:
                    secondTail.next = head
                    secondTail = secondTail.next
            head = head.next
        
        if secondTail:
            secondTail.next = None
        if firstTail:
            firstTail.next = secondHead
        if firstHead:
            return firstHead
        return secondHead
