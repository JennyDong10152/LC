# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        evenScore = oddScore = 0

        while head and head.next:
            if head.val > head.next.val:
                evenScore += 1
            else:
                oddScore += 1
            head = head.next.next
        if evenScore == oddScore:
            return "Tie"
        elif evenScore > oddScore:
            return "Even"
        return "Odd"