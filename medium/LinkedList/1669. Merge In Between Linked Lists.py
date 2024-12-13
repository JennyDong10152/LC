# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(0, list1)
        list1Tail = list1Head2 = None
        node = list1

        for i in range(b+1):
            if i == a-1:
                list1Tail = node
            node = node.next
        
        list1Head2 = node
        list1Tail.next = list2

        while list2.next:
            list2 = list2.next
        list2.next = list1Head2
        return dummy.next