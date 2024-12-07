# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k:
            return head
        cnt = 1
        dummy = ListNode(0, head)
        curr = head
        prev = dummy

        while curr.next:
            prev = curr
            curr = curr.next
            cnt += 1
        k = k%cnt

        curr.next = head
        prev.next = None
        return self.rotateRight(curr, k-1)
