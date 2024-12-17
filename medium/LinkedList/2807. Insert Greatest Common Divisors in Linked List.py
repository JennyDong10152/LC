# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        current = head
        while current and current.next:
            greatestDivisor = self.greatestCommonDivisor(current.val, current.next.val)
            current.next = ListNode(val=greatestDivisor, next=current.next)
            current = current.next.next
        return head

    def greatestCommonDivisor(self, num1, num2):
        if not num1:
            return num2
        return self.greatestCommonDivisor(num2 % num1, num1)
