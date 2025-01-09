# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = self.add(l1, l2, 0)
        return node
    
    def add(self, l1, l2, carry):
        if not l1 and not l2 and not carry:
            return 
        
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        num = l1_val + l2_val + carry
        carry = num // 10
        node = ListNode(num % 10)
        node.next = self.add(l1.next if l1 else None, l2.next if l2 else None, carry)
        return node