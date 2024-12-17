# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        self.plus(dummy)
        return dummy if dummy.val else dummy.next

    def plus(self, node):
        if not node.next:
            num = node.val + 1
        else:
            num = node.val + self.plus(node.next)
        node.val = num % 10
        return num // 10