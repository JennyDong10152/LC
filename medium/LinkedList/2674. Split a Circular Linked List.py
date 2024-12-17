# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitCircularLinkedList(self, list: Optional[ListNode]) -> List[Optional[ListNode]]:
        first = list
        slow = list
        fast = list.next
        while fast.next != first:
            slow = slow.next
            if fast.next.next != first:
                fast = fast.next.next
            else:
                fast = fast.next

        secondHead = slow.next
        slow.next = first
        fast.next = secondHead
        return [first, secondHead]