# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        values = set(nums)
        node = self.modify(values, head)
        return node
    
    def modify(self, values, head):
        if not head:
            return None
        if head.val in values:
            return self.modify(values, head.next)
        head.next = self.modify(values, head.next)
        return head