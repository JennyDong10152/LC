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
        if not head or not head.next:
            return head
        
        prev, secondHead = self.findMid(head)
        prev.next = None
        list1 = head
        list2 = self.reverse(secondHead)
        self.merge(list1, list2)
    
    def reverse(self, node):
        current = node
        prev = None
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
    
    def findMid(self, head):
        fast = slow = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return prev, slow

        
