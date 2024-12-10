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
        slow = prev = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        list1 = head
        list2 = self.reverse(slow)
        self.merge(list1, list2)
    
    def reverse(self, head):
        if not head:
            return None
        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev
    
    def merge(self, list1, list2):
        while list2:
            nextNode = list1.next
            list1.next = list2
            list1 = list2
            list2 = nextNode

        
