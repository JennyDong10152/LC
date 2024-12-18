# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        firstHead = secondHead = firstTail = secondTail = None
        current = head
        while current:
            if current.val < x:
                if not firstHead:
                    firstHead = firstTail = current
                else:
                    firstTail.next = current
                    firstTail = firstTail.next
            else:
                if not secondHead:
                    secondHead = secondTail = current
                else:
                    secondTail.next = current
                    secondTail = secondTail.next
            current = current.next
        if secondTail:
            secondTail.next = None
        if firstHead:
            firstTail.next = secondHead
            return firstHead
        return secondHead
