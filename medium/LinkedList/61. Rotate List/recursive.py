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
        new_head = head
        new_tail = dummy

        while new_head.next:
            new_tail = new_head
            new_head = new_head.next
            cnt += 1
        k = k%cnt

        new_head.next = head
        new_tail.next = None
        return self.rotateRight(new_head, k-1)