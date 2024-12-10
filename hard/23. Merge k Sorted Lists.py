# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if not n:
            return None
        if n == 1:
            return lists[0]
        mid = n // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left, right)
    
    def merge(self, left, right):
        dummy = node = ListNode(0)
        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
            
        if left:
            node.next = left
        else:
            node.next = right
        return dummy.next