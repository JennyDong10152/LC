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
        secondHead = self.reverse(midNode)
        self.merge(head, secondHead)
    
    def findMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        midNode = slow.next
        slow.next = None
        return midNode
    
    def reverse(self, head):
        prev = None
        current = head
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        return prev
    
    def merge(self, list1, list2):
        while list2:
            nextNode = list1.next
            list1.next = list2
            list1 = list2
            list2 = nextNode
        
