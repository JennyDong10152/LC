# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        frequency = self.count(head)
        self.delete(dummy, frequency)
        return dummy.next
    
    def delete(self, head, frequency):
        if not head:
            return head
        
        if frequency[head.val] > 1:
            return self.delete(head.next, frequency)
        head.next = self.delete(head.next, frequency)
        return head
    
    def count(self, head):
        frequency = defaultdict(int)
        while head:
            frequency[head.val] += 1
            head = head.next
        return frequency