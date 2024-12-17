# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(0, list1)
        node = list1

        for i in range(b):
            if i == a-1:
                nodeA = node
            node = node.next

        nodeB = node.next
        nodeA.next = list2

        while list2.next:
            list2 = list2.next
        list2.next = nodeB
        return dummy.next