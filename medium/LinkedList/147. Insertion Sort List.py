# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = head
        curr = head.next

        while curr:
            if curr.val >= prev.val:
                prev = curr
                curr = curr.next
                continue

            insert_idx = dummy
            while curr.val > insert_idx.next.val:
                insert_idx = insert_idx.next
            prev.next = curr.next
            curr.next = insert_idx.next
            insert_idx.next = curr
            curr = prev.next
        return dummy.next