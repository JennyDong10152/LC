# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        values = set(nums)
        node = head
        count = 0
        isConnected = False
        while node:
            if node.val in values:
                if not isConnected:
                    count += 1
                isConnected = True
            else:
                isConnected = False
            node = node.next
        return count