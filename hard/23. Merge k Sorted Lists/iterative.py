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
        list1 = self.mergeKLists(lists[:mid])
        list2 = self.mergeKLists(lists[mid:])
        return self.merge(list1, list2)
    
    def merge(self, list1, list2):
        current = dummy = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy.next