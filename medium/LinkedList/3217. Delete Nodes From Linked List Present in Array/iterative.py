# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode(0, head)
        values_to_remove = set(nums)

        while node and node.next:
            if node.next.val in values_to_remove:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next
