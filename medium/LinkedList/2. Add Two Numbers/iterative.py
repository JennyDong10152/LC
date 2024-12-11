# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            add_on = carry + l1_val + l2_val
            carry = add_on // 10
            head.next = ListNode(add_on % 10)

            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next