# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        midNode = self.findMid(head)
        secondHead = self.reverse(None, midNode)
        self.merge(head, secondHead, True)
    
    def findMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        midNode = slow.next
        slow.next = None
        return midNode
    
    def reverse(self, first, second):
        if not second:
            return first
        third = second.next
        second.next = first
        return self.reverse(second, third)
    
    def merge(self, list1, list2, isFirst):
        if not list1:
            return list2
        if not list2:
            return list1
        if isFirst:
            list1.next = self.merge(list1.next, list2, False)
            return list1
        else:
            list2.next = self.merge(list1, list2.next, True)
            return list2