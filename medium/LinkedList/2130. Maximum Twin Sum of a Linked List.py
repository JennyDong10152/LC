# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        slow = fast = head
        maxSum = 0

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        while slow:
            maxSum = max(maxSum, slow.val+stack.pop())
            slow = slow.next
        return maxSum