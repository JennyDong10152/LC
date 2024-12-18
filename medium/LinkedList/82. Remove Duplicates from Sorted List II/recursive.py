class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        cur_val = head.val
        if head.next.val == cur_val:
            while head and head.val == cur_val:
                head = head.next
            return self.deleteDuplicates(head)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head