# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitCircularLinkedList(self, list: Optional[ListNode]) -> List[Optional[ListNode]]:

        slow = head = list
        fast = list.next

        while fast.next != head:
            slow = slow.next
            if fast.next.next != head:
                fast = fast.next.next
            else:
                fast = fast.next
        
        secondHead = slow.next
        slow.next = head
        fast.next = secondHead
        return [head, secondHead]