# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = self.reverse(None, head)
        return node
    
    def reverse(self, first, second):
        if not second:
            return first
        third = second.next
        second.next = first
        return self.reverse(second, third)