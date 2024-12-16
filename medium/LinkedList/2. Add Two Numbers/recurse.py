# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = self.add(l1, l2, 0)
        return answer
    
    def add(self, list1, list2, carry):
        if list1 is None and list2 is None and not carry:
            return None

        list1_val = list1.val if list1 else 0
        list2_val = list2.val if list2 else 0
        value = list1_val + list2_val + carry

        carry = value//10
        node = ListNode(value%10)
        node.next = self.add(list1.next if list1 else None, list2.next if list2 else None, carry)
        return node