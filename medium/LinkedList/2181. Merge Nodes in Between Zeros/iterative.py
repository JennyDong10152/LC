# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        modify = node = head.next
        while node:
            total = 0
            while node.val != 0:
                total += node.val
                node = node.next
            modify.val = total
            node = node.next
            modify.next = node
            modify = modify.next
        return head.next