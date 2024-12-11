# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        count = 0
        connecting = False

        while head:
            if head.val in nums:
                if not connecting:
                    count += 1
                connecting = True
            else:
                connecting = False
            head = head.next
        return count