# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        values_to_remove = set(nums)
        node = self.modify(values_to_remove, head)
        return node
    
    def modify(self, values_to_remove, head):
        if not head:
            return None
        if head.val in values_to_remove:
            return self.modify(values_to_remove, head.next)

        head.next = self.modify(values_to_remove, head.next)
        return head