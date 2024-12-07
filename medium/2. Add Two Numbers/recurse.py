# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.recurse(l1, l2, 0)
    
    def recurse(self, l1, l2, carry):
        if l1 is None and l2 is None and not carry:
            return None

        if l1:
            l1_val = l1.val
            l1_next = l1.next
        else:
            l1_val = 0
            l1_next = None
        if l2:
            l2_val = l2.val
            l2_next = l2.next
        else:
            l2_val = 0
            l2_next = None

        add_on = l1_val + l2_val + carry
        carry = add_on//10
        
        node = ListNode(add_on%10)
        node.next = self.recurse(l1_next, l2_next, carry)
        return node
