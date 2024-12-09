# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        firstHead = firstTail = secondHead = secondTail = None
        if head is None:
            return head
        
        curr = head
        while curr:
            if curr.val < x:
                if firstHead is None:
                    firstHead = curr
                    firstTail = curr
                else:
                    firstTail.next = curr
                    firstTail = firstTail.next
            else:
                if secondHead is None:
                    secondHead = curr
                    secondTail = curr
                else:
                    secondTail.next = curr
                    secondTail = secondTail.next
            curr = curr.next
            
        if secondTail is not None:
            secondTail.next = None
        if firstTail is not None:
            firstTail.next = secondHead
        if firstHead is not None:
            return firstHead
        return secondHead